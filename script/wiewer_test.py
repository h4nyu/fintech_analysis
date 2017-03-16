#!/usr/bin/env python
# -*- coding: utf-8 -*-

from modules import WeightVeiwer

if __name__ == "__main__":
    w = WeightVeiwer("model.h5")
    w.show_dual_bar()
