#!/usr/bin/env python
# -*- coding: utf-8 -*-
import keras.backend as K
from keras.models import Model
from keras.utils import plot_model
from keras.layers import InputLayer


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


class FeatureExtractModel(KerasModel):
    def __init__(self, batch_input_shape):
        """TODO: to be defined1. """
        inputs = InputLayer(batch_input_shape=batch_input_shape).output

        super().__init__(inputs=[inputs], outputs=inputs)
