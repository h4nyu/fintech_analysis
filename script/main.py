#!/usr/bin/env python
# -*- coding: utf-8 -*-
from neuralnet import NeuralNet
from helper import DatasetGenerator


def liner(factors):
    return [factors[0] * factors[2]]


if __name__ == "__main__":
    neuralnet = NeuralNet()

    generator = DatasetGenerator(10)
    (x_train, y_train) = generator.generate(liner, 100)

    neuralnet.set_dataset(x_train=x_train, y_train=y_train)
    neuralnet.build_model(3)
    neuralnet.fit()
    neuralnet.show_graph()
    neuralnet.save("model.h5")
