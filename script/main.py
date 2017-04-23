#!/usr/bin/env python
# -*- coding: utf-8 -*-
from modules import WeightsVeiwer
from modules import Analyzer

if __name__ == "__main__":

    # read training dataset
    file_paths = []
    for i in range(0, 28):
        file_paths.append(
            '~/fintech_tutorial/dataset/datazq8/{0}.csv'.format(i))
    a = Analyzer()
    a.csv_file_config(x_start_col=2,
                      x_end_col=9,
                      y_start_col=1,
                      y_end_col=1
                      )
    # a.grid_search(file_paths=file_paths,
    #               epochs=20,
    #               layer_nums=[4, 5],
    #               lassos=[0.01, 0.001],
    #               batch_sizes=[5, 10]
    #               )
    a.training(num=10,
               threshold=0.8,
               batch_size=5,
               init_weight=0,
               file_paths=file_paths,
               lasso=0.01,
               layer_num=4
               )

    w = WeightsVeiwer(a.model_paths)
    w.show_heatmap()
    w.set_col_names(['sharpe', 'alpha', 'beta', 'sortino', 'treynor',
                     'volo', 'stockrec', 'maxy'])
    w.show_abs_bar()
    w.show_pn_bar()
