#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
from fintech_analysis import Reader


@pytest.fixture
def reader():
    return Reader()


@pytest.fixture
def reader_with_files(reader):
    reader.set_dir("dataset/newfactor")
    return reader


def test_load_model():
    from fintech_analysis.models import FeatureExtractModel
    batch_input_shape = (None, 10)
    m = FeatureExtractModel(batch_input_shape)
    m.summary()


def test_reader_set_dir(reader):
    file_names = reader.set_dir("dataset/newfactor")
    assert len(file_names) == 525


def test_reader_read(reader_with_files):
    r = reader_with_files
    x_train, y_train = r.read(input_cols=range(2, 15), output_cols=[1])
    assert x_train.shape[1] == 13
    assert y_train.shape[1] == 1



