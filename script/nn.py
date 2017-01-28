#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.callbacks import EarlyStopping
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':

    x_train = np.empty((0, 7))
    y_train = np.empty((0, 1))
    for i in range(1):
        df = pd.read_csv("~/fintech_tutorial/data/{0}.tsv".format(i),
                         delimiter="\t")
        x_train = np.append(x_train, np.array(df.ix[0:, 2:]), axis=0)
        y_train = np.append(y_train, np.array(
            df.ix[0:, 1]).reshape(len(df), 1), axis=0)

    print(x_train[0])
    print(y_train[0])

    model = Sequential()
    model.add(Dense(output_dim=7, input_dim=7))
    model.add(Activation('tanh'))
    model.add(Dense(input_dim=7, output_dim=7))
    model.add(Activation('tanh'))
    model.add(Dense(output_dim=1))
    model.add(Activation('linear'))

    model.compile(loss="mse", optimizer='rmsprop', metrics=['accuracy'])
    early_stopping = EarlyStopping(patience=3, verbose=1)
    history = model.fit(x_train, y_train, nb_epoch=200,
                        batch_size=1,
                        validation_split=0.2,
                        callbacks=[early_stopping])

    df = pd.read_csv("~/fintech_tutorial/data/3.tsv",
                     delimiter="\t")

    x_train = np.array(df.ix[0:, 2:])
    y_train = np.array(df.ix[0:, 1]).reshape(len(df), 1)

    print x_train[0:3]
    print model.predict(x_train)

    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.show()
