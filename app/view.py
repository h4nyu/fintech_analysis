from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    arg0 = 'aaaa'
    arg1 = {'subarg0': 'bbbb'}
    return render_template('index.html',
                           arg0=arg0,
                           arg1=arg1
                           )
