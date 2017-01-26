#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-


import pandas as pd
import numpy as np


x_train = np.empty((0, 7))
y_train = np.empty((0))
for i in range(3):
    df = pd.read_csv("~/fintech_tutorial/data/{0}.tsv".format(i), delimiter="\t")
    x_train = np.append(x_train, np.array(df.ix[0:, 2:]), axis=0)
    y_train = np.append(y_train, np.array(df.ix[0:, 1]), axis=0)

print y_train





