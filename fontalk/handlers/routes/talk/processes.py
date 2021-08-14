from fontalk.models.talk import Talk
from typing import Union
from . import view
from . import exceptions
from . import models
from . import firebase
from fontalk.handlers.routes import talk

class get_talks(view.firebase_view):
  def view(self, user:models.User):
    data = user.get_talks()
    return '', data

class get_members(view.firebase_view):
  def view(self, user:models.User, talk:int):
    #data = models.Talk.get(talk).get_members(user.id)
    data = models.Member.get_members(talk, user.id)
    return '', data

class info(view.firebase_view):
  def view(self, user:models.User, talk:int):
    data = Talk.get(talk).info()
    return 'Successfully get talk information', data

class create(view.firebase_view):
  def view(self, user:models.User, name:Union[str, None]=None, image:Union[bytes, None]=None):
    data = models.Talk.create(user.id, name, image).info()
    return 'Successfully create talk.', data

class setup(view.firebase_view):
  def view(self, user:models.User, talk:int, \
    name:Union[str, None, models.nodata]=models.nodata, \
    image:Union[bytes, None, models.nodata]=models.nodata):
    models.Talk.get(talk).update(user.id, name, image)
    return 'Successfully update talk.', None

class delete(view.firebase_view):
  def view(self, user:models.User, talk:int):
    models.Talk.get(talk).delete(user.id)
    return 'Successfully delete talk', None

class add_members(view.firebase_view):
  def view(self, user:models.User, talk:int, targets:list[int]):
    #models.Talk.get(talk).add_members(user.id, targets)
    models.Member.add_members(talk, user.id, targets)
    return 'Successfully add members', None

class del_members(view.firebase_view):
  def view(self, user:models.User, talk:int, targets:list[int]):
    #models.Talk.get(talk).del_members(user.id, targets)
    models.Member.del_members(talk, user.id, targets)
    return 'Successfully delete members', None

class participate(view.firebase_view):
  def view(self, user:models.User, talk:int):
    #models.Talk.get(talk).participate(user.id)
    models.Member.get(talk, user.id).participate()
    return 'Successfully participate', None

class message(view.firebase_view):
  pass