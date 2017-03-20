#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pprint import pprint
import matplotlib.pyplot as plt
import numpy as np
from modules import DatasetGenerator
from modules import WeightVeiwer
from modules import NeuralNet


def model_with_relation(factors):
    return [np.sin(np.pi * 2 * (factors[0] + factors[3])) + 0.2 * np.random.rand()]


def model_with_no_relation(factors):
    return [np.random.rand()]


if __name__ == "__main__":

    g = DatasetGenerator(30)

    (x_train, y_train) = g.generate(model_with_relation, 10000)
    # (x_train, y_train) = g.generate(model_with_no_relation, 1000)

    neuralnet = NeuralNet()
    neuralnet.set_dataset(x_train=x_train, y_train=y_train)
    neuralnet.build_model(4, l1=0.04)
    neuralnet.fit(batch_size=100)
    neuralnet.save('reg_test.h5')

    w = WeightVeiwer("reg_test.h5")
    w.show_heatmap()
    w.show_bar()
