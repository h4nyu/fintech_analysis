#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import csv

with open("/home/yao/fintech_tutorial/data/0.csv") as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        print(row)
