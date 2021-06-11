from . import view
from . import exceptions
from . import models

class create(view.firebase_view):
  def view(self, data, firebase_id):
    user = models.user.User(\
    firebase_id=firebase_id, \
    user_id=data.get("user_id"), \
    name=data.get("name"), \
    image=data.get("image"), \
    )
    models.db.session.add(user)
    try:
      models.db.session.commit()
    except exceptions.IntegrityError as e:
      if e.orig.args[0] == 1062:
        if 'user.firebase_id' in e.orig.args[1]:
          raise exceptions.InvalidUsage('登録済みです')
      else:
        raise e
    return '新規に登録しました', None