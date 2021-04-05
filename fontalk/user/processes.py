from .models import *
from . import no_data

def create(user_id, name, image):
  if User.query.get(user_id) == None:
    user = User(\
      id=user_id, \
      name=no_data.W(name, None), \
      image=no_data.W(image, None), \
    )
    db.session.add(user)
    db.session.commit()
    temp = {"message": "新規に登録しました"}
  else:
    temp = {"message": "既に存在しているユーザーです"}
  return temp

def update(user_id, name, image):
  user = User.query.get(user_id)
  if not user == None:
    if not no_data.Q(name):
      user.name = name
    if not no_data.Q(image):
      user.image = image
    db.session.commit()
    temp = {"message": "変更を登録しました"}
  else:
    temp = {"message": "存在しないユーザーです"}
  return temp