#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from keras.models import load_model
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import preprocessing
from keras.utils import np_utils
sns.set()


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
        print(self.model)
        if(self.model is None):
            raise ValueError("model not found")
        self.weights = self.model.get_weights()[0]

    def show_heatmap(self):
        sns.heatmap(self.weights)
        plt.show()

    def set_col_names(self, array):
        self.col_names = list(array)
        if len(array) < len(self.weights):
            for i in range(len(self.weights) - len(array)):
                self.col_names.append("")
        self.col_names = self.col_names[:len(self.weights)]

    def show_abs_bar(self):
        plotlist = []
        for item in self.weights:
            plotlist.append(np.abs(item).sum())
        print("---abs,sum---")
        print(plotlist)
        print("---abs,sum---")
        x = range(len(self.col_names))
        f, axarr = plt.subplots()
        axarr.bar(x, plotlist)
        axarr.set_xticks(x)
        axarr.set_xticklabels(labels=self.col_names)
        plt.show()

    def show_sum_bar(self):
        plotlist = []
        for item in self.weights:
            plotlist.append(item.sum())
        print("---sum---")
        print(plotlist)
        print("---sum---")
        x = range(len(plotlist))
        f, axarr = plt.subplots(1)
        axarr.bar(x, plotlist)
        axarr.set_xticks(x)
        axarr.set_xticklabels(labels=self.col_names)
        plt.show()

    def show_pn_bar(self):
        positives = []
        negatives = []
        print(self.weights.shape)
        for i in self.weights:
            positives.append(i[i > 0].sum())
            negatives.append(i[i < 0].sum())

        print("---positive,sum---")
        print(positives)
        print("---positive,sum---")
        print("---negatives,sum---")
        print(negatives)
        print("---negatives,sum---")
        x = range(len(positives))
        f, axarr = plt.subplots(2)
        axarr[0].bar(x, positives)
        axarr[0].set_xticks(x)
        axarr[0].set_xticklabels(self.col_names)
        axarr[1].bar(x, negatives)
        axarr[1].set_xticks(x)
        axarr[1].set_xticklabels(self.col_names)
        plt.show()

    def show_times(self, row, col):
        self.times = self.plotlist.reshape(row, col)
        for item in self.times:
            plt.scatter(range(len(item)), item)
        plt.show()

    def sum_times(self):
        sum_times = np.sum(self.times, axis=0)
        plt.bar(range(len(sum_times)), sum_times)
        plt.show()


class WeightsVeiwer(WeightVeiwer):

    """Docstring for WeightVeiwer. """

    def __init__(self, file_paths):
        self.file_paths = file_paths
        if(len(file_paths) == 0):
            raise ValueError("no file path")
        self.models = []
        for path in self.file_paths:
            self.models.append(load_model(path))

        self.input_weights_array = []
        for model in self.models:
            self.input_weights_array.append(model.get_weights()[0])
        self.input_weights_array = np.array(self.input_weights_array)
        self.weights = np.mean(self.input_weights_array, axis=0)
