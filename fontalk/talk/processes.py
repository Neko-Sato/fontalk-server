from .models import *
from ..user.models import User
from . import erorr_handlers

def create(firebase_id, name=None, image=None, users=[]):
  talk = Talk(\
    name=name, \
    image=image, \
  )
  db.session.add(talk)
  db.session.flush()
  creater = User.query.filter(User._firebase_id==firebase_id).one()
  db.session.add(Member(talk.id, creater.id, True))
  db.session.add_all([Member(talk.id, i) for i in users])
  db.session.commit()
  return {"message": "新規にトークを作成しました"}

def update(firebase_id, talk_id, name=None, image=None):
  try:
    talk = Talk.query.filter(Talk._id==talk_id).one()
  except erorr_handlers.NoResultFound:
    raise erorr_handlers.InvalidUsage('存在しないトークです')
  user = User.query.filter(User._firebase_id==firebase_id).one()
  if Member.query.filter(\
    Member._talk==talk.id, \
    Member._user==user.id, \
    Member.is_participated==False\
  ).one_or_none() is None:
    raise erorr_handlers.InvalidUsage('権限がありません')
  talk.name = name
  talk.image = image
  db.session.commit()
  return {"message": "トークを変更しました"}

def delete(firebase_id, talk_id):
  try:
    talk = Talk.query.filter(Talk._id==talk_id).one()
  except erorr_handlers.NoResultFound:
    raise erorr_handlers.InvalidUsage('存在しないトークです')
  user = User.query.filter(User._firebase_id==firebase_id).one()
  if Member.query.filter(\
    Member._talk==talk.id, \
    Member._user==user.id, \
    Member.is_participated==False\
  ).one_or_none() is None:
    raise erorr_handlers.InvalidUsage('権限がありません')
  db.session.delete(talk)
  db.session.commit()
  return {"message": "トークを削除しました"}

def invitation(firebase_id, talk_id, users=[]):
  try:
    talk = Talk.query.filter(Talk._id==talk_id).one()
  except erorr_handlers.NoResultFound:
    raise erorr_handlers.InvalidUsage('存在しないトークです')
  user = User.query.filter(User._firebase_id==firebase_id).one()
  if Member.query.filter(\
    Member._talk==talk.id, \
    Member._user==user.id, \
    Member.is_participated==False\
  ).one_or_none() is None:
    raise erorr_handlers.InvalidUsage('権限がありません')
  db.session.add_all([Member(talk.id, i) for i in users])
  db.session.commit()

def participation(firebase_id, talk_id):
  pass
