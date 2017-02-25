#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
import requests
from pprint import pprint
import matplotlib.pyplot as plt


class Collector(object):

    """Docstring for Collector. """

    def __init__(self):
        """TODO: to be defined1. """
        pass
        self.yql_url = 'https://query.yahooapis.com/v1/public/yql?'
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

        r = requests.get(self.yql_url, params=pyload)
        return r.json()['query']['results']['quote']

    def get_quote(self, symbol):
        yql = 'select * from yahoo.finance.quote '\
            + 'where symbol = "{0}" '.format(symbol)

        pyload = {
            'q': yql,
            'format': 'json',
            'env': self.datatable_url
        }

        r = requests.get(self.yql_url, params=pyload)

        return r.json()['query']


if __name__ == "__main__":
    c = Collector()
    r = c.get_histrical_data('YHOO', '2014-02-11', '2014-02-18')
    closes = [float(i['Close']) for i in r]
    opens = [float(i['Open']) for i in r]
    highs = [float(i['High']) for i in r]
    lows = [float(i['Low']) for i in r]
    plt.plot(closes)
    plt.plot(opens)
    plt.plot(highs)
    plt.plot(lows)
    plt.show()

