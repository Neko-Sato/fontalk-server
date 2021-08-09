from . import db
from . import exceptions
from datetime import datetime

class Talk(db.Model):
  id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
  name = db.Column('name', db.VARCHAR(20))
  image = db.Column('image', db.LargeBinary)
  member = db.relationship("Member", foreign_keys='Member.talk', cascade='delete')
  message = db.relationship("Message", foreign_keys='Message.talk', cascade='delete')
  def __init__(self, name=None, image=None):
    self.name = name
    self.image = image
  def __repr__(self):
    return '<talk {}>'.format(self.id)

class Member(db.Model):
  id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
  talk = db.Column('talk', db.Integer, db.ForeignKey('talk.id', ondelete="CASCADE"), nullable=False)
  user = db.Column('user', db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)
  is_participated = db.Column('is_participated', db.Boolean, nullable=False, default=False)
  def __init__(self, talk, user, is_participated=False):
    self.talk = talk
    self.user = user
    self.is_participated = is_participated
  def have_authority(self):
    if not self.is_participated:
      exceptions.InvalidUsage('You don\'t have clearance.')

class Message(db.Model):
  id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
  talk = db.Column('talk', db.Integer, db.ForeignKey('talk.id', ondelete="CASCADE"), nullable=False)
  user = db.Column('user', db.Integer, db.ForeignKey('user.id', ondelete="SET NULL"))
  message = db.Column('message', db.TEXT, nullable=False)
  is_binary = db.Column('is_binary', db.Boolean, nullable=False, default=False)
  binary = db.Column('binary', db.LargeBinary, default=None)
  datetime = db.Column('datetime', db.DATETIME, nullable=False, default=datetime.now())
  def __init__(self, talk, user, message, is_binary=False, binary=None):
    self.talk = talk
    self.user = user
    self.message = message
    self.is_binary = is_binary
    self.binary = binary
  def __repr__(self):
    return '<message {}>'.format(self.id)
