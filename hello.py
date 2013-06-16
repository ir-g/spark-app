import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'The index page...'
    
@app.route('/querytest/<query>')
def hello(query):
    return 'Query %s' % query
