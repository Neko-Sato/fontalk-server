from . import routing
from . import processes

url_map = routing.Map([
              routing.Rule('/is-already-registered'),
              routing.Rule('/create'),
              routing.Rule('/follow'),
              routing.Rule('/unfollow'),
          ])