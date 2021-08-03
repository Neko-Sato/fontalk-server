from . import view
from . import exceptions
from . import models
from . import firebase

class setup(view.firebase_view):
  def view(self, user, name=None, user_id=None, image=None):
    if name is not None:
      user.name = name
    if user_id is not None:
      user.user_id = user_id
      firebase.auth.update_user(user.firebase_id, display_name=user_id)
    if image is not None:
      user.image = bytes(bytearray(image))
    models.db.session.commit()
    return 'Successfully update user information.', None

class info(view.firebase_view):
  def view(self, user):
    data = {
      'name': user.name,
      'user_id': user.user_id,
      'image': list(bytearray(user.image)),
    }
    return 'Successfully get user information', data

class delete(view.firebase_view):
  def view(self, user):
    models.db.session.delete(user)
    models.db.session.commit()
    return 'Successfully delete account', None

class is_available_user_id(view.general_view):
  def view(self, user_id):
    if not isinstance(user_id, str):
      raise exceptions.InvalidUsage('user_id is not string type')
    isunregistered = models.User.is_available_user_id(user_id)
    return 'Available' if isunregistered else 'Not available', None