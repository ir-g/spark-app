import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    #return 'The index page...'
    return render_template('p/index.html', message="Index Page")
    
@app.route('/querytest/<query>')
def queryview(query):
    return 'Query %s' % query
    
@app.route('/gh/~<user>/<page>')
def viewghuser(user,page):
    return 'User %s' % user