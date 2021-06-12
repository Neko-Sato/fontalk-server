from .handlers import *

class error_Map(list):
  def to_dict(self):
    error_handler_spec = {}
    for handler in self:
      temp = error_handler_spec.\
        setdefault(None, {}).\
        setdefault(getattr(handler.exception, 'code', None), {})
      temp[handler.exception] = handler.get_view()
    return error_handler_spec

error_handler_spec = error_Map([
                                     handle_invalid_usage,
                                     handle_exception,
                     ]).to_dict()