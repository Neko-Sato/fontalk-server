from flask import Flask
app = Flask('fontalk')

from flask_firebase_admin import FirebaseAdmin
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app.config["FIREBASE_ADMIN_CREDENTIAL"] = \
  FirebaseAdmin.credentials.Certificate("serviceAccountKey.json")

#app.config['SQLALCHEMY_DATABASE_URI'] = \
#  'sqlite:///../database.sqlite3'
app.config['SQLALCHEMY_DATABASE_URI'] = \
  'mysql+pymysql://{user}:{password}@{host}/{db_name}?charset=utf8'.format(
    user='root', \
    password='fontalk@pass!350350', \
    host='localhost', \
    db_name='fontalk_database', \
  )
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = \
  False

CORS(app)
firebase = FirebaseAdmin(app)
db = SQLAlchemy(app)