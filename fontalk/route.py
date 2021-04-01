from flask import request, make_response
from . import app
from . import firebase
from . import path
from . import processes
import json

@app.route(path + "/", methods=["POST"])
@firebase.jwt_required
def index():
  print(request.data)
  response = make_response()
  response.data = json.dumps({})#test.test(request.jwt_payload["user_id"]))
  response.mimetype = 'application/json'
  return response

##About Talk
#@app.route("/talk/get_list", methods=["POST"])
#@firebase.jwt_required
#def talks_get_list():
#  response = make_response()
#  response.data = json.dumps(talk.get_list(request.jwt_payload["user_id"]))
#  response.mimetype = 'application/json'
#  return response
#
##About User
#@app.route("/user/create", methods=["POST"])
#@firebase.jwt_required
#def user_create():
#  user_id = request.jwt_payload["user_id"]
#  data = json.loads(request.data.decode('utf-8'))
#   
#  response = make_response()
#  response.data = json.dumps(user.create(\
#    id=user_id, \
#    **data, \
#  )
#  response.mimetype = 'application/json'
#  return response
#
#@app.route("/user/change", methods=["POST"])
#@firebase.jwt_required
#def user_change():
#  user_id = request.jwt_payload["user_id"]
#  data = json.loads(request.data.decode('utf-8'))
#  response = make_response()
#  response.data = json.dumps(user.change(\
#    user_id=user_id, \
#    name=data.get('name', no_data), \
#    image=data.get('image', no_data), \
#  ))
#  response.mimetype = 'application/json'
#  return response