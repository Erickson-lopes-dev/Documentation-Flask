from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Olá, Mundo'


@app.route('/hello')
def hello():
    return 'Hello'
