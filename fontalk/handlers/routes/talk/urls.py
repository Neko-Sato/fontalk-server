from werkzeug.routing import Map, Rule, Submount
from .processes import \
  get_talks, \
  get_members, \
  create, \
  delete, \
  info, \
  setup, \
  add_members, \
  remove_members, \
  participate, \
  message

url_map = Map([
            Rule('/get_talks', methods=['POST'], endpoint=get_talks.endpoint()),
            Rule('/get_members', methods=['POST'], endpoint=get_members.endpoint()),

            Rule('/create', methods=['POST'], endpoint=create.endpoint()),
            Rule('/delete', methods=['POST'], endpoint=delete.endpoint()),

            Rule('/info', methods=['POST'], endpoint=info.endpoint()),
            Rule('/setup', methods=['POST'], endpoint=setup.endpoint()),

            Rule('/add_members', methods=['POST'], endpoint=add_member.endpoint()),
            Rule('/remove_members', methods=['POST'], endpoint=remove_member.endpoint()),
            Rule('/participate', methods=['POST'], endpoint=participate.endpoint()),

            Rule('/message', methods=['POST'], endpoint=message.endpoint()),
          ])