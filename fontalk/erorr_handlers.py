from flask import make_response
from werkzeug.exceptions import HTTPException
from .fontalk import app
import json

class InvalidUsage(Exception):
  status_code = 400
  def __init__(self, message, status_code=None, payload=None):
    super().__init__(self)
    self.message = message
    if status_code is not None:
      self.status_code = status_code
    self.payload = payload

  def to_dict(self):
    rv = dict(self.payload or ())
    rv['message'] = self.message
    return rv

@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
  response = make_response()
  response.data = json.dumps(error.to_dict())
  response.status_code = error.status_code
  response.mimetype = 'application/json'
  return response

@app.errorhandler(HTTPException)
def handle_exception(e):
  response = make_response()
  response.data = json.dumps({
    "code": e.code,
    "name": e.name,
    "description": e.description,
  })
  response.content_type = "application/json"
  return response