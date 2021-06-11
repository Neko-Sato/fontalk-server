from . import exceptions
from .handlers import *

error_handler_spec = {
  None: {
    None: {
      exceptions.InvalidUsage : handle_invalid_usage.get_view(),
      exceptions.HTTPException : handle_exception.get_view()
    }
  }
}