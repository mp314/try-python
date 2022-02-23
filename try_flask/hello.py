#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
$ export FLASK_APP=hello.py
$ set FLASK_APP = hello.py
$ export FLASK_ENV=development
$ set FLASK_DEBUG = True
$ flask run
'''

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    '''Return Hello, World!'''
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
