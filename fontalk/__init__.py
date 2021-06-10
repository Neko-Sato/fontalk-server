#input
from .fontalk import app
from .fontalk import firebase
from .fontalk import db
from . import view
from . import exceptions
from . import erorr_handlers

#output
from . import models
from . import routes

#setting
def FirebaseAdmin_new_make_401(message):
  raise exceptions.InvalidUsage(message, status_code=401)
firebase.make_401 = FirebaseAdmin_new_make_401
del FirebaseAdmin_new_make_401

app.url_map = routes.url_map
app.register_error_handler(exceptions.InvalidUsage, erorr_handlers.handle_invalid_usage)
app.register_error_handler(exceptions.HTTPException, erorr_handlers.handle_exception)