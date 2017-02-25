#!/usr/bin/env python
# -*- coding: utf-8 -*-

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Activation
# from keras.layers import Dropout
# from keras.optimizers import SGD
from keras.optimizers import RMSprop
from keras.models import model_from_json
from keras.regularizers import l2
# from keras.regularizers import l1
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
        self.size = None

    def save(self, model_path):
        self.model.save(model_path)

    def set_dataset(self, x_train, y_train):
        self.x_train = x_train
        self.y_train = y_train
        self.input_dim = x_train.shape[1]
        self.output_dim = y_train.shape[1]
        self.size = y_train.shape[0]
        print(x_train.shape)
        print(y_train.shape)

    def restore_model(self, model_path, weight_path):
        self.model = model_from_json(model_path)
        self.model.load_weights(weight_path)

    def build_model(self, layer_num=3):
        layer_nodes = list(np.linspace(
            self.input_dim, self.output_dim, layer_num + 1))
        print(layer_nodes)

        self.model = Sequential()

        self.model.add(Dense(int(layer_nodes[1]),
                             W_regularizer=l2(0.01),
                             input_shape=(int(layer_nodes[0]),)))
        self.model.add(Activation("linear"))

        layer_nodes.pop(0)
        layer_nodes.pop(0)
        layer_nodes.pop(len(layer_nodes) - 1)

        for dim in layer_nodes:
            self.model.add(Dense(int(dim)))
            self.model.add(Activation("softsign"))

        self.model.add(Dense(int(self.output_dim)))
        self.model.add(Activation("linear"))

        self.model.summary()

        # sgd = SGD(lr=0.005, decay=1e-6, momentum=0.9, nesterov=True)
        opt = RMSprop(lr=0.001, rho=0.9, epsilon=1e-08, decay=0.0)

        self.model.compile(loss="mse", optimizer=opt,
                           metrics=['mse'])

    def fit(self):
        self.early_stopping = EarlyStopping(patience=3, verbose=0)
        self.history = self.model.fit(self.x_train,
                                      self.y_train,
                                      nb_epoch=2000,
                                      batch_size=2,
                                      validation_split=0.3,
                                      verbose=2,
                                      callbacks=[self.early_stopping])

    def show_graph(self):
        plt.plot(self.history.history['loss'])
        plt.plot(self.history.history['val_loss'])
        plt.show()

    def predict(self, x_train):
        return self.model.predict(x_train)

    def validate(self, x_train, y_train):
        for ans, pred in zip(y_train, self.predict(x_train)):
            print("ans: {0},\t predict:{1}".format(ans[0], pred[0]))


if __name__ == "__main__":
    neuralnet = NeuralNet()
