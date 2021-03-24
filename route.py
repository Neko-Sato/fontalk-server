from flask import Flask, request, session, redirect, url_for
from main import app, auth, database
import json

@app.route("/")
def hello_world():
  user = session.get('user')
  print(user)
  return "Hello, World!"

@app.route("/signin_with_email_and_password", methods=["POST"])
def signin_with_email_and_password():
  data = json.loads(request.data.decode())
  user = auth.sign_in_with_email_and_password(data['email'], data['password'])
  print(user)
  session['user'] = user
  return ""

@app.route('/signout', methods=["POST"])
def logout():
  session.clear()
  return ""

@app.route('/refreshToken', methods=["POST"])
def refreshToken():
  session['user'] = auth.refresh(session['user']['refreshToken'])
  return ""