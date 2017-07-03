#!/usr/bin/env python
# -*- coding: utf-8 -*-
import keras.backend as K
from keras.models import Model
from keras.utils import plot_model
from keras.layers import InputLayer
from keras import regularizers
from keras.layers.core import Flatten, Dense, Dropout
from keras.layers import Input
from keras.layers import Reshape
from keras.layers import Activation
from keras.layers.advanced_activations import LeakyReLU
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import Conv2DTranspose
from keras.layers.local import LocallyConnected2D
from keras.layers.convolutional import MaxPooling2D
from keras.layers.convolutional import ZeroPadding2D
from keras.layers.convolutional import UpSampling2D
from keras.layers.local import LocallyConnected1D


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
    def __init__(self, batch_input_shape, class_num):
        """TODO: to be defined1. """
        inputs = InputLayer(batch_input_shape=batch_input_shape).output
        hidden = LocallyConnected2D(1,
                                    kernel_size=(3, 1),
                                    activation='linear',
                                    activity_regularizer=regularizers.l2(0.01))(inputs)
        hidden = Flatten()(hidden)
        hidden = Dense(units=11)(hidden)
        hidden = LeakyReLU(alpha=0.3)(hidden)
        hidden = Dense(units=11)(hidden)
        hidden = LeakyReLU(alpha=0.3)(hidden)
        hidden = Dense(units=11)(hidden)
        hidden = LeakyReLU(alpha=0.3)(hidden)
        outputs = Dense(units=class_num, activation='linear')(hidden)
        super().__init__(inputs=[inputs], outputs=outputs)
