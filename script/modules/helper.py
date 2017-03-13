#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from keras.models import load_model
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn import preprocessing
from keras.utils import np_utils
from pprint import pprint
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


class Reader(object):

    """Docstring for Reader. """

    def __init__(self):
        self.file_path_list = None

    def set_paths(self, file_path_list):
        self.file_path_list = file_path_list

    def read(self, x_start_col, x_end_col, y_start_col, y_end_col):
        x_train = np.empty((0, x_end_col - x_start_col + 1))
        y_train = np.empty((0, y_start_col - y_end_col + 1))
        for path in self.file_path_list:
            df = pd.read_csv(path,
                             delimiter=",", header=None)
            print("read"
                  + path
                  + "for training")
            x_train = np.append(x_train,
                                np.array(df.ix[0:, x_start_col:x_end_col]),
                                axis=0)

            y_train = np.append(y_train,
                                np.array(df.ix[0:, y_start_col:y_end_col]),
                                axis=0)

        self.x_train = x_train
        self.y_train = y_train
        return (self.x_train, self.y_train)

    def change_to_one_hot(self, y_train):
        max_num = int(np.max(y_train))
        min_num = int(np.min(y_train))
        span = max_num - min_num
        y_int_train = np.array([int(i > 0) for i in y_train])

        return np_utils.to_categorical(y_int_train)

    def get_time_window_dataset(self):
        x_train_2 = []
        y_train_2 = []

        for i in range(len(self.x_train) - 3):
            x_train_2.append(np.concatenate((self.x_train[i],
                                             self.x_train[i + 1],
                                             self.x_train[i + 2],
                                             self.x_train[i + 3])))
            y_train_2.append(self.y_train[i + 3])

        self.x_train_2 = np.array(x_train_2)
        self.y_train_2 = np.array(y_train_2)
        return (self.x_train_2, self.y_train_2)

    def normalize(self):
        self.x_train = preprocessing.normalize(self.x_train, axis=0, norm='l2')
        self.y_train = preprocessing.normalize(self.y_train, axis=0, norm='l2')
        return (self.x_train, self.y_train)


class WeightVeiwer(object):

    """Docstring for WeightVeiwer. """

    def __init__(self, weight_path):
        self.model = load_model(weight_path)
        self.input_weights = self.model.get_weights()[0]

    def show_heatmap(self):
        sns.heatmap(self.input_weights)
        plt.show()

    def show_bar(self):
        self.plotlist = []
        for item in self.model.get_weights()[0]:
            self.plotlist.append(np.abs(item).sum())
        self.plotlist = np.array(self.plotlist)
        print(self.plotlist)
        plt.bar(range(len(self.plotlist)), self.plotlist)
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


if __name__ == "__main__":
    file_path_list = []
    for i in range(1):
        file_path_list.append(
            '~/fintech_tutorial/dataset/datadsq8/{0}.csv'.format(i))

    x_start_col = 2
    x_end_col = 9
    y_start_col = 1
    y_end_col = 1

    reader = Reader()
    reader.set_paths(file_path_list)
    (x_train, y_train) = reader.read(x_start_col,
                                     x_end_col,
                                     y_start_col,
                                     y_end_col)
    pprint(reader.change_to_one_hot(y_train))
