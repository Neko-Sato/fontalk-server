from flask import Flask
from flask_firebase_admin import FirebaseAdmin
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from .exceptions import InvalidUsage
def FirebaseAdmin_new_make_401(self, message):
  raise InvalidUsage(message, status_code=401)
FirebaseAdmin.make_401 = FirebaseAdmin_new_make_401
del FirebaseAdmin_new_make_401, InvalidUsage
