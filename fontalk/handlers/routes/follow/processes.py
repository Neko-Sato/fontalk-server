from sqlalchemy.sql.functions import mode
from . import view
from . import exceptions
from . import models
from . import firebase

class follow(view.firebase_view):
  def view(self, user, target):
    target = models.User.query.get(target)
    user.follow(target)
    return '', None

class unfollow(view.firebase_view):
  def view(self, user, target):
    target = models.User.query.get(target)
    user.unfollow(target)
    return '', None

class get_follows(view.firebase_view):
  def view(self, user):
    temp = user.get_follows()
    data = [{
          'id' : i[0],
          'name': i[1],
          'user_id' : i[3],
          'image' : i[4],
        } for i in temp]
    return '', data

class get_followers(view.firebase_view):
  def view(self, user):
    temp = user.get_followers(user)
    data = [{
          'id' : i[0],
          'name': i[1],
          'user_id' : i[3],
          'image' : i[4],
        } for i in temp]
    return '', data