from . import routing
from . import processes

from . import user

url_map = routing.Map([
               routing.Rule('/test', methods=None, view_func=processes.test),
               routing.Submount('/user2', user.url_map.iter_rules())
          ])