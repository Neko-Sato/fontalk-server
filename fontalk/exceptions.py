from werkzeug.exceptions import *
from sqlalchemy.exc import *
from sqlalchemy.orm.exc import *

class InvalidUsage(Exception):
  status_code = 400
  def __init__(self, message:str, status_code:int=None, payload=None):
    super().__init__(self)
    self.message = message
    if status_code is not None:
      self.status_code = status_code
    self.payload = payload
