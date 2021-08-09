from . import view
from . import exceptions
from . import models
from . import firebase

class setup(view.firebase_view):
  def view(self, user, name=models.nodata, user_id=models.nodata, image=models.nodata):
    user.update(\
      name=name, \
      user_id=user_id, \
      image = bytes(bytearray(image)) if isinstance(image, list) else image
    )
    return 'Successfully update user information.', None

class info(view.firebase_view):
  def view(self, user):
    data = user.info()
    data['image'] = list(bytearray(data['image'])) \
      if isinstance(data['image'], bytes) else data['image']
    return 'Successfully get user information', data

class delete(view.firebase_view):
  def view(self, user):
    user.delete()
    return 'Successfully delete account', None

class is_available_user_id(view.firebase_view):
  def view(self, user, user_id):
    isunregistered = user.is_available_user_id(user_id)
    return 'Available' if isunregistered else 'Not available', None