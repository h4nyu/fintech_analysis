#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
import requests
import csv
from datetime import datetime
from io import StringIO
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
        pass

    def get_histrical_data(self, symbol, exchange_code, start_time, interval):
        unix_time = int(start_time.timestamp())
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

        self.prices_url = 'https://www.google.com/finance/getprices?'
        r = requests.get(self.api_url, params=pyload)

        lines = r.text.splitlines()
        prices = [item.split(',') for item in lines[8:]]
        start_timestamp = float(prices[0][0].lstrip('a'))
        prices[0][0] = start_timestamp
        for row in prices[1:]:
            row[0] = start_timestamp + float(row[0])

        return np.array(prices)

    def get_quote(self, symbol):
        pyload = {
            'q': symbol,
        }
        self.quote_url = 'https://www.google.com/finance/info?'
        r = requests.get(self.quote_url, params=pyload)
        return r.text


if __name__ == "__main__":
    y = GCollector()
    pprint(y.get_quote('7751'))

