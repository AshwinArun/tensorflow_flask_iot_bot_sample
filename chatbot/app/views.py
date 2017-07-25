# views.py

from flask import render_template
from flask_socketio import SocketIO, send
from bot import bot_response
from app import app

socketio = SocketIO(app)
@socketio.on('message')
def handleMessage(msg):
    if msg == 'user_connected':
        send('Hi. How can I help?', broadcast=False)
    else:
        send (bot_response.response(msg))
        
    

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

