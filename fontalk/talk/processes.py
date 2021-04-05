from .models import *
from . import no_data

def create(user_id, name, image, users):#トーク作成
  talk = Talk(\
    user_id=user_id, \
    name=no_data.W(name, None), \
    image=no_data.W(image, None), \
  )
  db.session.add(talk)
  db.session.flush()
  db.session.add(Member(talk.id, user_id, True))
  db.session.commit()
  invitation(talk.id, users)
  return {'message': 'talkを作成しました'}

def update(talk_id, name, image):#トーク編集
  talk = Talk.query.get(talk_id)
  if not talk == None:
    if not no_data.Q(name):
      talk.name = name
    if not no_data.Q(image):
      talk.image = image
    db.session.commit()
    temp = {"message": "変更を登録しました"}
  else:
    temp = {"message": "存在しないトークです"}
  return temp

def invitation(talk_id, users):#トーク招待
  talk = Talk.query.get(talk_id)
  if not talk == None:
    for u in no_data(users, []):
      db.session.add(Member(talk.id, u))
    db.session.commit()
    temp = {"message": "トークに招待しました"}
  else:
    temp = {"message": "存在しないトークです"}
  return temp


def participate(user_id, talk_id):#メンバー参加
  member = Member.query.filter_by(\
    user=user_id, \
    talk=talk_id, \
  ).first()
  if not member == None:
    if member.is_participated:
      temp = {"message": "招待済みです"}
    else:
      member.is_participated = True
      temp = {"message": "トークに招待しました"}
  else:
    temp = {"message": "招待されていません"}
  return temp

def withdrawal(user_id, talk_id):#招待拒否、メンバー脱退
  member = Member.query.filter_by(\
    user=user_id, \
    talk=talk_id, \
  ).first()
  if not member == None:
    if member.is_participated:
      temp = {"message": "脱退しました"}
    else:
      temp = {"message": "拒否しました"}
    db.session.delete(member)
    db.session.commit()
  else:
    temp = {"message": "招待されていません"}
  return temp

def get_talks(user_id):#トーク習得
  talks = [Talk.query.get(i.talk).get_dict() for i in Member.query.filter_by(user=user_id)]
  temp = {"message": "トーク一覧です", "data": talks}
  return temp

def get_member(talk_id):#メンバー一覧取得
  talk = Talk.query.get(talk_id)
  if not talk == None:
    talks = [User.query.get(i.user).get_dict() for i in Member.query.filter_by(talk=talk_id)]
    temp = {"message": "メンバー一覧です", "data": talks}
  else:
    temp = {"message": "存在しないトークです"}
  return temp

def get_messages():#メッセージ取得
  pass