from flask_cors import extension
from . import app
from flask import request, make_response
import json

class general_view:
  app = app
  @classmethod
  def endpoint(cls):
    view = cls.get_view()
    endpoint = str(id(view))
    cls.app.view_functions[endpoint] = view
    return endpoint
  @classmethod
  def get_view(cls, *args, **kwargs):
    return cls().as_view
  def as_view(self, *args, **kwargs):
    try:
      data = json.loads(request.get_data().decode('utf-8'))
    except json.decoder.JSONDecodeError:
      data = {}
    response = make_response()
    result = self.view(data, *args, **kwargs)
    response.data = json.dumps({'message': result[0], 'data': result[1]})
    response.mimetype = 'application/json'
    return response
  def view(self, data, *args, **kwargs):
    return 'massage', None

class error_viwe(general_view):
  exception=Exception
  def as_view(self, error, *args, **kwargs):
    response = make_response()
    result = self.view(error, *args, **kwargs)
    response.data = json.dumps({'message': result[0]})
    response.status_code = result[1]
    response.mimetype = 'application/json'
    return response
  def view(self, error, *args, **kwargs):
    return 'error', None

from . import firebase
class firebase_view(general_view):
  @firebase.jwt_required
  def as_view(self, *args, **kwargs):
      kwargs['firebase_id'] = request.jwt_payload["user_id"]
      return super().as_view(*args, **kwargs)
  def view(self, data, firebase_id, *args, **kwargs):
      return super().view(data, *args, **kwargs)