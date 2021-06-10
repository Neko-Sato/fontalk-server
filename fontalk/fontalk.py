from flask import Flask
from flask_firebase_admin import FirebaseAdmin
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from .config import config

app = Flask('fontalk')
config(app)
CORS(app)
firebase = FirebaseAdmin(app)
db = SQLAlchemy(app)