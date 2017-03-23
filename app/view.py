from app import app
from flask import render_template
from app.utility import list_to_json


class User(object):

    """Docstring for User. """

    def __init__(self, user, password):
        """TODO: to be defined1.

        :user: TODO
        :password: TODO

        """
        self.name = user
        self.password = password


class Waveform(object):

    """Docstring for Waveform. """

    def __init__(self, data):
        """TODO: to be defined1. """
        self.value = data
        self.timestamp = data

    def get_json(self):
        pass


@app.route('/')
@app.route('/index')
def index():
    title = 'my_title'
    waveforms = []
    for i in range(100):
        waveforms.append(Waveform([i] * 10).__dict__)
    return render_template('index.html',
                           title=title,
                           waveforms=waveforms
                           )
