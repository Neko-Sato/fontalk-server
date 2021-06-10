from werkzeug.routing import Map, Rule, Submount
from .processes import test

url_map = Map([
               Rule('/test', methods=None, endpoint=test.endpoint()),
               #Submount('/user', user.url_map.iter_rules())
          ])