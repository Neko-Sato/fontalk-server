from flask import request, make_response
from . import app
from . import firebase
from . import path
from . import processes
import json

@app.route(path + "/create", methods=["POST"])
@firebase.jwt_required
def create():
  user_id = request.jwt_payload["user_id"]
  data = json.loads(request.data.decode('utf-8'))
  response = make_response()
  response.data = json.dumps(processes.create(\
    id=user_id, \
    **data, \
  ))
  response.mimetype = 'application/json'
  return response

@app.route(path +"/update", methods=["POST"])
@firebase.jwt_required
def update():
  user_id = request.jwt_payload["user_id"]
  data = json.loads(request.data.decode('utf-8'))
  response = make_response()
  response.data = json.dumps(user.update(\
    user_id=user_id, \
    **data
  ))
  response.mimetype = 'application/json'
  return response