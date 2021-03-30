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
  user_id = request.jwt_payload["user_id"]
  data = json.loads(request.data.decode('utf-8'))
  response = make_response()
  response.data = json.dumps(user.create(\
    user_id=user_id, \
    name=data.get('name', user_id), \
    image=data.get('image', None), \
  ))
  response.mimetype = 'application/json'
  return response

@app.route("/user/change", methods=["POST"])
@firebase.jwt_required
def user_change():
  user_id = request.jwt_payload["user_id"]
  data = json.loads(request.data.decode('utf-8'))
  response = make_response()
  response.data = json.dumps(user.change(\
    user_id=user_id, \
    name=data.get('name', no_data), \
    image=data.get('image', no_data), \
  ))
  response.mimetype = 'application/json'
  return response