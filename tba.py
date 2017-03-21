#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

class Threat:
    def __init__(self, _emax=120, _emin=110):
        emax = _emax
        emin = _emax
        #ratio = newton(f, df, 2, 3)
        #print(ratio)
        print(emax,emin)
    def setdata(self, _max, _min, _current):
        print(100)
    def f(x):
        return float(x) - log((emax - emin) / emin) + log(x-1)
    def df(x):
        return 1 - emin / (emax-emin) + 1 / (x-1)
    def newton(f, df, a0, n):
        if n == 0: return a0
        a = newton(f, df, a0, n-1)
        return a - float(f(a)) / df(a)

def main():
    usd = Threat(120, 100)

if __name__ == '__main__':
    main()
