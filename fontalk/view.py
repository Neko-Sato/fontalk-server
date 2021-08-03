from . import app
from . import models
from . import exceptions
from flask import request, make_response
import re
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
    try:
      result = self.view(*args, **kwargs, **data)
    except TypeError as e:
      m = re.match(r"^view\(\) missing \d* required positional argument: (.*)$", e.args[0])
      if m is not None:
        raise exceptions.InvalidUsage(f'Missing required argument {m.group(1)}.')
      m = re.match(r"^view\(\) got an unexpected keyword argument (.*)$", e.args[0])
      if m is not None:
        raise exceptions.InvalidUsage(f'Unexpected argument {m.group(1)}.')
      raise e
    response.data = json.dumps({'message': result[0], 'data': result[1]})
    response.mimetype = 'application/json'
    return response
  def view(self, *args, **kwargs):
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
    firebase_id = request.jwt_payload["user_id"]
    user = models.User.from_firebase_id(firebase_id)
    if user is None:
      user = models.User(firebase_id)
      models.db.session.add(user)
      models.db.session.commit()
    return super().as_view(user=user, *args, **kwargs)
  def view(self, data, user, *args, **kwargs):
    return super().view(data, user, *args, **kwargs)