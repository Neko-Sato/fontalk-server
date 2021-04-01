from flask import Flask
app = Flask(__name__)

from .config import firebase, db

def get_path(name):
  return ''.join(map(lambda x: '/' + x, name.split('.')[1:]))
path = get_path(__name__)

from . import models
from . import processes
from . import route

from . import user
from . import talk