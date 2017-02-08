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
    for i in range(5):
        for i in range(5):
            path = "~/fintech_tutorial/data1/{0}.tsv".format(i)
            df = pd.read_csv(path,
                             delimiter="\t", header=None)
            print("read"
                  + path
                  + "for training")
            x_train = np.append(x_train, np.array(df.ix[0:, 2:]), axis=0)
            y_train = np.append(y_train, np.array(
                df.ix[0:, 1]).reshape(len(df), 1), axis=0)

    model = Sequential()
    model.add(Dense(input_dim=7, output_dim=7))
    model.add(Activation('linear'))
    model.add(Dense(output_dim=7))
    model.add(Activation('relu'))
    model.add(Dense(output_dim=7))
    model.add(Activation('relu'))
    model.add(Dense(output_dim=7))
    model.add(Activation('relu'))
    model.add(Dense(output_dim=1))
    model.add(Activation('linear'))

    model.compile(loss="mse", optimizer='rmsprop', metrics=['accuracy'])
    early_stopping = EarlyStopping(patience=3, verbose=0)
    history = model.fit(x_train, y_train, nb_epoch=2000,
                        batch_size=2,
                        validation_split=0.3,
                        verbose=2,
                        callbacks=[early_stopping])

    path = "~/fintech_tutorial/data1/5.tsv"
    df = pd.read_csv(path,
                     delimiter="\t")

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

    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.show()
