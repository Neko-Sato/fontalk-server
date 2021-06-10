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
    data = json.loads(request.get_data().decode('utf-8'))
    response = make_response()
    response.data = json.dumps(self.view(data, *args, **kwargs))
    response.mimetype = 'application/json'
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