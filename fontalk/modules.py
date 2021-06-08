from flask import Flask
from flask_firebase_admin import FirebaseAdmin
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

def FirebaseAdmin_new_make_401(self, message):
  print(message)
  raise Exception

FirebaseAdmin.make_401 = FirebaseAdmin_new_make_401
