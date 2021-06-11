from . import view

class handle_invalid_usage(view.error_viwe):
  def view(self, error):
    return error.to_dict(), error.status_code

class handle_exception(view.error_viwe):
  def view(self, error):
    return error.name, error.code