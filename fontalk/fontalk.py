from .modules import Flask
from .modules import FirebaseAdmin
from .modules import SQLAlchemy
from .modules import CORS
from .config import config

app = Flask('fontalk')
config(app)
CORS(app)
firebase = FirebaseAdmin(app)
db = SQLAlchemy(app)