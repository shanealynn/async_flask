"""
Demo Flask application to test the operation of Flask with socket.io

Aim is to create a webpage that is constantly updated with random numbers from a background python process.

30th May 2014
"""

# Start with a basic flask app webpage.

from flask import Flask, render_template
#from flask.ext.socketio import SocketIO, emit

__author__ = 'slynn'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True


@app.route('/')
def index():
    return "Flask app isd up and running right now!"


if __name__ == '__main__':
    app.run()