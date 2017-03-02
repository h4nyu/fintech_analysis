#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np


def get_sum_of_squares_error(predicts, answers):
    sum_of_squares_error = 0.0
    for pred, ans in zip(predicts, answers):
        sum_of_squares_error = sum_of_squares_error + (pred - ans) ** 2

    return sum_of_squares_error / 2.0


if __name__ == "__main__":
    sample_size = 4
    answers = [np.sin(i) for i in range(sample_size)]
    noise = np.random.rand(sample_size)
    noise_weight = 4
    predicts = [a + noise_weight * n for a, n in zip(answers, noise)]

    sse = get_sum_of_squares_error(predicts, answers)
    print(sse)
