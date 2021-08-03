from werkzeug.routing import Map, Rule, Submount
from .processes import \
  setup, \
  info, \
  is_available_user_id, \
  delete \

url_map = Map([
               Rule('/setup', methods=['POST'], endpoint=setup.endpoint()),
               Rule('/is_available_user_id', methods=['POST'], endpoint=is_available_user_id.endpoint()),
               Rule('/delete', methods=['POST'], endpoint=delete.endpoint()),
               Rule('/info', methods=['POST'], endpoint=info.endpoint()),
          ])