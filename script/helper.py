#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from keras.models import load_model
import matplotlib.pyplot as plt
import seaborn as sns


class DatasetGenerator(object):

    """Docstring for DatasetGenerator. """

    def __init__(self, num_factor):
        self.num_factor = num_factor

    def generate(self, function, row_num):
        facters_set = np.random.rand(row_num, self.num_factor)
        y_train = np.array([function(factors) for factors in facters_set])
        x_train = facters_set
        return (x_train, y_train)


class WeightVeiwer(object):

    """Docstring for WeightVeiwer. """

    def __init__(self, weight_path):
        self.model = load_model(weight_path)

    def show_weight(self):
        sns.heatmap(self.model.get_weights()[0])
        plt.show()


if __name__ == "__main__":
    w = WeightVeiwer("./model.h5")
    w.show_weight()
