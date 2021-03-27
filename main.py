from flask import Flask
from flask_firebase_admin import FirebaseAdmin
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["FIREBASE_ADMIN_CREDENTIAL"] = \
  FirebaseAdmin.credentials.Certificate("serviceAccountKey.json")
app.config['SQLALCHEMY_DATABASE_URI'] = \
  'sqlite:///database.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = \
  False

firebase = FirebaseAdmin(app)
db = SQLAlchemy(app)

import route