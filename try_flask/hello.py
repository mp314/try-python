from flask import Flask

'''
$ export FLASK_APP=hello.py
$ set FLASK_APP = hello.py
$ export FLASK_ENV=development
$ set FLASK_DEBUG = True
$ flask run
'''

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
   app.run()