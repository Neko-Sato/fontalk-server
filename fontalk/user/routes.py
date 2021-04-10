from flask import request, make_response
from . import app
from . import firebase
from . import path
from . import processes
from . import functions
import json

@app.route(path + "/create", methods=["POST"])
@firebase.jwt_required
def user_create():
  data = json.loads(request.data.decode('utf-8'))
  response = make_response()
  response.data = json.dumps(\
    processes.create(\
      firebase_id=request.jwt_payload["user_id"], \
      **functions.dict_molding(data, {\
        'user_id': (False, ['str', 'NoneType']), \
        'name': (False, ['str', 'NoneType']), \
        'image': (False, ['bytes', 'NoneType']), \
      })\
    )\
  )
  response.mimetype = 'application/json'
  return response

@app.route(path +"/update", methods=["POST"])
@firebase.jwt_required
def user_update():
  data = json.loads(request.data.decode('utf-8'))
  response = make_response()
  response.data = json.dumps(\
    processes.update(\
      firebase_id=request.jwt_payload["user_id"], \
      **functions.dict_molding(data, {\
        'user_id': (False, ['str', 'NoneType']), \
        'name': (False, ['str', 'NoneType']), \
        'image': (False, ['bytes', 'NoneType']), \
      })\
    )\
  )
  response.mimetype = 'application/json'
  return response

@app.route(path +"/follow", methods=["POST"])
@firebase.jwt_required
def user_follow():
  data = json.loads(request.data.decode('utf-8'))
  response = make_response()
  response.data = json.dumps(\
    processes.follow(\
      firebase_id=request.jwt_payload["user_id"], \
      **functions.dict_molding(data, {\
        'follow_id': (True, ['str']), \
      })\
    )\
  )
  response.mimetype = 'application/json'
  return response

@app.route(path +"/unfollow", methods=["POST"])
@firebase.jwt_required
def user_unfollow():
  data = json.loads(request.data.decode('utf-8'))
  response = make_response()
  response.data = json.dumps(\
    processes.unfollow(\
      firebase_id=request.jwt_payload["user_id"], \
      **functions.dict_molding(data, {\
        'follow_id': (True, ['str']), \
      })\
    )\
  )
  response.mimetype = 'application/json'
  return response