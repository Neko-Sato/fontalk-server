from werkzeug.routing import Map, Rule, Submount
from .processes import \
  is_registered, \
  is_available_user_id, \
  create, \
  delete

url_map = Map([
               Rule('/is_registered', methods=['POST'], endpoint=is_registered.endpoint()),
               Rule('/is_available_user_id', methods=['POST'], endpoint=is_available_user_id.endpoint()),
               Rule('/create', methods=['POST'], endpoint=create.endpoint()),
               Rule('/delete', methods=['POST'], endpoint=delete.endpoint()),
          ])