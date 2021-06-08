from flask import request, make_response
import json

def test():
  response = make_response()
  response.data = json.dumps({'massage': 'test'})
  response.mimetype = 'application/json'
  return response