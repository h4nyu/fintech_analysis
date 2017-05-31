#!/usr/bin/env python
# -*- coding: utf-8 -*-
import keras.backend as K
from .layers import OscaInput
from .layers import Grad
from .layers import ClipLeft
from .layers import ClipRight
from .layers import GreaterFirst
from keras.models import Model
from keras.utils import plot_model


class KerasModel(Model):
    def __init__(self, inputs, outputs, name=None):
        super().__init__(inputs, outputs, name=None)

    def plot_model(self):
        filepath = 'model.png'
        plot_model(self,
                   to_file=filepath,
                   show_shapes=True)

    def get_layer_output(self, x_predict, layer_num):
        output_func = K.function(
            self.inputs, [self.layers[layer_num].output])
        return output_func(x_predict)


class SplitModel(KerasModel):
    def __init__(self):
        """TODO: to be defined1. """

        id = OscaInput().output
        start = OscaInput().output
        end = OscaInput().output

        start_diff = Grad()(start)
        start_point = GreaterFirst(0)(start_diff)

        id_left = ClipLeft()([id, start_point])
        end_left = ClipLeft()([end, start_point])

        end_diff = Grad()(end_left)
        end_point = GreaterFirst(0)(end_diff)
        cliped = ClipRight()([id_left, end_point])

        super().__init__(inputs=[id, start, end], outputs=cliped)
