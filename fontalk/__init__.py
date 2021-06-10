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
app.url_map = routes.url_map
app.register_error_handler(exceptions.InvalidUsage, erorr_handlers.handle_invalid_usage)
app.register_error_handler(exceptions.HTTPException, erorr_handlers.handle_exception)