from . import view

class test(view.general_view):
  def view(self, **data):
      return "test", data
