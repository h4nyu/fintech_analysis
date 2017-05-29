#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.request
import urllib.parse
import json
from pprint import pprint

url = "https://query.yahooapis.com/v1/public/yql"
params = {
    "q": 'select * from yahoo.finance.xchange where pair in ("USDJPY")',
    "format": "json",
    "env": "store://datatables.org/alltableswithkeys"
}
url += "?" + urllib.parse.urlencode(params)
res = urllib.request.urlopen(url)

result = json.loads(res.read().decode('utf-8'))
# pprint(result)

rate = result["query"]["results"]["rate"]["Rate"]
time = result["query"]["results"]["rate"]["Time"]
date = result["query"]["results"]["rate"]["Date"]
print('USD/JPY:', rate, date, time)
