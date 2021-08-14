from typing import Union
from . import view
from . import exceptions
from . import models
from . import firebase

class setup(view.firebase_view):
  def view(self, user:models.User, \
    name:Union[str, None, models.nodata]=models.nodata, \
    user_id:Union[str, None, models.nodata]=models.nodata, \
    image:Union[bytes, None, models.nodata]=models.nodata):
    user.update(name=name, user_id=user_id, image=image)
    return 'Successfully update user information.', None

class info(view.firebase_view):
  def view(self, user:models.User, target:Union[int, None]=None):
    if target is not None:
      user = models.User.get(target)
    data = user.info()
    return 'Successfully get user information', data

class info_from_user_id(view.firebase_view):
  def view(self, user:models.User, target:str):
    data = models.User.from_user_id(target).info()
    return 'Successfully get user information', data

class delete(view.firebase_view):
  def view(self, user:models.User):
    user.delete()
    return 'Successfully delete account', None

class is_available_user_id(view.firebase_view):
  def view(self, user:models.User, user_id:str):
    isunregistered = user.is_available_user_id(user_id)
    return 'Available' if isunregistered else 'Not available', isunregistered