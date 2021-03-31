from flask import Flask
app = Flask(__name__)

from .config import firebase, db
from . import models
from . import application
from . import route