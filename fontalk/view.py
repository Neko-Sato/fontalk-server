from . import app
from flask import request, make_response
import json

class general_view:
  app = app
  @classmethod
  def endpoint(cls):
    instance = cls()
    endpoint = str(id(instance))
    cls.app.view_functions[endpoint] = instance.as_view
    return endpoint
  def as_view(self, *args, **kwargs):
    try:
      data = json.loads(request.get_data().decode('utf-8'))
    except json.decoder.JSONDecodeError:
      data = {}
    response = make_response()
    result = self.view(data, *args, **kwargs)
    response.data = json.dumps({'message': result[0], 'data': result[1]})
    response.mimetype = 'application/json'
    print(response.data)
    return response
  def view(self, data, *args, **kwargs):
    return {'massage': 'massage', 'data': 'data'}

from . import firebase
class firebase_view(general_view):
  @firebase.jwt_required
  def as_view(self, *args, **kwargs):
      kwargs['firebase_id'] = request.jwt_payload["user_id"]
      return super().as_view(*args, **kwargs)
  def view(self, data, firebase_id, *args, **kwargs):
      return super().view(data, *args, **kwargs)