#!/usr/bin/env python
# -*- coding: utf-8 -*-

from threatbasedalgorithm import Threat
from numpy.random import *
import time
import numpy as np

if __name__ == '__main__':
    value = 110
    cycle = 0
    seed(0)
    user = Threat(120, 100, 1000, value)
    while cycle < 36000:
        if randint(100) % 2 == 0:
            value += np.round(rand(),2) / 10
        else:
            value -= np.round(rand(),2) / 10
        user.input(value)
        cycle += 1
    user.end(value)
