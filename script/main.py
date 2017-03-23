#!/usr/bin/env python
# -*- coding: utf-8 -*-
from modules import WeightsVeiwer
from modules import Analyzer

if __name__ == "__main__":

    # read training dataset

    file_paths = []
    for i in range(0, 3):
        file_paths.append(
            '~/fintech_tutorial/dataset/datajf101/{0}.csv'.format(i))
    a = Analyzer()
    a.csv_file_config(x_start_col=2,
                      x_end_col=11,
                      y_start_col=1,
                      y_end_col=1
                      )
    a.training(num=50,
               threshold=0.9,
               file_paths=file_paths
               )

    a.validation(["~/fintech_tutorial/dataset/datajf101/3.csv"])

    w = WeightsVeiwer(a.model_paths)
    # w.show_heatmap()
    w.set_col_names(['sharpe', 'alpha', 'beta', 'sortino', 'treynor',
                     'volo', 'stockrec', 'maxy', 'mktrelated', 'mktvol'])
    w.show_abs_bar()
    w.show_sum_bar()
