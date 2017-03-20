#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Account(object):
    def __init__(self, _asset = 1000000):
        self.asset = _asset
    def buy(self, _price, _amount):
        self.asset -= _price * _amount
    def sell(self, _price ,_amount):
        self.asset += _price * _amount

def main():
    user = Account()
    print(user.asset)

if __name__ == '__main__':
    main()
