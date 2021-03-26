from flask import request, session, redirect, url_for
from main import app, firebase, database
import json

@app.route("/", methods=["POST"])
@firebase.jwt_required
def hello_world():
  print(request.__dict__)
  return "Hello, World!"