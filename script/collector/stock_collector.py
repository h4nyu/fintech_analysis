#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Get stock quotes from Google Finace and push to my database
"""

import requests

r = requests.get("http://finance.google.com/finance/info?client=ig&q=7751")


r = requests.get("http://download.finance.yahoo.com/d/quotes.csv?s={-listjoin|,|symbol}")

PUBLIC_API_URL = 'https://query.yahooapis.com/v1/public/yql'


print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)
print(r.text)
