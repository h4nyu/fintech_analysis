#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
import requests
import csv
from datetime import datetime
from datetime import timedelta
from io import StringIO
from pprint import pprint
from abc import ABCMeta
from abc import abstractmethod
import pandas as pd
import numpy as np
import json


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


class DataChunk(object):

    """Docstring for DataChunk. """

    def __init__(self):
        """TODO: to be defined1. """
        self.timestamp_header = None
        self.frames = None
        self.interval = None
        self.colums = None
        self.date_sessions = None
        self.timezone_offset = None

    def read_text(self, text):
        pass


class Frame(object):

    """Docstring for DataChunk. """

    def __init__(self):
        """TODO: to be defined1. """
        self.timestamp_header = None
        self.frames = None


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
        self.base_timestamp = None

    def get_histrical_data(self,
                           symbol,
                           start_time,
                           end_date,
                           interval,
                           exchange_code='TYO'
                           ):
        if interval < 60:
            interval = 60

        unix_time = start_time.timestamp()
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

        r = requests.get(self.prices_url, params=pyload)

        lines = r.text.split('\n')
        header_lines = lines[:8]
        columns = header_lines[4][8:].split(',')

        self.interval = int(header_lines[3][9:])
        self.offset = int(header_lines[7][16:])
        pprint(self.interval)

        body_lines = [line.split(',') for line in lines[8:]]

        df = pd.DataFrame(body_lines, columns=columns)
        df = df.dropna()

        df["DATE"] = df["DATE"].map(
            lambda x: self.convert_timestamp(x, interval))
        df = df.astype(float)
        df["DATE"] = df["DATE"].map(lambda x: datetime.fromtimestamp(x))

        return df

    def convert_timestamp(self, line, interval):
        if("a" in line):
            line = float(line.lstrip('a'))
            self.base_timestamp = line
        else:
            line = self.base_timestamp + float(line) * interval
        return float(line) + self.offset

    def get_quote(self, symbol):
        pyload = {
            'q': symbol,
        }
        self.quote_url = 'https://www.google.com/finance/info?'
        r = requests.get(self.quote_url, params=pyload)
        text = r.text[3:]
        return json.loads(text)[0]


if __name__ == "__main__":
    y = GCollector()
    r = y.get_histrical_data(7751, datetime.now() -
                             timedelta(days=100), datetime.now())
    pprint(r)
