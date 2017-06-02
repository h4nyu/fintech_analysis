#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
from fintech_analysis import Reader


@pytest.fixture(scope='module')
def reader():
    return Reader()


@pytest.fixture
def reader_with_files(reader):
    reader.set_dir("dataset/newfactor")
    return reader


@pytest.fixture(scope='module')
def datasets():
    r = Reader()
    r.set_dir("dataset/newfactor")
    x_train, y_train = r.read(input_cols=range(2, 15), output_cols=[1])
    return x_train, y_train



def test_reader_set_dir(reader):
    file_names = reader.set_dir("dataset/newfactor")
    assert len(file_names) == 525


def test_reader_read(datasets):
    x_train, y_train = datasets
    assert x_train.shape[1] == 13
    assert y_train.shape[1] == 1

