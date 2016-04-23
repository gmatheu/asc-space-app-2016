from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    data = {'title': 'Hello World'}
    return render_template("index.html",
                           title='Home',
                           data=data)

