#!/usr/bin/env python

from fintech_analysis import WeightVeiwer
from fintech_analysis.models import FeatureExtractRegressionModel

if __name__ == '__main__':
    model = FeatureExtractRegressionModel(batch_input_shape=(None, 1, 11, 1),
                                          out_dim=1, kernel_size=(1, 1))
    model.load_weights("/home/yao/fintech_tutorial/reg_w0.h5")
    model.summary()
    w = WeightVeiwer(model)
    w.set_col_names(['sharpe', 'alpha', 'beta', 'sortino', 'treynor',
                     'volo', 'stockrec', 'maxy'])
    w.show_pn_bar()
