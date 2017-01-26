#!/usr/bin/env python2

from keras.models import Sequential
from keras.layers import Dense, Activation
import pandas as pd
import numpy as np

if __name__ == '__main__':

    x_train = np.empty((0, 7))
    y_train = np.empty((0, 1))
    for i in range(3):
        df = pd.read_csv("~/fintech_tutorial/data/{0}.tsv".format(i),
                         delimiter="\t")
        x_train = np.append(x_train, np.array(df.ix[0:, 2:]), axis=0)
        y_train = np.append(y_train, np.array(df.ix[0:, 1]).reshape(len(df), 1), axis=0)

    print(x_train.shape)
    print(y_train.shape)
    print(x_train[0])
    print(y_train[0])

    model = Sequential()
    model.add(Dense(output_dim=3, input_dim=7))
    model.add(Activation('relu'))
    model.add(Dense(output_dim=3, input_dim=3))
    model.add(Activation('relu'))
    model.add(Dense(output_dim=1))
    model.add(Activation('relu'))

    model.compile(loss="mse", optimizer='rmsprop', metrics=['accuracy'])
    model.fit(x_train, y_train, nb_epoch=200, batch_size=1, validation_split=0.1)
    print model.predict(x_train[0].reshape(1,7))
