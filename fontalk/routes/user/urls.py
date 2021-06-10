from werkzeug.routing import Map, Rule, Submount
from .processes import create

url_map = Map([
               Rule('/create', methods=['POST'], endpoint=create.endpoint()),
          ])