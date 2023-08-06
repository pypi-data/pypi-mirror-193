# !/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
# Copyright (c) 2022 Baidu.com, Inc. All Rights Reserved
"""
capture logger library
"""
import datetime
import json
import os
import sys
import time
import numpy as np
import PIL.Image
from logging.handlers import RotatingFileHandler
from loguru import logger as loguru_logger
from typing import Union, Sequence, Dict, List, Any, Mapping

from .utils import get_model_name, gen_correlation_id, NpEncoder
from .constants import DEFAULT_CAPTURE_IMAGE_DIR_PATH, TIME_DIRECTORY_FORMAT, CAPTURE_DATA_DIR, \
    DEFAULT_CAPTURE_DATA_PATH, ENABLE_CAPTURE_INPUT, ENABLE_CAPTURE_PREDICTION, ENABLE_CAPTURE_GROUND_TRUTH, \
    DEFAULT_CAPTURE_BLOB_DIR_PATH
from .data_types import ModelCollectConfig, WindmillBlob, WindmillImage, WindmillText


def _is_pillow_image(img):
    return isinstance(img, PIL.Image.Image)


def _is_numpy_array(img):
    return isinstance(img, np.ndarray)


def _is_windmill_image(img):
    return isinstance(img, WindmillImage)


class CaptureClient:
    """
    CaptureClient
    """

    def __init__(self, config: ModelCollectConfig):
        """
        init logger
        :path log_dir_path:
        """
        self._load_env_setting_and_config(config)
        self._init_base_logger()

    def _init_base_logger(self):
        """
        init base logger
        :return:
        """
        # 取消console log的输出
        loguru_logger.remove(handler_id=None)
        log_file_path = f"{self.path}/predictions/result.jsonl"
        handler = RotatingFileHandler(
            log_file_path,
            maxBytes=100 * 1024 * 1024,
            mode='w',
            backupCount=10,
            encoding='utf-8',
        )
        # 异步，避免阻塞 编码格式设置为utf-8
        loguru_logger.add(handler, enqueue=True, level='INFO')
        self._logger = loguru_logger.opt(lazy=True).opt(colors=False).opt(raw=True)
        self._logger.info("init logger success")
        if self._is_data_capture_enable() is False:
            self._logger.remove(handler_id=None)

    def _is_data_capture_enable(self):
        """
        check is need print log
        :return:
        """
        return self.is_enable_capture_input and \
            self.is_enable_capture_prediction and \
            self.is_enable_capture_ground_truth

    def _gen_image_save_path(self, correlation_id: str) -> str:
        """
        generate image tmp save dir as yyyy-MM-dd/hh
        :return:
        """
        # generate time directory
        time_tuple = time.localtime(int(time.time()))
        dir_name = os.path.join(f"{self.path}/{DEFAULT_CAPTURE_IMAGE_DIR_PATH}",
                                time.strftime(TIME_DIRECTORY_FORMAT, time_tuple))
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
        file_name = f"{dir_name}/{correlation_id}.png"
        return file_name

    def log(self,
            correlation_id: str,
            data: Dict[str, Any] = None,
            blob: Union[WindmillImage, WindmillText, WindmillBlob] = None,
            image: Union[WindmillImage, np.ndarray, PIL.Image.Image] = None,
            text: Sequence = None,
            time_series: Sequence = None,
            input: Union[Dict, List, str] = None,
            prediction: Union[Dict, List, str] = None,
            ground_truth: Union[Dict, List] = None,
            config: ModelCollectConfig = None,
            ):
        """
        data capture main log function
        :param input:
        :param correlation_id:
        :param data:
        :param blob:
        :param image:
        :param text:
        :param time_series:
        :param prediction:
        :param ground_truth:
        :param config:
        :return:
        """

        if config is not None:
            self._load_env_setting_and_config(config)
            self._init_base_logger()

        message = {
            'timestamp': datetime.datetime.now(datetime.timezone.utc).isoformat(),
            'correlation_id': correlation_id,
            'model_name': self.model_name,
        }

        if data is not None:
            if not isinstance(data, Mapping):
                raise ValueError("data must be passed a dictionary")

            if any(not isinstance(key, str) for key in data.keys()):
                raise ValueError("Key values passed to data must be strings.")

            for k, v in data.items():
                if isinstance(v, (list, dict)):
                    message[k] = json.dumps(v, cls=NpEncoder)
                if isinstance(v, (int, float, str)):
                    message[k] = v
                if _is_windmill_image(v) or _is_numpy_array(v) or _is_pillow_image(v):
                    self._log_image(correlation_id, v)
                if isinstance(v, WindmillBlob):
                    self._log_blob(correlation_id, v)

        if input is not None:
            message['input'] = input if isinstance(input, str) else json.dumps(input, cls=NpEncoder)

        if prediction is not None:
            message['prediction'] = prediction if isinstance(prediction, str) else json.dumps(prediction,
                                                                                              cls=NpEncoder)

        if ground_truth is not None:
            message['ground_truth'] = ground_truth if isinstance(ground_truth, str) else json.dumps(ground_truth,
                                                                                                    cls=NpEncoder)

        if image is not None:
            self._log_image(correlation_id, image)

        if blob is None:
            self._log_blob(correlation_id, blob)

        self._record(message)

    def _record(self, message: Dict):
        """
        record log
        :param message:
        :return:
        """
        json_encode_message = json.dumps(message, cls=NpEncoder)
        self._logger.info(json_encode_message)

    def _load_env_setting_and_config(self, config: ModelCollectConfig):
        """
        load env setting and config
        :param config:
        :return:
        """
        self.model_name = config.model_name if config.model_name is not None else get_model_name()

        env_capture_path = os.environ.get(CAPTURE_DATA_DIR)
        config.path = config.path.rstrip("/") if config.path is not None else env_capture_path.rstrip("/")
        self.path = config.path if config.path is not None else DEFAULT_CAPTURE_DATA_PATH

        self.is_enable_capture_input = config.input_enable if config.input_enable is not None else os.environ.get(
            ENABLE_CAPTURE_INPUT) == "True"
        self.is_enable_capture_prediction = config.prediction_enable if config.prediction_enable is not None \
            else os.environ.get(ENABLE_CAPTURE_PREDICTION) == "True"
        self.is_enable_capture_ground_truth = config.ground_truth_enable if config.ground_truth_enable is not None \
            else os.environ.get(ENABLE_CAPTURE_GROUND_TRUTH) == "True"

    def _log_image(self,
                   correlation_id: str,
                   image: Union[WindmillImage, np.ndarray, PIL.Image.Image],
                   metadata: Dict = None):

        def _normalize_to_uint8(x):
            # Based on: https://github.com/matplotlib/matplotlib/blob/06567e021f21be046b6d6dcf00380c1cb9adaf3c/lib/matplotlib/image.py#L684

            is_int = np.issubdtype(x.dtype, np.integer)
            low = 0
            high = 255 if is_int else 1
            if x.min() < low or x.max() > high:
                msg = (
                    "Out-of-range values are detected. "
                    "Clipping array (dtype: '{}') to [{}, {}]".format(x.dtype, low, high)
                )
                self._logger.warning(msg)
                x = np.clip(x, low, high)

            # float or bool
            if not is_int:
                x = x * 255

            return x.astype(np.uint8)

        with self._gen_image_save_path(correlation_id) as tmp_path:
            if "PIL" in sys.modules and _is_pillow_image(image):
                image.save(tmp_path, format="PNG")
            elif "numpy" in sys.modules and _is_numpy_array(image):
                import numpy as np

                try:
                    from PIL import Image
                except ImportError as exc:
                    from PIL import Image
                    raise ImportError(
                        "`log_image` requires Pillow to serialize a numpy array as an image."
                        "Please install it via: pip install Pillow"
                    ) from exc

                # Ref.: https://numpy.org/doc/stable/reference/generated/numpy.dtype.kind.html#numpy-dtype-kind
                valid_data_types = {
                    "b": "bool",
                    "i": "signed integer",
                    "u": "unsigned integer",
                    "f": "floating",
                }

                if image.dtype.kind not in valid_data_types:
                    raise TypeError(
                        f"Invalid array data type: '{image.dtype}'. "
                        f"Must be one of {list(valid_data_types.values())}"
                    )

                if image.ndim not in [2, 3]:
                    raise ValueError(
                        "`image` must be a 2D or 3D array but got a {}D array".format(image.ndim)
                    )

                if (image.ndim == 3) and (image.shape[2] not in [1, 3, 4]):
                    raise ValueError(
                        "Invalid channel length: {}. Must be one of [1, 3, 4]".format(
                            image.shape[2]
                        )
                    )

                # squeeze a 3D grayscale image since `Image.fromarray` doesn't accept it.
                if image.ndim == 3 and image.shape[2] == 1:
                    image = image[:, :, 0]

                image = _normalize_to_uint8(image)

                Image.fromarray(image).save(tmp_path)

            elif _is_windmill_image(image):
                if correlation_id is None:
                    correlation_id = image.correlation_id
                self._log_image(correlation_id, image.data, image.metadata)
            else:
                raise TypeError("Unsupported image object type: '{}'".format(type(image)))

    def _log_blob(self, correlation_id: str, blob: WindmillBlob):
        with self._gen_blob_save_path(correlation_id, blob.metadata['extension']) as tmp_path:
            with open(tmp_path, "wb", encoding="utf-8") as f:
                f.write(blob.data)

    def _gen_blob_save_path(self, correlation_id, extension):
        """
        generate blob save path
        :param correlation_id:
        :return:
        """
        time_tuple = time.localtime(int(time.time()))
        dir_name = os.path.join(f"{self.path}/{DEFAULT_CAPTURE_BLOB_DIR_PATH}",
                                time.strftime(TIME_DIRECTORY_FORMAT, time_tuple))
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
        return f"{dir_name}/{correlation_id}.{extension}"
