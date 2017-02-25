#!/usr/bin/env python
# -*- coding: utf-8 -*-
from neuralnet import NeuralNet
from helper import WeightVeiwer
from helper import Reader

if __name__ == "__main__":

    # read training dataset
    file_path_list = []
    for i in range(4):
        file_path_list.append(
            "~/fintech_tutorial/dataset/data0/{0}.tsv".format(i))
    for i in range(5):
        file_path_list.append(
            "~/fintech_tutorial/dataset/data1/{0}.tsv".format(i))
    for i in range(1):
        file_path_list.append(
            "~/fintech_tutorial/dataset/data2/{0}.tsv".format(i))

    reader = Reader()
    reader.set_path(file_path_list)
    reader.read(x_start_col=2,
                x_end_col=8,
                y_start_col=1,
                y_end_col=1)

    (x_train, y_train) = reader.get_time_window_dataset()

    # set model
    neuralnet = NeuralNet()
    neuralnet.set_dataset(x_train=x_train, y_train=y_train)
    neuralnet.build_model(5)

    # train
    neuralnet.fit()
    neuralnet.show_graph()

    # save model
    neuralnet.save("model.h5")

    # read validation dataset
    reader.set_path(["~/fintech_tutorial/dataset/data2/1.tsv"])
    (x_train, y_train) = reader.read(x_start_col=2,
                                     x_end_col=8,
                                     y_start_col=1,
                                     y_end_col=1)

    (x_train, y_train) = reader.get_time_window_dataset()

    # validation
    neuralnet.validate(x_train, y_train)

    # veiw weights
    w = WeightVeiwer("model.h5")
    w.show_heatmap()
    w.show_bar()
    w.show_times(4, 7)
    w.sum_times()
