from werkzeug.routing import Map, Rule, Submount
from .processes import test
from . import user

url_map = Map([
               Rule('/test', methods=['POST'], endpoint=test.endpoint()),
               Submount('/user', user.url_map.iter_rules())
          ])