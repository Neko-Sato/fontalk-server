from .fontalk import app
from .fontalk import firebase
from .fontalk import db
from .fontalk import routing

from . import erorr_handlers

from .routes import url_map
app.url_map = url_map