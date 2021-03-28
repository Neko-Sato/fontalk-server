from flask import request, make_response
from main import app, firebase
from application import *
import json

@app.route("/", methods=["POST"])
@firebase.jwt_required
def index():
  print(request.data)
  response = make_response()
  response.data = json.dumps(test.test(request.jwt_payload["user_id"]))
  response.mimetype = 'application/json'
  return response

#About Talks
@app.route("/talks/get_list", methods=["POST"])
@firebase.jwt_required
def talks_get_list():
  response = make_response()
  response.data = json.dumps(talks.get_list(request.jwt_payload["user_id"]))
  response.mimetype = 'application/json'
  return response

#About User
@app.route("/user/create", methods=["POST"])
@firebase.jwt_required
def user_create():
  response = make_response()
  response.data = user.create(**json.loads(request.data.decode('utf-8')))
  response.mimetype = 'application/json'
  return response