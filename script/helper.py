#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np


class DatasetGenerator(object):

    """Docstring for DatasetGenerator. """

    def __init__(self, num_factor):
        self.num_factor = num_factor

    def generate(self, function, row_num):
        facters_set = np.random.rand(row_num, self.num_factor)
        y_train = np.array([function(factors) for factors in facters_set])
        x_train = facters_set
        return (x_train, y_train)


def function(factors):
    return factors[0] + factors[1]


class Reader(object):

    """Docstring for Reader. """

    def __init__(self):
        pass


if __name__ == "__main__":
    g = DatasetGenerator(10)
    g.generate(function, 100)
    for i in np.linspace(3, 8, 3):
        print(i)
        print int(i)
