#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import numpy as np
from keras.utils import np_utils
from sklearn import preprocessing
import pandas as pd


class Reader(object):

    """Docstring for Reader. """

    def __init__(self):
        self.file_path_list = None

    def set_files(self, file_path_list):
        self.file_path_list = file_path_list

    def set_dir(self, dir_path, file_type="csv"):
        file_path_list = []
        abspath = os.path.abspath(dir_path)
        file_names = os.listdir(abspath)
        for file_name in file_names:
            root, ext = os.path.splitext(file_name)
            if ext == ".csv":
                file_path_list.append(os.path.join(abspath, file_name))
        self.file_path_list = file_path_list
        return file_path_list

    def read(self, input_cols, output_cols, verbose=False):
        x_train = np.empty((0, len(input_cols)))
        y_train = np.empty((0, len(output_cols)))

        for path in self.file_path_list:
            df = pd.read_csv(path, delimiter=",", header=None)
            shape = df.shape
            if max(input_cols) > shape[1] - 1 or max(output_cols) > shape[1] - 1:
                raise ValueError("invalid col. shape is {}".format(shape))

            if verbose is True:
                print("reading..." + path)
            x_train = np.append(x_train,
                                np.array(df.ix[0:, input_cols]),
                                axis=0)

            y_train = np.append(y_train,
                                np.array(df.ix[0:, output_cols]),
                                axis=0)

        self.x_train = x_train
        self.y_train = y_train
        return (self.x_train, self.y_train)

    def change_to_one_hot(self, y_train):
        y_int_train = np.array([int(i > 0) for i in y_train])
        return np_utils.to_categorical(y_int_train)

    def get_time_window_dataset(self, step=5):
        x_train_2 = []
        y_train_2 = []

        for i in range(len(self.x_train) - step):
            img = []
            for s in range(step):
                img.append(self.x_train[i + s])
            x_train_2.append(img)
            y_train_2.append(self.y_train[i + step])

        self.x_train_2 = np.array(x_train_2)
        self.y_train_2 = np.array(y_train_2)
        return (self.x_train_2, self.y_train_2)

    def set_nam_values(self, col, m_value):
        self.x_train_2
        return (self.x_train_2, self.y_train_2)

    def normalize(self, array):
        return preprocessing.normalize(array, axis=0, norm='l2')
