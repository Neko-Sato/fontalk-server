from flask import request, make_response
from . import app
from . import firebase
from . import path
from . import processes
from . import functions
import json

@app.route(path + "/create", methods=["POST"])
@firebase.jwt_required
def talk_create():
  data = json.loads(request.data.decode('utf-8'))
  response = make_response()
  response.data = json.dumps(\
    processes.create(\
      firebase_id=request.jwt_payload["user_id"], \
      **functions.dict_molding(data, {\
        'name': (False, ['str', 'NoneType']), \
        'image': (False, ['bytes', 'NoneType']), \
        'users': (False, ['list', 'NoneType']), \
      })\
    )\
  )
  response.mimetype = 'application/json'
  return response

@app.route(path + "/update", methods=["POST"])
@firebase.jwt_required
def talk_update():
  data = json.loads(request.data.decode('utf-8'))
  response = make_response()
  response.data = json.dumps(\
    processes.update(\
      firebase_id=request.jwt_payload["user_id"], \
      **functions.dict_molding(data, {\
        'talk_id': (True, ['int']), \
        'name': (False, ['str', 'NoneType']), \
        'image': (False, ['bytes', 'NoneType']), \
      })\
    )\
  )
  response.mimetype = 'application/json'
  return response

@app.route(path + "/delete", methods=["POST"])
@firebase.jwt_required
def talk_delete():
  data = json.loads(request.data.decode('utf-8'))
  response = make_response()
  response.data = json.dumps(\
    processes.delete(\
      firebase_id=request.jwt_payload["user_id"], \
      **functions.dict_molding(data, {\
        'talk_id': (True, ['int']), \
      })\
    )\
  )
  response.mimetype = 'application/json'
  return response

@app.route(path + "/invitation", methods=["POST"])
@firebase.jwt_required
def talk_invitation():
  data = json.loads(request.data.decode('utf-8'))
  response = make_response()
  response.data = json.dumps(\
    processes.invitation(\
      firebase_id=request.jwt_payload["user_id"], \
      **functions.dict_molding(data, {\
        'talk_id': (True, ['int', 'NoneType']), \
        'users': (False, ['list', 'NoneType']), \
      })\
    )\
  )
  response.mimetype = 'application/json'
  return response

@app.route(path + "/participation", methods=["POST"])
@firebase.jwt_required
def talk_participation():
  data = json.loads(request.data.decode('utf-8'))
  response = make_response()
  response.data = json.dumps(\
    processes.participation(\
      firebase_id=request.jwt_payload["user_id"], \
      **functions.dict_molding(data, {\
        'talk_id': (True, ['int', 'NoneType']), \
      })\
    )\
  )
  response.mimetype = 'application/json'
  return response

@app.route(path + "/withdrawal", methods=["POST"])
@firebase.jwt_required
def talk_withdrawal():
  data = json.loads(request.data.decode('utf-8'))
  response = make_response()
  response.data = json.dumps(\
    processes.withdrawal(\
      firebase_id=request.jwt_payload["user_id"], \
      **functions.dict_molding(data, {\
        'talk_id': (True, ['int', 'NoneType']), \
        'users': (False, ['list', 'NoneType']), \
      })\
    )\
  )
  response.mimetype = 'application/json'
  return response

@app.route(path + "/get_member", methods=["POST"])
@firebase.jwt_required
def talk_get_member():
  data = json.loads(request.data.decode('utf-8'))
  response = make_response()
  response.data = json.dumps(\
    processes.get_member(\
      firebase_id=request.jwt_payload["user_id"], \
      **functions.dict_molding(data, {\
        'talk_id': (True, ['int', 'NoneType']), \
      })\
    )\
  )
  response.mimetype = 'application/json'
  return response

@app.route(path + "/get_talks", methods=["POST"])
@firebase.jwt_required
def talk_get_talks():
  data = json.loads(request.data.decode('utf-8'))
  response = make_response()
  response.data = json.dumps(\
    processes.get_talks(firebase_id=request.jwt_payload["user_id"])\
  )
  response.mimetype = 'application/json'
  return response