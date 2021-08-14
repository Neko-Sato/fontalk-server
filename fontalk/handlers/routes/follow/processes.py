from . import view
from . import exceptions
from . import models
from . import firebase

class follow(view.firebase_view):
  def view(self, user:models.User, target:int):
    target = models.User.get(target)
    user.follow(target)
    return '', None

class unfollow(view.firebase_view):
  def view(self, user:models.User, target:int):
    target = models.User.get(target)
    user.unfollow(target)
    return '', None

class get_follows(view.firebase_view):
  def view(self, user:models.User):
    data = user.get_follows()
    return '', data

class get_followers(view.firebase_view):
  def view(self, user:models.User):
    data = user.get_followers()
    return '', data