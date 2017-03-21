#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np

class Threat(object):

    def __init__(self, _emax=120, _emin=110):
        self.emax = _emax
        self.emin = _emin

    def setdata(self, _max, _min, _current):
        print(100)

    def f(self, x):
        return float(x) - np.log((float(self.emax) / float(self.emin)) - 1) + np.log(x - 1)

    def df(self, x):
        return x / (x - 1)

    def newton(self, value, cycle):
        if cycle == 0:
            return value
        value = value - self.f(value) / self.df(value)
        return self.newton(value, cycle - 1)


if __name__ == '__main__':
    usd = Threat(120, 100)
    value = usd.newton(1.15, 5)
    print(value)
