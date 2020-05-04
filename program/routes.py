from program import app
import socket
from flask import render_template
@app.route('/')
@app.route('/index')


def index():
  return render_template('index.html')
@app.route("/aboutme")

def aboutme():
   return render_template('aboutme.html')

@app.route('/studies')
def studies():
   return render_template('studies.html')

@app.route('/ip')

def ip():
   return socket.gethostbyaddr(socket.gethostname())[0]
