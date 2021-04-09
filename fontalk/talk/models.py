from . import db
from datetime import datetime

class Talk(db.Model):
  _id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
  _name = db.Column('name', db.VARCHAR(20), nullable=False)
  _image = db.Column('image', db.LargeBinary)
  _member = db.relationship("Member", backref="talk", foreign_keys='Member._talk', lazy=True)
  _message = db.relationship("Message", backref="talk", foreign_keys='Message._talk', lazy=True)
  def __init__(self, name=None, image=None):
    self._name = name
    self._image = image
  @property
  def id(self):
    return self._id
  @property
  def name(self):
    return self._name if self._name is not None else '${}'.fromat(self.id)
  @name.setter
  def name(self, value):
    self._name = value
  @property
  def image(self):
    return self._image if self._image is not None else 'default'
  @image.setter
  def image(self, value):
    self._image = value
  def __repr__(self):
    return '<talk {}>'.format(self.id)

class Member(db.Model):
  _id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
  _talk = db.Column('talk', db.Integer, db.ForeignKey('talk.id'), nullable=False)
  _user = db.Column('user', db.VARCHAR(128), db.ForeignKey('user.id'), nullable=False)
  _is_participated = db.Column('is_participated', db.Boolean, nullable=False, default=False)
  def __init__(self, talk, user, is_participated=False):
    self._talk = talk
    self._user = user
    self._is_participated = is_participated
  @property
  def id(self):
    return self._id
  @property
  def talk(self):
    return self._talk
  @property
  def user(self):
    return self._user
  @property
  def is_participated(self):
    return self._is_participated
  @is_participated.setter
  def is_participated(self, value):
    self._is_participated = value
  def __repr__(self):
    return '<member {}>'.format(self.id)

class Message(db.Model):
  _id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
  _talk = db.Column('talk', db.Integer, db.ForeignKey('talk.id'), nullable=False)
  _user = db.Column('user', db.VARCHAR(128), db.ForeignKey('user.id'), nullable=False)
  _message = db.Column('message', db.TEXT, nullable=False)
  _is_binary = db.Column('is_binary', db.Boolean, nullable=False, default=False)
  _binary = db.Column('binary', db.LargeBinary, default=None)
  _datetime = db.Column('datetime', db.DATETIME, nullable=False, default=datetime.now())
  def __init__(self, talk, user, message, is_binary=False, binary=None):
    self._talk = talk
    self._user = user
    self._message = message
    self._is_binary = is_binary
    self._binary = binary
  @property
  def id(self):
    return self._id
  @property
  def talk(self):
    return self._talk
  @property
  def user(self):
    return self._user
  @property
  def is_binary(self):
    return self._is_binary
  @property
  def message(self):
    return self._message
  @property
  def binary(self):
    return self._binary
  @property
  def datetime(self):
    return self._datetime
  def __repr__(self):
    return '<message {}>'.format(self.id)
