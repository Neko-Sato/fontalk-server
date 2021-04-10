from .models import *
from ..user.models import User
from . import erorr_handlers
from fontalk import talk

#トークを作成
def create(firebase_id, name=None, image=None, users=[]):
  talk = Talk(\
    name=name, \
    image=image, \
  )
  db.session.add(talk)
  db.session.flush()
  creater = User.query.filter(User._firebase_id==firebase_id).one()
  db.session.add(Member(talk.id, creater.id, True))
  users = User.query.filter(User._user_id.in_(users)).all()
  db.session.add_all([Member(talk.id, i.id) for i in users])
  db.session.commit()
  return {"message": "新規にトークを作成しました"}

#トーク情報を更新
def update(firebase_id, talk_id, name=None, image=None):
  user = User.query.filter(User._firebase_id==firebase_id).one()
  try:
    Member.query.filter(\
      Member._talk==talk_id, \
      Member._user==user.id, \
      Member._is_participated==True\
    ).one()
  except erorr_handlers.NoResultFound:
    raise erorr_handlers.InvalidUsage('存在しないトークです')
  talk = Talk.query.filter(Talk._id==talk_id).one()
  talk.name = name
  talk.image = image
  db.session.commit()
  return {"message": "トークを変更しました"}

#トークを削除
def delete(firebase_id, talk_id):
  user = User.query.filter(User._firebase_id==firebase_id).one()
  try:
    Member.query.filter(\
      Member._talk==talk_id, \
      Member._user==user.id, \
      Member._is_participated==True\
    ).one()
  except erorr_handlers.NoResultFound:
    raise erorr_handlers.InvalidUsage('存在しないトークです')
  talk = Talk.query.filter(Talk._id==talk_id).one()
  db.session.delete(talk)
  db.session.commit()
  return {"message": "トークを削除しました"}

#トークに招待
def invitation(firebase_id, talk_id, users=[]):
  user = User.query.filter(User._firebase_id==firebase_id).one()
  try:
    Member.query.filter(\
      Member._talk==talk_id, \
      Member._user==user.id, \
      Member._is_participated==True\
    ).one()
  except erorr_handlers.NoResultFound:
    raise erorr_handlers.InvalidUsage('存在しないトークです')
  users = User.query.filter(User._user_id.in_(users)).all()
  db.session.add_all([Member(talk_id, i.id) for i in users])
  db.session.commit()

#トークに参加
def participation(firebase_id, talk_id):
  user = User.query.filter(User._firebase_id==firebase_id).one()
  try:
    member = Member.query.filter(\
      Member._talk==talk_id, \
      Member._user==user.id, \
    ).one()
  except erorr_handlers.NoResultFound:
    raise erorr_handlers.InvalidUsage('存在しないトークです')
  if member.is_participated:
    raise erorr_handlers.InvalidUsage('参加済みです')
  member.is_participated = True
  db.session.commit()

#トークから退会、強制退会
def withdrawal(firebase_id, talk_id, users=None):
  user = User.query.filter(User._firebase_id==firebase_id).one()
  if users is None:
    try:
      member = Member.query.filter(\
        Member._talk==talk_id, \
        Member._user==user.id, \
      ).one()
    except erorr_handlers.NoResultFound:
      raise erorr_handlers.InvalidUsage('存在しないトークです')
    db.session.delete(member)
    temp = {'message': '退会しました'}
  else:
    try:
      Member.query.filter(\
        Member._talk==talk_id, \
        Member._user==user.id, \
        Member._is_participated==True
      ).one()
    except erorr_handlers.NoResultFound:
      raise erorr_handlers.InvalidUsage('存在しないトークです')
    users = [u.id for u in User.query.filter(User._user_id.in_(users)).all()]
    users = Member.query.filter(Member._talk==talk_id, Member._user.in_(users)).all()
    for u in users:
      db.session.delete(u)
    temp = {'message': '退会させました'}
  return temp

#トークメンバーを取得
def get_member(firebase_id, talk_id):
  user = User.query.filter(User._firebase_id==firebase_id).one()
  try:
    Member.query.filter(\
      Member._talk==talk_id, \
      Member._user==user.id, \
    ).one()
  except erorr_handlers.NoResultFound:
    raise erorr_handlers.InvalidUsage('存在しないトークです')
  data = []
  for i in Member.query.filter(Member._talk==talk_id).all():
    u = User.query.get(i.user)
    data.append({\
      'user_id': u.user_id, \
      'is_participated': i.is_participated, \
    })
  return {'message': '取得しました', 'data': data}

def get_talks(firebase_id):
  user = User.query.filter(User._firebase_id==firebase_id).one()
  data = []
  for i in Member.query.filter(Member._user==user.id).all():
    t = Talk.query.get(i.talk)
    data.append({\
      'name': t.name, \
      'is_participated': i.is_participated, \
    })
  return {'message': '取得しました', 'data': data}