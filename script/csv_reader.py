#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-


import pandas as pd
import numpy as np


df = pd.read_csv("~/fintech_tutorial/data/3.tsv",
                 delimiter="\t")

x_train = np.array(df.ix[0:, 2:])
y_train = np.array(df.ix[0:, 1]).reshape(len(df), 1)
print y_train
