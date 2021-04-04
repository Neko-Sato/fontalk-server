from flask import make_response
from . import app
import json

class TestErorr(Exception):
  def __init__(self, message):
    super().__init__()
    self.message = message

@app.errorhandler(TestErorr)
def handle_invalid_usage(error):
  response = make_response()
  response.data = json.dumps({'message': error.message})
  response.mimetype = 'application/json'
  return response