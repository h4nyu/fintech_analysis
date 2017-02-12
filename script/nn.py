#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.callbacks import EarlyStopping
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':

    x_train = np.empty((0, 6))
    y_train = np.empty((0, 1))
    drop_col = 4
    for i in range(10):
        for i in range(1):
            path = "~/fintech_tutorial/data2/{0}.tsv".format(i)
            df = pd.read_csv(path,
                             delimiter="\t", header=None)
            df = df.drop(drop_col, axis=1)
            print("read "
                  + path
                  + " for training")
            x_train = np.append(x_train, np.array(df.ix[0:, 2:]), axis=0)
            y_train = np.append(y_train, np.array(
                df.ix[0:, 1]).reshape(len(df), 1), axis=0)

    model = Sequential()
    model.add(Dense(input_dim=6, output_dim=6))
    model.add(Activation('linear'))
    model.add(Dense(input_dim=6, output_dim=6))
    model.add(Activation('relu'))
    model.add(Dense(input_dim=6, output_dim=6))
    model.add(Activation('relu'))
    model.add(Dense(input_dim=6, output_dim=1))
    model.add(Activation('linear'))

    model.compile(loss="mse", optimizer='rmsprop', metrics=['accuracy'])
    early_stopping = EarlyStopping(patience=3, verbose=0)
    history = model.fit(x_train, y_train, nb_epoch=2000,
                        batch_size=2,
                        validation_split=0.4,
                        verbose=2,
                        callbacks=[early_stopping])

    path = "~/fintech_tutorial/data2/1.tsv"
    df = pd.read_csv(path,
                     delimiter="\t", header=None)

    df = df.drop(drop_col, axis=1)

    print("read"
          + path
          + "for validation")

    x_train = np.array(df.ix[0:, 2:])
    y_train = np.array(df.ix[0:, 1]).reshape(len(df), 1)

    predict_y = model.predict(x_train)
    for (predict, answer) in zip(predict_y, y_train):
        diff = abs((answer - predict))
        print("predict:{0}, answer:{1}, diff:{2}".format(
            predict, answer, diff))

    #     header = ["sharpe",
    #               "alpha",
    #               "beta",
    #               "sortino",
    #               "col0",
    #               "col1",
    #               "col2"]
    #     header = header.remove(drop_col)
    #
    # for h, w in zip(header, model.get_weights()[0]):
    #     print("weight of {0} is {1}".format(h, w))
    #
    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.show()
