#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np

class Threat(object):

    def __init__(self, _emax, _emin, _asset):
        self.asset = self.init = _asset
        self.emax = _emax
        self.emin = _emin
        self.vmax = 0
        self.vmin = 0
        self.balance = 0
        self.ratio = self.newton(1.15, 5)

    def input(self, _current):
        if _current > self.vmax:
            self.vmax = _current
            opt = self.init * self.vmax
            sell = np.round((opt - self.asset * self.emin * self.ratio)  / self.ratio / (self.vmax - self.emin), 0)
            if sell > 0:
                self.asset -= sell
                self.balance += sell * self.vmax
                opt =  self.vmax * self.init
                compratio = np.round(opt / (self.balance + self.asset * self.vmax), 3)
                # print("SELL", sell)
                print(sell, self.asset, self.balance, compratio)

    def f(self, x):
        return float(x) - np.log((float(self.emax) / float(self.emin)) - 1) + np.log(x - 1)

    def df(self, x):
        return x / (x - 1)

    def newton(self, value, cycle):
        if cycle == 0:
            return value
        value = value - self.f(value) / self.df(value)
        return self.newton(value, cycle - 1)

# DEBUG STATUS
if __name__ == '__main__':
    usd = Threat(120, 100, 10000)
    usd.input(110)
