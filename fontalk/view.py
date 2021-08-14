from typing import Any, Tuple, Callable
from . import app
from . import models
from . import exceptions
from flask import request, make_response, Response
import re
import json

class JSONEncoder(json.JSONEncoder):
  def default(self, obj):
    if isinstance(obj, bytes):
      temp = {'__bytes__': list(bytearray(obj))}
    else:
      temp = super().default(obj)
    return temp
def as_bytes(dct):
  if '__bytes__' in dct:
    return bytes(bytearray(dct['__bytes__']))
  return dct

class general_view:
  app = app
  @classmethod
  def endpoint(cls)->str:
    view = cls.get_view()
    endpoint = str(id(view))
    cls.app.view_functions[endpoint] = view
    return endpoint
  @classmethod
  def get_view(cls)->Callable:
    return cls().as_view
  def as_view(self, *args, **kwargs)->Response:
    try:
      data = json.loads(request.get_data().decode('utf-8'), object_hook=as_bytes)
    except json.decoder.JSONDecodeError:
      raise exceptions.InvalidUsage('Erorr in json decoding.')
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
    response.data = json.dumps({'message': result[0], 'data': result[1]}, cls=JSONEncoder)
    response.mimetype = 'application/json'
    return response
  def view(self, *args, **kwargs)->Tuple[str, Any]:
    return 'massage', None

class error_viwe(general_view):
  exception=Exception
  def as_view(self, error:Exception, *args, **kwargs)->Response:
    response = make_response()
    result = self.view(error, *args, **kwargs)
    response.data = json.dumps({'message': result[0]}, cls=JSONEncoder)
    response.status_code = result[1]
    response.mimetype = 'application/json'
    return response
  def view(self, error:Exception, *args, **kwargs)->Tuple[str, Any]:
    return 'error', None

from . import firebase
class firebase_view(general_view):
  @firebase.jwt_required
  def as_view(self, *args, **kwargs)->Response:
    firebase_id = request.jwt_payload["user_id"]
    user = models.User.from_firebase_id(firebase_id)
    if user is None:
      user = models.User.create(firebase_id)
    return super().as_view(user=user, *args, **kwargs)
  def view(self, user:models.User, *args, **kwargs)->Tuple[str, Any]:
    return super().view(*args, **kwargs, user=user)