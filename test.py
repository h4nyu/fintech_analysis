#!/usr/bin/env python
# -*- coding: utf-8 -*-


class User(object):

    """Docstring for User. """

    def __init__(self, user, password):
        """TODO: to be defined1.

        :user: TODO
        :password: TODO

        """
        self.user = user
        self.password = password


class Waveform(object):

    """Docstring for Waveform. """

    def __init__(self, data):
        """TODO: to be defined1. """
        self.value = data
        self.timestamp = data

    def get_json(self):
        pass

if __name__ == "__main__":

    waveforms = []
    for i in range(10):
        waveforms.append(Waveform([i] * 10))
    waveforms = list(map(lambda x: x.__dict__, waveforms))
    print(waveforms)
