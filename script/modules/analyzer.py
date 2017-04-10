#!/usr/bin/env python
# -*- coding: utf-8 -*-
from modules.helper import Reader
from modules.neuralnet import NeuralNet


class Analyzer(object):

    """Docstring for Analyzer. """

    def __init__(self):
        """TODO: to be defined1. """
        self.model = NeuralNet()
        self.reader = Reader()

    def feed_trainings(self, file_paths):
        self.traing_file_paths = file_paths

    def csv_file_config(self, x_start_col, x_end_col, y_start_col, y_end_col):
        self.x_start_col = x_start_col
        self.x_end_col = x_end_col
        self.y_start_col = y_start_col
        self.y_end_col = y_end_col

    def read(self, file_paths):
        self.reader.set_paths(file_paths)
        (x, y) = self.reader.read(self.x_start_col,
                                  self.x_end_col,
                                  self.y_start_col,
                                  self.y_end_col)
        self.y_train = self.reader.change_to_one_hot(y)
        self.x_train = self.reader.normalize(x)

    def training(self,
                 num,
                 threshold,
                 file_paths,
                 batch_size=10,
                 lasso=0.05,
                 **kwargs):

        self.read(file_paths)
        self.model.set_dataset(self.x_train, self.y_train)
        self.model.build_model(l=lasso,
                               sammary=True,
                               **kwargs
                               )
        self.model_paths = []
        for i in range(num):
            self.model.build_model(layer_num=4,
                                   l=lasso)
            score = self.model.fit(batch_size=batch_size)
            if score > threshold:
                model_path = 'traning_model_{0}.h5'.format(i)
                self.model_paths.append(model_path)
                self.model.save(model_path)
                print('save model {0}'.format(model_path))
                # self.model.save_graph('traning_{0}.png'.format(i))

    def grid_search(self, file_paths, **kwargs):
        self.read(file_paths)
        self.model.set_dataset(self.x_train, self.y_train)
        self.model.grid_search(**kwargs)

    def validation(self, file_paths):
        self.validation_file_paths = file_paths
        self.reader.set_paths(self.validation_file_paths)
        (x, y) = self.reader.read(self.x_start_col,
                                  self.x_end_col,
                                  self.y_start_col,
                                  self.y_end_col)
        y = self.reader.change_to_one_hot(y)
        self.model.validate_category(x, y)
