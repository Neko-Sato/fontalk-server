from .models import *

def create(user_id, **data):
  if User.query.get(user_id) == None:
    user = User(\
      id=user_id, \
      name=data.get('name'), \
      image=data.get('image'), \
    )
    db.session.add(user)
    db.session.commit()
    temp = {"message": "新規に登録しました"}
  else:
    temp = {"message": "既に存在しているユーザーです"}
  return temp
def update(user_id, **data):
  user = User.query.get(user_id)
  if not user == None:
    for key, value in data.items():
      setattr(user, key, value)
    db.session.commit()
    temp = {"message": "変更を登録しました"}
  else:
    temp = {"message": "存在しないユーザーです"}
  return temp