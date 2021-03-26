from flask import request, session, jsonify, redirect, url_for, make_response
from main import app, firebase
from models import User
import json

@app.route("/", methods=["POST"])
@firebase.jwt_required
def index():
    user_id = request.jwt_payload["user_id"]
    temp = {\
        "message": "your userid is {}".format(user_id)
    }
    return jsonify(temp)

#About talks
@app.route("/talks/get_list", methods=["POST"])
@firebase.jwt_required
def index():
    user_id = request.jwt_payload["user_id"]
    #try:
    #    データベースからuser_idが同じなユーザーを習得する
    #Exception(んなユーザーはいません):
    #   return errorになっちゃったよでーたくれよ～
    #    そのユーザーがいるtalkのみを習得
    return jsonify({})

#About User
@app.route("/user/create", methods=["POST"])
@firebase.jwt_required
def index():
    user_id = request.jwt_payload["user_id"]
　　#データベースに登録
    #うまくいったよと返信
    return jsonify({})

#-------------------------------------------------------------------------------------
@app.route("/set_user_icon", methods=["POST"])
@firebase.jwt_required
def set_user_icon():
    image = request.files['image'].stream.read()
    return ''

@app.route("/get_user_icon/<string:user_id>", methods=["GET"])
@firebase.jwt_required
def get_user_icon(user_id):
    if user_id == '':
      user_id = request.jwt_payload["user_id"]
    response = make_response()
    response.data = ''
    response.mimetype = 'image/png'
    return response