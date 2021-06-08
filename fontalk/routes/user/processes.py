from flask import request, make_response
import json
from . import firebase
from . import erorr_handlers
from . import db
from . import models

@firebase.jwt_required
def create():
  user = models.User(\
    firebase_id=firebase_id, \
    user_id=user_id, \
    name=name, \
    image=image, \
  )
  db.session.add(user)
  try:
    db.session.commit()
  except erorr_handlers.IntegrityError as e:
    if e.orig.args[0] == 1062:
      if 'user.firebase_id' in e.orig.args[1]:
        raise erorr_handlers.InvalidUsage('登録済みです')
    else:
      raise e
  return {"message": "新規に登録しました"}