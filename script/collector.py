#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
from pprint import pprint


class Collector(object):

    """Docstring for Collector. """

    def __init__(self):
        """TODO: to be defined1. """
        pass
        self.yql_url = 'https://query.yahooapis.com/v1/public/yql?'

    def get_histrical_data(self, symbol, start_date, end_date):

        pyload = {
            'q': 'select * from yahoo.finance.historicaldata where symbol = "{0}" and startDate = "{1}" and endDate = "{2}"'.format(symbol, start_date, end_date),
            'format': 'json',
            'env': 'store://datatables.org/alltableswithkeys'
        }

        r = requests.get(self.yql_url, params=pyload)
        return r.json()

    def get_quote(self, symbol, start_date, end_date):

        pyload = {
            'q': 'select * from yahoo.finance.quote where symbol = "{0}"',
            'format': 'json',
            'env': 'store://datatables.org/alltableswithkeys'
        }.format(symbol, start_date, end_date)

        r = requests.get(self.yql_url, params=pyload)

        return r.json()


if __name__ == "__main__":
    c = Collector()
    c.get_histrical_data('YHOO', '2014-02-11', '2014-02-18')
