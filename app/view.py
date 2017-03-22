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


@app.route('/')
@app.route('/index')
def index():
    title = 'my_title'
    users = []
    users.append(User('aaa', 'bbb'))
    users.append(User('ccc', 'ddd'))
    return render_template('index.html',
                           title=title,
                           users=list_to_json(users)
                           )
