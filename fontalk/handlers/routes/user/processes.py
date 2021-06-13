from . import view
from . import exceptions
from . import models
import re

class is_registered(view.firebase_view):
  def view(self, data, firebase_id):
    user = models.user.User.query.filter(\
      models.user.User._firebase_id==firebase_id).one_or_none()
    return 'Registered' if user is not None else 'Not registered', None

class create(view.firebase_view):
  def view(self, data, firebase_id):
    try:
      models.user.User(\
        firebase_id=firebase_id, \
        user_id=data.get("user_id"), \
        name=data.get("name"), \
        image=data.get("image"), \
      )
    except exceptions.IntegrityError as e:
      if e.orig.args[0] == 1062:
        if 'user.firebase_id' in e.orig.args[1]:
          raise exceptions.InvalidUsage('Registered accounts')
      raise e
    return 'Successfully created account', None

class delete(view.firebase_view):
  def view(self, data, firebase_id):
    models.user.User.query.filter(\
      models.user.User._firebase_id==firebase_id).one().delete()
    return 'Successfully delete account', None

class is_available_user_id(view.firebase_view):
  def view(self, data, firebase_id):
    user_id = data.get('user_id')
    if isinstance(user_id, str):
      exceptions.InvalidUsage('user_id is not string type')
    user = models.user.User.query.filter(\
      models.user.User._user_id==user_id).one_or_none()
    return 'Available' if (user is None) and re.match("^[a-zA-Z0-9_]{4,16}$", user_id) else 'Not available', None