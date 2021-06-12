from flask_cors import extension
from . import view
from . import exceptions

class handle_invalid_usage(view.error_viwe):
  exception = exceptions.InvalidUsage
  def view(self, error):
    return error.message, error.status_code

class handle_exception(view.error_viwe):
  exception = exceptions.HTTPException
  def view(self, error):
    return error.name, error.code