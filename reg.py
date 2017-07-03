#!/usr/bin/env python
# s-*- coding: utf-8 -*-
from fintech_analysis.models import FeatureExtractRegressionModel
import keras
#  import matplotlib.pyplot as plt
from keras.callbacks import EarlyStopping
from fintech_analysis import Reader

if __name__ == "__main__":
    r = Reader()
    for i in range(765):
        files = ['./dataset/daily/{}.csv'.format(i)]
        r.set_files(files)
        x_train, y_train = r.read(input_cols=range(2, 13),
                                  output_cols=[1],
                                  )
        x_train, y_train = r.get_time_window_dataset(step=10)
        print(x_train.shape, y_train.shape)
        x_train = x_train.reshape(-1, x_train.shape[1], x_train.shape[2], 1)
        model = FeatureExtractRegressionModel(batch_input_shape=(None, x_train.shape[1], x_train.shape[2], 1),
                                    class_num=y_train.shape[1])
        model.summary()

        model.compile(loss=keras.losses.mean_squared_error,
                      optimizer=keras.optimizers.RMSprop(),
                      metrics=['mse'])
        model.fit(x_train, y_train,
                  batch_size=16,
                  epochs=200,
                  verbose=0,
                  validation_split=0.3,
                  callbacks=[EarlyStopping(patience=3)]
                  )
        model.save_weights("reg_w{}.h5".format(i))

        start_index = 0
        end_index = len(y_train)
        layer_index = 1
        result = model.get_layer_output([x_train[start_index:end_index + 1]],
                                        layer_index)[0]
        print(result.shape)
        answers = y_train[start_index:end_index + 1]

        metrics = model.evaluate(x_train, y_train, batch_size=32, verbose=1)

        #  Returns the loss value & metrics values for the model in test mode
        print(metrics)
        # sns.heatmap(np.abs(result[0]), annot=True, cbar=False)
        # plt.show()

        predicts = model.predict(x_train[start_index:end_index + 1])
        #  for a, p in zip(answers, predicts):
        #      print(a, p)
        # plt.show()
