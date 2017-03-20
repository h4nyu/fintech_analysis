#!/usr/bin/env python
# -*- coding: utf-8 -*-
from modules import NeuralNet
from modules import WeightVeiwer
from modules import Reader

if __name__ == "__main__":

    # read training dataset

    file_path_list = []
    for i in range(0, 3):
        file_path_list.append(
            '~/fintech_tutorial/dataset/datajf101/{0}.csv'.format(i))

    x_start_col = 2
    x_end_col = 11
    y_start_col = 1
    y_end_col = 1

    reader = Reader()
    reader.set_paths(file_path_list)
    (x_train, y_train) = reader.read(x_start_col,
                                     x_end_col,
                                     y_start_col,
                                     y_end_col)
    y_train = reader.change_to_one_hot(y_train)
    x_train = reader.normalize(x_train)

    # (x_train, y_train) = reader.get_time_window_dataset()

    # set model
    neuralnet = NeuralNet()
    neuralnet.set_dataset(x_train=x_train, y_train=y_train)
    neuralnet.build_model(layer_num=4, l1=0.5)

    # train
    neuralnet.fit(batch_size=3)
    neuralnet.show_graph()

    # save model
    neuralnet.save("model.h5")

    # read validation dataset
    reader.set_paths(["~/fintech_tutorial/dataset/datajf101/3.csv"])
    (x_train, y_train) = reader.read(x_start_col,
                                     x_end_col,
                                     y_start_col,
                                     y_end_col)

    # validation
    y_train = reader.change_to_one_hot(y_train)
    neuralnet.validate_category(x_train, y_train)

    # veiw weights
    w = WeightVeiwer("model.h5")
    w.set_col_names(['sharpe', 'alpha', 'beta', 'sortino', 'treynor', 'volo', 'stockrec', 'maxy', 'mktrelated', 'mktvol'])
    w.show_abs_bar()
    w.show_sum_bar()
    w.show_pn_bar()
