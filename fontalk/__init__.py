from .fontalk import app
from .fontalk import firebase
from .fontalk import db
from .fontalk import no_data
from .fontalk import dict_molding
from .fontalk import get_path

path = get_path(__name__)

from . import models
from . import processes
from . import routes
from . import erorr_handlers

from . import user
from . import talk