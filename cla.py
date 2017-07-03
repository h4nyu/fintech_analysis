#!/usr/bin/env python
# s-*- coding: utf-8 -*-
from fintech_analysis.models import FeatureExtractClassificationModel
import keras
#  import matplotlib.pyplot as plt
from keras.callbacks import EarlyStopping
from fintech_analysis import Reader

if __name__ == "__main__":
    r = Reader()
    files = ['./dataset/daily/3.csv']
    r.set_files(files)
    x_train, y_train = r.read(input_cols=range(2, 13),
                              output_cols=[1],
                              )
    x_train, y_train = r.get_time_window_dataset(step=10)
    y_train = r.change_to_one_hot(y_train)
    #
    x_train = x_train.reshape(-1, x_train.shape[1], x_train.shape[2], 1)
    print(x_train.shape)
    print(y_train.shape)

    model = FeatureExtractClassificationModel(batch_input_shape=(None, x_train.shape[1], x_train.shape[2], 1),
                                              class_num=y_train.shape[1])
    model.summary()

    model.compile(loss=keras.losses.categorical_crossentropy,
                  optimizer=keras.optimizers.RMSprop(),
                  metrics=['acc'])
    model.fit(x_train, y_train,
              batch_size=16,
              epochs=200,
              verbose=1,
              validation_split=0.3,
              callbacks=[EarlyStopping(patience=3)]
              )

    start_index = 0
    end_index = len(y_train)
    layer_index = 1
    result = model.get_layer_output([x_train[start_index:end_index + 1]],
                                    layer_index)[0]
    print(result.shape)
    answers = y_train[start_index:end_index + 1]

    predicts = model.predict(x_train[start_index:end_index + 1])

    metrics = model.evaluate(x_train, y_train, batch_size=32, verbose=1)

    #  Returns the loss value & metrics values for the model in test mode
    print(metrics)


    #  for a, p in zip(answers, predicts):
    #      print(a, p)
