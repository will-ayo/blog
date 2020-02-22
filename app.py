import os
os.environ['FLASK_APP'] = "app.py"
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World !'