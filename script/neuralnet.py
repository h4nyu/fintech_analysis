#!/usr/bin/env python
# -*- coding: utf-8 -*-

from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json
from keras.regularizers import l1
from keras.callbacks import EarlyStopping
import numpy as np
import matplotlib.pyplot as plt


class NeuralNet(object):

    """Docstring for NeuralNet. """

    def __init__(self):
        self.x_train = None
        self.y_train = None
        self.history = None
        self.model = None
        self.input_dim = None
        self.output_dim = None
        self.early_stopping = EarlyStopping(patience=3, verbose=0)

    def save(self, model_path):
        self.model.save(model_path)

    def set_dataset(self, x_train, y_train):
        self.x_train = x_train
        self.y_train = y_train
        self.input_dim = x_train.shape[1]
        self.output_dim = y_train.shape[1]
        print(x_train.shape)
        print(y_train.shape)

    def restore_model(self, model_path, weight_path):
        self.model = model_from_json(model_path)
        self.model.load_weights(weight_path)

    def build_model(self, layer_num):
        layer_nodes = list(np.linspace(
            self.input_dim, self.output_dim, layer_num + 1))
        print(layer_nodes)

        self.model = Sequential()
        self.model.add(Dense(int(layer_nodes[1]),
                             input_shape=(int(layer_nodes[0]),),
                             W_regularizer=l1(0.01)
                             ))

        layer_nodes.pop(0)
        layer_nodes.pop(0)

        for dim in layer_nodes:
            print(dim)
            self.model.add(Dense(int(dim)))

        self.model.summary()

        self.model.compile(loss="mse", optimizer='rmsprop',
                           metrics=['accuracy'])

    def fit(self):
        self.history = self.model.fit(self.x_train,
                                      self.y_train,
                                      nb_epoch=2000,
                                      batch_size=2,
                                      validation_split=0.4,
                                      verbose=2,
                                      callbacks=[self.early_stopping])

    def show_graph(self):
        plt.plot(self.history.history['loss'])
        plt.plot(self.history.history['val_loss'])
        plt.show()


if __name__ == "__main__":
    neuralnet = NeuralNet()
