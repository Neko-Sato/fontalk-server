from flask import request, make_response
from . import app
from . import firebase
from . import path
from . import processes
import json

@app.route(path + "/", methods=["POST"])
@firebase.jwt_required
def index():
  user_id = request.jwt_payload["user_id"]
  response = make_response()
  response.data = json.dumps(processes.test(user_id))
  response.mimetype = 'application/json'
  return response

@app.route(path + "/erorr", methods=["POST"])
@firebase.jwt_required
def erorr():
  processes.erorr()