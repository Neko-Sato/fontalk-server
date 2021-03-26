from flask import Flask
from flask_firebase_admin import FirebaseAdmin

app = Flask(__name__)
app.config["FIREBASE_ADMIN_CREDENTIAL"] = \
    FirebaseAdmin.credentials.Certificate("serviceAccountKey.json")

firebase = FirebaseAdmin(app)

import database
import route