from . import app
from flask_firebase_admin import FirebaseAdmin
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app.config["FIREBASE_ADMIN_CREDENTIAL"] = \
  FirebaseAdmin.credentials.Certificate("serviceAccountKey.json")
app.config['SQLALCHEMY_DATABASE_URI'] = \
  'sqlite:///../database.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = \
  False

CORS(app)
firebase = FirebaseAdmin(app)
db = SQLAlchemy(app)