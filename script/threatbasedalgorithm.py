#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np

class Threat(object):

    def __init__(self, _emax, _emin, _asset, _buy):
        self.asset = self.init = _asset
        self.emax = _emax
        self.emin = _emin
        self.buy = self.vmax = self.vmin = _buy
        self.balance = 0
        self.ratio = self.newton(1.15, 5)

    def input(self, _current):
        if _current > self.vmax:
            self.vmax = _current
            opt = self.init * self.vmax
            sell = np.round((opt - self.asset * self.emin * self.ratio - self.balance * self.ratio)  / self.ratio / (self.vmax - self.emin), 0)
            if sell > 0:
                self.asset -= sell
                self.balance += sell * self.vmax
                # 最適オフラインアルゴリズムの利益
                opt =  self.vmax * self.init
                # 現時点での競合比
                self.compratio = np.round(opt / (self.balance + self.asset * self.vmax), 3)
                # 資産
                total = self.balance + self.asset * self.vmax
                # 利益
                benefit = total - self.buy * self.init
                # print("SELL", sell)
                # print(sell, self.asset, self.balance, compratio, benefit)
        if _current < self.vmin:
            self.vmin = _current

    def end(self, _current):
        opt = self.vmax * self.init
        total = self.balance + self.asset * _current
        benefit = total - self.buy * self.init
        print("MAX=",self.vmax,"MIN=",self.vmin)
        print("OPT=",opt, "ALG=",total, "CR=",self.compratio, "BENEFIT=",benefit)

    def f(self, x):
        return float(x) - np.log((float(self.emax) / float(self.emin)) - 1) + np.log(x - 1)

    def df(self, x):
        return x / (x - 1)

    def newton(self, value, cycle):
        if cycle == 0:
            return value
        value = value - self.f(value) / self.df(value)
        return self.newton(value, cycle - 1)
