from flask import make_response
import json

def handle_invalid_usage(error):
  response = make_response()
  response.data = json.dumps(error.to_dict())
  response.status_code = error.status_code
  response.mimetype = 'application/json'
  return response

def handle_exception(e):
  response = make_response()
  response.data = json.dumps({
    'message': e.name,
  })
  response.content_type = "application/json"
  return response