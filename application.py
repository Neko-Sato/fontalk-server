from main import firebase
from models import *
import json

class no_data:
  @classmethod
  def setter(cls, target, value, default):
    if not value == cls:
      if value == None:
        temp = default
      else:
        temp = value
    else:
      temp = target
    return temp

class test:
  def test(user_id):
    temp = {\
      "message": "your userid is {}".format(user_id), \
    }
    return temp

class talks:
  def get_list(user_id):
    user = User.query.get(user_id)
    if user == None:
      temp = {\
        "message": "error :User information is not registered.", \
      }
    else:
      temp = {}
    return temp

class user:
  def create(user_id, name, image):
    if User.query.get(user_id) == None:
      user = User()
      user.id = user_id
      user.name = name
      user.image = image
      db.session.add(user)
      db.session.commit()
      temp = {"message": "新規に登録しました"}
    else:
      temp = {"message": "ユーザーは既に存在しています"}
    return temp
  def change(user_id, name, image):
    user = User.query.get(user_id)
    if not user == None:
      user.name = no_data.setter(user.name, name, user_id)
      user.image = no_data.setter(user.image, image, None)
      db.session.commit()
      temp = {"message": "変更を登録しました"}
    else:
      temp = {"message": "存在しないユーザーです"}
    return temp