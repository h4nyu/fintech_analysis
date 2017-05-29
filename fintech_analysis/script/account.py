#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Account(object):
    def __init__(self, _asset = 1000000):
        self.asset = _asset
    def buy(self, _price, _amount):
        if _price * _amount <= 100000:
            comm = 100
        if _price * _amount <= 200000:
            comm = 180
        if _price * _amount <= 300000:
            comm = 250
        if _price * _amount <= 400000:
            comm = 350
        if _price * _amount <= 500000:
            comm = 450
        if _price * _amount <= 1000000:
            comm = 1000
        if _price * _amount > 1000000:
            comm + _price * _amount * 0.001
        self.asset -= _price * _amount + comm
    def sell(self, _price , _amount):
        if _price * _amount <= 100000:
            comm = 100
        if _price * _amount <= 200000:
            comm = 180
        if _price * _amount <= 300000:
            comm = 250
        if _price * _amount <= 400000:
            comm = 350
        if _price * _amount <= 500000:
            comm = 450
        if _price * _amount <= 1000000:
            comm = 1000
        if _price * _amount > 1000000:
            comm + _price * _amount * 0.001
        self.asset += _price * _amount - comm
