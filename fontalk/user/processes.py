from .models import *
from . import erorr_handlers

def create(firebase_id, user_id=None, name=None, image=None):
  user = User(\
    firebase_id=firebase_id, \
    user_id=user_id, \
    name=name, \
    image=image, \
  )
  db.session.add(user)
  try:
    db.session.commit()
  except erorr_handlers.IntegrityError as e:
    if e.orig.args[0] == 1062:
      if 'user.firebase_id' in e.orig.args[1]:
        raise erorr_handlers.InvalidUsage('登録済みです')
    else:
      raise e
  return {"message": "新規に登録しました"}

def update(firebase_id, user_id=None, name=None, image=None):
  try:
    user = User.query.filter(User._firebase_id==firebase_id).one()
  except erorr_handlers.NoResultFound:
    raise erorr_handlers.InvalidUsage('存在しないユーザーです')
  setattr(user, 'user_id', user_id)
  setattr(user, 'name', name)
  setattr(user, 'imag', image)
  db.session.commit()
  return {"message": "変更を登録しました"}

def follow(firebase_id, follow_id):
  try:
    user = User.query.filter(User._firebase_id==firebase_id).one()
    follow = User.query.filter(User._user_id==follow_id).one()
  except erorr_handlers.NoResultFound:
    raise erorr_handlers.InvalidUsage('存在しないユーザーです')
  if Follow.query.filter(Follow.user==user.id, Follow.follow==follow.id).one_or_none() is not None:
    raise erorr_handlers.InvalidUsage("既にフォロー済みです")
  follow = Follow(user=user.id, follow=follow.id)
  db.session.add(follow)
  db.session.commit()
  return {"message": "フォローしました"}

def unfollow(firebase_id, follow_id):
  try:
    user = User.query.filter(User.firebase_id==firebase_id).one()
    followed = User.query.filter(User.user_id==follow_id).one()
  except erorr_handlers.NoResultFound:
    raise erorr_handlers.InvalidUsage('存在しないユーザーです')
  try:
    follow = Follow.query.filter(Follow.user==user.id, Follow.follow==followed.id).one()
  except erorr_handlers.NoResultFound:
    raise erorr_handlers.InvalidUsage('フォローされていません')  
  db.session.delete(follow)
  db.session.commit()
  return {"message": "フォロー解除しました"}
