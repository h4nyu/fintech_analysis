#!/usr/bin/env python
# s-*- coding: utf-8 -*-
from fintech_analysis.models import FeatureExtractModel
import keras
#  import matplotlib.pyplot as plt
from keras.callbacks import EarlyStopping
from fintech_analysis import Reader
import numpy as np

if __name__ == "__main__":
    r = Reader()
    files = ['./dataset/newfactor/21.csv']
    r.set_files(files)
    x_train, y_train = r.read(input_cols=range(2, 15),
                              output_cols=[1],
                              )

    x_train = x_train.reshape(-1, x_train.shape[1], 1)
    print(x_train.shape)
    print(y_train.shape)

    model = FeatureExtractModel(batch_input_shape=(None, x_train.shape[1], 1),
                                class_num=y_train.shape[1])
    model.summary()

    model.compile(loss=keras.losses.mean_squared_error,
                  optimizer=keras.optimizers.Adadelta(),
                  metrics=['mse'])
    model.fit(x_train, y_train,
              batch_size=32,
              epochs=9,
              shuffle=True,
              verbose=1,
              validation_split=0.3,
              callbacks=[EarlyStopping(patience=3)]
              )

    num = 1
    layer_index = 1
    result = model.get_layer_output([x_train[num:num+1]], layer_index)[0]
    print(result.shape)
    print(x_train[num])
    print(y_train[num])
    # sns.heatmap(np.abs(result[0]), annot=True, cbar=False)
    # plt.show()

    result = model.predict([x_train[num:num+1]])[0]
    print(result)
    # plt.show()
