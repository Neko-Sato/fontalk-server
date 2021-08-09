from werkzeug.routing import Map, Rule, Submount
from .processes import \
  follow,\
  unfollow, \
  get_follows, \
  get_followers

url_map = Map([
            Rule('/follow', methods=['POST'], endpoint=follow.endpoint()),
            Rule('/unfollow', methods=['POST'], endpoint=unfollow.endpoint()),
            Rule('/get_follows', methods=['POST'], endpoint=get_follows.endpoint()),
            Rule('/get_followers', methods=['POST'], endpoint=get_followers.endpoint()),
          ])