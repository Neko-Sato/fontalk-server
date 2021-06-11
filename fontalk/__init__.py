#input
from .fontalk import app
from .fontalk import firebase
from .fontalk import db
from . import view
from . import exceptions
from . import error_handlers

#output
from . import models
from . import routes

#setting
def FirebaseAdmin_new_make_401(message):
  raise exceptions.InvalidUsage(message, status_code=401)
firebase.make_401 = FirebaseAdmin_new_make_401
del FirebaseAdmin_new_make_401

app.url_map = routes.url_map
app.register_error_handler(exceptions.InvalidUsage, error_handlers.handle_invalid_usage.get_view())
app.register_error_handler(exceptions.HTTPException, error_handlers.handle_exception.get_view())