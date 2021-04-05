from flask import request, make_response
from . import app
from . import firebase
from . import path
from . import processes
from . import dict_molding
import json

@app.route(path + "/create", methods=["POST"])
@firebase.jwt_required
def create():
  data = dict_molding(json.loads(request.data.decode('utf-8')), {\
    'name' : (True, ['str', 'NoneType']), 
    'image' : (False, ['bytes', 'NoneType']),
  })
  response = make_response()
  response.data = json.dumps(\
    processes.create(\
      user_id=request.jwt_payload["user_id"], \
      name=data['name'], \
      image=data['image'], \
    )\
  )
  response.mimetype = 'application/json'
  return response

@app.route(path +"/update", methods=["POST"])
@firebase.jwt_required
def update():
  data = dict_molding(json.loads(request.data.decode('utf-8')), {\
    'name' : (False, ['str', 'NoneType']), 
    'image' : (False, ['bytes', 'NoneType']),
  })
  response = make_response()
  response.data = json.dumps(\
    processes.update(\
      request.jwt_payload["user_id"], \
      name=data['name'], \
      image=data['image'], \
    )\
  )
  response.mimetype = 'application/json'
  return response