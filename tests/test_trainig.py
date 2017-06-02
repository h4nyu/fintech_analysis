import pytest
from fintech_analysis import Reader
from .test_load_model import datasets
from keras.callbacks import EarlyStopping
import keras


@pytest.fixture
def model():
    from fintech_analysis.models import FeatureExtractModel
    batch_input_shape = (None, 13)
    m = FeatureExtractModel(batch_input_shape, 1)
    m.summary()
    return m


def test_training(model, datasets):
    x_train, y_train = datasets
    model.compile(loss=keras.losses.mean_squared_error,
                  optimizer=keras.optimizers.Adadelta(),
                  metrics=['mse']
                  )
    model.fit(x_train,
              y_train,
              batch_size=10,
              epochs=1000,
              verbose=1,
              validation_split=0.3,
              callbacks=[EarlyStopping()]
              )
