from flask import request, make_response
from . import app
from . import firebase
from . import path
from . import dict_molding
from . import processes
import json

@app.route(path + "/create", methods=["POST"])
@firebase.jwt_required
def create():
  data = json.loads(request.data.decode('utf-8'))
  data = dict_molding(data, {\
    'name' : (True, ['str', 'NoneType']), 
    'image' : (False, ['bytes', 'NoneType']),
  })
  response = make_response()
  response.data = json.dumps(\
    processes.create(\
      user_id = request.jwt_payload["user_id"], \
      **data, \
    )\
  )
  response.mimetype = 'application/json'
  return response

@app.route(path +"/update", methods=["POST"])
@firebase.jwt_required
def update():
  data = json.loads(request.data.decode('utf-8'))
  data = dict_molding(data, {\
    'name' : (False, ['str', 'NoneType']), 
    'image' : (False, ['bytes', 'NoneType']),
  })
  response = make_response()
  response.data = json.dumps(\
    processes.create(\
      user_id = request.jwt_payload["user_id"], \
      **data, \
    )\
  )
  response.mimetype = 'application/json'
  return response