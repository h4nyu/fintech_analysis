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
        return 1 + 1 / (x - 1)

    def newton(self):
        return self._newton(self.f, self.df, 2, 3)

    def _newton(self, f, df, a0, n):
        if n == 0:
            return a0
        a = self._newton(f, df, a0, n - 1)
        return a - float(f(a)) / df(a)

if __name__ == '__main__':
    usd = Threat(120, 100)
    print(usd.newton())
