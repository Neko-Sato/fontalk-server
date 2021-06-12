from . import view
from . import exceptions
from . import models

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

class is_available_user_id(view.firebase_view):
  def view(self, data, firebase_id):
    user_id = data.get('user_id')
    if isinstance(user_id, str):
      exceptions.InvalidUsage('user_id is not string type')
    user = models.User.query.filter(\
      models.User._user_id==user_id).one_or_none()
    return 'Available' if user is None else 'Not available', None