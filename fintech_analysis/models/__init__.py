#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .models import FeatureExtractRegressionModel
from .models import FeatureExtractClassificationModel

import inspect
import sys

custom_objects = dict()

for name, obj in inspect.getmembers(sys.modules[__name__]):
    if inspect.isclass(obj):
        custom_objects[obj.__name__] = obj
