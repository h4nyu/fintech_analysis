#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import csv
from datetime import datetime
from pprint import pprint
from abc import ABCMeta
from abc import abstractmethod
import pandas as pd
import numpy as np


class Dao(metaclass=ABCMeta):

    """Docstring for Dao. """

    def __init__(self):
        """TODO: to be defined1. """
        metaclass = ABCmeta.__init__(self)

    @abstractmethod
    def get_histrical_data(self, symbol, start_date, end_date):
        pass

    @abstractmethod
    def get_quote(self, symbol):
        pass


class YCollector(Dao):

    """Docstring for Collector. """

    def __init__(self):
        """TODO: to be defined1. """
        pass
        self.api_url = 'https://query.yahooapis.com/v1/public/yql?'
        self.datatable_url = 'store://datatables.org/alltableswithkeys'

    def get_histrical_data(self, symbol, start_date, end_date):
        yql = 'select * from yahoo.finance.historicaldata '\
            + 'where symbol = "{0}" '.format(symbol)\
            + 'and startDate = "{0}" '.format(start_date)\
            + 'and endDate = "{0}"'.format(end_date)

        pyload = {
            'q': yql,
            'format': 'json',
            'env': self.datatable_url
        }

        r = requests.get(self.api_url, params=pyload)
        return r.json()['query']['results']['quote']

    def get_quote(self, symbol):
        yql = 'select * from yahoo.finance.quote '\
            + 'where symbol = "{0}" '.format(symbol)

        pyload = {
            'q': yql,
            'format': 'json',
            'env': self.datatable_url
        }

        r = requests.get(self.api_url, params=pyload)

        return r.json()['query']['results']['quote']


class GCollector(Dao):

    """Docstring for Collector. """

    def __init__(self):
        """TODO: to be defined1. """
        self.api_url = 'https://www.google.com/finance/getprices?'

    def get_histrical_data(self, symbol, exchange_code, start_time, interval):
        unix_time = int(start_time.timestamp())
        print(unix_time)

        pyload = {
            'q': symbol,
            'x': exchange_code,
            'i': interval,
            'p': 'Y',
            'df': 'cpct',
            'auto': 1,
            'f': 'd,h,o,c,v',
            'ts': unix_time,
        }

        r = requests.get(self.api_url, params=pyload)
        print(r.url)
        lines = r.text.splitlines()
        f  = [list(map(float, i)) for i in csv.reader(lines[9:])]
        print(len(f))
        # print(type(ts))
        # te = ts + interval * int(prices[-1][0])
        # print(datetime.fromtimestamp(ts))
        # print(datetime.fromtimestamp(te))
        # pprint(r.text)

    def get_quote(self, symbol):
        raise NotImplementedError


if __name__ == "__main__":
    y=GCollector()
    y.get_histrical_data('7751', 'TYO', datetime(2015, 2, 3), 86400)
