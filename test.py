#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json


class User(object):

    """Docstring for User. """

    def __init__(self, user, password):
        """TODO: to be defined1.

        :user: TODO
        :password: TODO

        """
        self.user = user
        self.password = password


if __name__ == "__main__":

    users = []
    users.append(User('aaa', 'bbb'))
    users.append(User('ccc', 'ddd'))
    users = list(map(lambda x: x.__dict__, users))
    print(users)
