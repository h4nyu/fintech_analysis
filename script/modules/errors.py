#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np


def get_sum_of_squares_error(predicts, answers):
    sum_of_squares_error = 0.0
    for pred, ans in zip(predicts, answers):
        sum_of_squares_error = sum_of_squares_error + (pred - ans) ** 2

    return sum_of_squares_error / 2.0


def get_rms_error(sse, sample_size):
    return np.sqrt(sse / float(sample_size))


def get_ms_error(sse, sample_size):
    return sse / float(sample_size)


if __name__ == "__main__":
    sample_size = 100
    answers = [np.sin(i) for i in range(sample_size)]
    noise = np.random.rand(sample_size)
    noise_weight = 1
    predicts = [a + noise_weight * n for a, n in zip(answers, noise)]

    sse = get_sum_of_squares_error(predicts, answers)
    rms = get_rms_error(sse, sample_size)
