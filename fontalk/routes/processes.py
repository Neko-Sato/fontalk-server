from . import view

class test(view.general_view):
  def view(self, data, *args, **kwargs):
      return "fbsb", data