from models import *
import json

class test:
  def test(user_id):
    temp = {\
      "message": "your userid is {}".format(user_id), \
    }
    return temp

class talks:
  def get_list(user_id):
    user = User.query.get(user_id)
    print(user)
    if user == None:
      temp = {\
        "message": "error :User information is not registered.", \
      }
    else:
      temp = {}
    return temp

class user:
  def create(user_id, name, image=None):
    me = User(\
      id=user_id, \
      name=name, \
    )
    db.session.add(me)
    db.session.commit()
    return {}