from flask import request, session, jsonify, redirect, url_for
from main import app, firebase, database
import json

@app.route("/", methods=["POST"])
@firebase.jwt_required
def hello_world():
  print(request.__dict__)
  return "Hello, World!"

@app.errorhandler(Exception)
def error_except(e):
  temp = {\
    "error": {
      "message": e.description, \
    }, \
  }
  return jsonify(temp)