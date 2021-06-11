#input
from .fontalk import app
from .fontalk import firebase
from .fontalk import db
from . import view
from . import exceptions

#output
from . import models
from .handlers import url_map
from .handlers import error_handler_spec

#setting
def FirebaseAdmin_new_make_401(message):
  raise exceptions.InvalidUsage(message, status_code=401)
firebase.make_401 = FirebaseAdmin_new_make_401
del FirebaseAdmin_new_make_401

app.url_map = url_map
app.error_handler_spec = error_handler_spec
