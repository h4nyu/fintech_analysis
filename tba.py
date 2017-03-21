#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np


class Threat(object):

    def __init__(self, _emax=120, _emin=110):
        self.emax = _emax
        self.emin = _emin
        ratio = self.newton(self.f, self.df, 2, 3)
        print(ratio)
        print(self.emax, self.emin)

    def setdata(self, _max, _min, _current):
        print(100)

    def f(self, x):
        return float(x) - np.log((self.emax - self.emin) / float(self.emin)) + np.log(x - 1)

    def df(self, x):
        return 1 - self.emin / (self.emax - self.emin) + 1 / (x - 1)

    def newton(self, f, df, a0, n):
        if n == 0:
            return a0
        a = self.newton(f, df, a0, n - 1)
        return a - float(f(a)) / df(a)


if __name__ == '__main__':
    usd = Threat(120, 100)
