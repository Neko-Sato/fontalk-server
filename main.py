from flask import Flask
import json
import pyrebase
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

with open("firebaseConfig.json") as f:
  config = json.loads(f.read())
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

import database
import route