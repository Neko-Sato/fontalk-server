from werkzeug.routing import Map, Rule, Submount
from .processes import \
  get_talks

url_map = Map([
            Rule('/list', methods=['POST'], endpoint=get_talks.endpoint()), \
            Rule('/upload', methods=['POST']), \
            Submount('/<string:font_name>', [\
              Rule('/download', methods=['POST']), \
              Rule('/delete', methods=['POST']), \
            ])
          ])