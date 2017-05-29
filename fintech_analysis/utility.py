#!/usr/bin/env python
# -*- coding: utf-8 -*-


def object_to_json(arg):
    """TODO: Docstring for object_to_json.

    :arg: TODO
    :returns: TODO

    """
    return arg.__dict__


def list_to_json(args):
    """TODO: Docstring for object_to_json.

    :arg: TODO
    :returns: TODO

    """
    return [i.__dict__ for i in args]
