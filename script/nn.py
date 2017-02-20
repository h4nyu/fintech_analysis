#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.callbacks import EarlyStopping
from keras.regularizers import l2
from keras.regularizers import activity_l2
from keras.regularizers import l1
from keras.regularizers import activity_l1
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

if __name__ == '__main__':

    x_train = np.empty((0, 7))
    y_train = np.empty((0, 1))
    for i in range(10):
        for i in range(1):
            path = "~/fintech_tutorial/data2/{0}.tsv".format(i)
            df = pd.read_csv(path,
                             delimiter="\t", header=None)
            print("read"
                  + path
                  + "for training")
            x_train = np.append(x_train, np.array(df.ix[0:, 2:]), axis=0)
            y_train = np.append(y_train, np.array(
                df.ix[0:, 1]).reshape(len(df), 1), axis=0)

    model = Sequential()
    model.add(Dense(input_dim=7, output_dim=6, W_regularizer=l1(0.01)))
    model.add(Activation('linear'))
    model.add(Dense(output_dim=5))
    model.add(Activation('relu'))
    model.add(Dense(output_dim=4))
    model.add(Activation('relu'))
    model.add(Dense(output_dim=1))
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

    # plt.plot(history.history['loss'])
    # plt.plot(history.history['val_loss'])
    print(model.get_weights()[0].shape)

    sns.heatmap(model.get_weights()[0])

    plt.show()
