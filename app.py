from flask import Flask, request
import json
import pyrebase

PRJ_ID = "fontalk-6b52a"
API_KEY = "AIzaSyBnHuRLL48L89kOJJbN2i8YBAb73rJx_pA"
config = {
  "apiKey": API_KEY,
  "authDomain": PRJ_ID + ".firebaseapp.com",
  "databaseURL": "https://" + PRJ_ID + ".firebaseio.com/",
  "storageBucket": PRJ_ID + ".appspot.com"
}
firebase = pyrebase.initialize_app(config)
app = Flask(__name__)

@app.route("/")
def hello_world():
  return "Hello, World!"

@app.route("/signin", methods=['GET',"POST"])
def signin():
  if request.method == 'POST':
    data = json.loads(request.data.decode())
  return ""
