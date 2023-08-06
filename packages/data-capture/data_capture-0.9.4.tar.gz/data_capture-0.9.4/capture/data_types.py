# !/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
# Copyright (c) 2022 Baidu.com, Inc. All Rights Reserved
import typing
import PIL.Image
import numpy as np
from pydantic import BaseModel
from typing import Union, Dict


class ModelCollectConfig(BaseModel):
    """Config model"""
    model_name: str = ''
    path: str = ''
    input_enable: bool = True
    prediction_enable: bool = True
    ground_truth_enable: bool = True


class WindmillBlob:
    data: Union[np.ndarray, bytes, typing.IO]
    correlation_id: str
    metadata: Dict = {}


class WindmillImage(WindmillBlob):
    data: Union[np.ndarray, PIL.Image.Image]


class WindmillText(WindmillBlob):
    data: str
