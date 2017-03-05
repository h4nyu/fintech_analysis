#!/usr/bin/env python
# -*- coding: utf-8 -*-
from modules import NeuralNet
from modules import WeightVeiwer
from modules import Reader

if __name__ == "__main__":

    # read training dataset

    file_path_list = []
    for i in range(8):
        file_path_list.append(
            '~/fintech_tutorial/dataset/datadstz8/{0}.csv'.format(i))

    x_start_col = 2
    x_end_col = 9
    y_start_col = 1
    y_end_col = 1

    reader = Reader()
    reader.set_paths(file_path_list)
    (x_train, y_train) = reader.read(x_start_col,
                                     x_end_col,
                                     y_start_col,
                                     y_end_col)

    # (x_train, y_train) = reader.get_time_window_dataset()

    # set model
    neuralnet = NeuralNet()
    neuralnet.set_dataset(x_train=x_train, y_train=y_train)
    neuralnet.build_model(layer_num=3, l1=0.02)

    # train
    neuralnet.fit(batch_size=5)
    neuralnet.show_graph()

    # save model
    neuralnet.save("model.h5")

    # read validation dataset
    reader.set_paths(["~/fintech_tutorial/dataset/datadstz8/8.csv"])
    (x_train, y_train) = reader.read(x_start_col,
                                     x_end_col,
                                     y_start_col,
                                     y_end_col)

    # validation
    neuralnet.validate(x_train, y_train)

    # veiw weights
    w = WeightVeiwer("model.h5")
    w.show_heatmap()
    w.show_bar()
