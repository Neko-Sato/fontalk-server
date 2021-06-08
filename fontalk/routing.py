from werkzeug.routing import Map, Rule, Submount

class Routing:
  Map = Map
  Rule = Rule
  Submount = Submount
  def __init__(self, app):
    self.app = app
  def Rule(self, *args, **kwargs):
    if 'view_func' in kwargs:
      view_func = kwargs.pop('view_func')
      endpoint = str(id(view_func))
      self.app.view_functions[endpoint] = view_func
      kwargs['endpoint'] = endpoint
    return Rule(*args, **kwargs)