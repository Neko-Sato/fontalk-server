from .models import *
from . import no_data

def create(user_id, name, image, users):#トーク作成
  if no_data.Q(name):
    return {'message': '必須項目[name]がありません'}
  if no_data.Q(image):
    image = None
  if no_data.Q(users):
    users = []
  users.append(user_id)
  talk = Talk(\
    name=name, \
    image=image
  )
  Members = []
  for user in users:
    temp = Member(\
    )
    Members.append(temp)

def update():#トーク編集
  pass

def invitation():#トーク招待
  pass

def participate():#メンバー参加
  pass

def withdrawal():#招待拒否、メンバー脱退
  pass

def get_talks():#参加済みトーク習得
  pass

def get_participants():#メンバー一覧取得
  pass

def get_messages():#メッセージ取得
  pass