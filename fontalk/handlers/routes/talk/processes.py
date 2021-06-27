from fontalk.models import talk
from . import view
from . import exceptions
from . import models
from . import firebase

class get_talks(view.firebase_view):
  def view(self, user):
    talks = models.Member.from_user_id(user.id).all()
    return '', None

class get_members(view.firebase_view):
  def view(self, user, talk_id):
    members = models.Member.from_talk_id(talk_id).all()
    return '', None

class create(view.firebase_view):
  def view(self, user, name=None, image=None, members=[]):
    talk = models.Talk(\
      neam=name, \
      image=image, \
    )
    models.db.session.add(talk)
    models.db.session.flush()
    models.db.session.add(models.Member(talk.id, user.id, True))
    models.db.session.add_all([\
      models.Member(talk.id, i.id) for i in \
        models.User.from_user_id_list(members).all()\
    ])
    models.db.session.commit()
    return 'Successfully create talk.', {'talk_id': talk.id}

class delete(view.firebase_view):
  def view(self, user, talk_id):
    member = models.Member.from_user_id_and_talk_id(\
      user_id=user.id, \
      talk_id=talk_id, \
    )
    member.have_authority()
    models.db.session.delete(models.Talk.query.id(member.talk_id))
    models.db.session.commit()
    return 'Successfully delete talk', None

class info(view.firebase_view):
  pass

class setup(view.firebase_view):
  pass

class add_members(view.firebase_view):
  def view(self, user, talk_id, members):
    member = models.Member.from_user_id_and_talk_id(\
      user_id=user.id, \
      talk_id=talk_id, \
    )
    member.have_authority()
    members = [models.Member(member.id, i.id) \
      for i in models.User.from_user_id_list(members).all()]
    models.db.session.add_all(members)
    models.db.session.commit()
    return 'Successfully add members', None

class remove_members(view.firebase_view):
  def view(self, user, talk_id, members):
    member = models.Member.from_user_id_and_talk_id(\
      user_id=user.id, \
      talk_id=talk_id, \
    )
    member.have_authority()
    models.Member.from_user_id_list_and_talk_id(
      user_ids=[i.id for i in \
        models.User.from_user_id_list(members).all()], \
      talk_id=member.talk_id, \
    ).delete()
    models.db.session.commit()
    return 'Successfully remove members', None

class participate(view.firebase_view):
  def view(self, user, talk_id):
    member = models.Member.from_user_id_and_talk_id(\
      user_id=user.id, \
      talk_id=talk_id, \
    )
    try:
      member.have_authority()
    except exceptions.InvalidUsage as e:
      member.is_participated = True
      models.db.session.commit()
      return "I've already joined.", None
    exceptions.InvalidUsage("I'm already in.")

class message(view.firebase_view):
  pass