from . import db
from datetime import datetime

class Member(db.Model):
  __id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
  __talk = db.Column('talk', db.Integer, db.ForeignKey('talk.id'), nullable=False)
  __user = db.Column('user', db.VARCHAR(128), db.ForeignKey('user.id'), nullable=False)
  __is_participated = db.Column('is_participated', db.Boolean, nullable=False, default=False)
  def __init__(self, talk, user, is_participated=False):
    self.__talk = talk
    self.__user = user
    self.__is_participated = is_participated
  @property
  def id(self):
    return self.__id
  @property
  def talk(self):
    return self.__talk
  @property
  def user(self):
    return self.__user
  @property
  def is_participated(self):
    return self.__is_participated
  @is_participated.setter
  def is_participated(self, value):
    self.__is_participated = value
  def __repr__(self):
    return '<member {}>'.format(self.id)

class Message(db.Model):
  __id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
  __talk = db.Column('talk', db.Integer, db.ForeignKey('talk.id'), nullable=False)
  __user = db.Column('user', db.VARCHAR(128), db.ForeignKey('user.id'), nullable=False)
  __message = db.Column('message', db.TEXT, nullable=False)
  __is_binary = db.Column('is_binary', db.Boolean, nullable=False, default=False)
  __binary = db.Column('binary', db.LargeBinary, default=None)
  __datetime = db.Column('datetime', db.DATETIME, nullable=False, default=datetime.now())
  def __init__(self, talk, user, message, is_binary=False, binary=None):
    self.__talk = talk
    self.__user = user
    self.__message = message
    self.__is_binary = is_binary
    self.__binary = binary
  @property
  def id(self):
    return self.__id
  @property
  def talk(self):
    return self.__talk
  @property
  def user(self):
    return self.__user
  @property
  def is_binary(self):
    return self.__is_binary
  @property
  def message(self):
    return self.__message
  @property
  def binary(self):
    return self.__binary
  @property
  def datetime(self):
    return self.__datetime
  def __repr__(self):
    return '<message {}>'.format(self.id)

class Talk(db.Model):
  __id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
  __name = db.Column('name', db.VARCHAR(20), nullable=False)
  __image = db.Column('image', db.LargeBinary)
  __member = db.relationship("Member", backref="talk", lazy=True)
  __message = db.relationship("Message", backref="talk", lazy=True)
  def __init__(self, user_id, name=None, image=None, users=[]):
    self.__name = name
    self.__image = image
  @property
  def id(self):
    return self.__id
  @property
  def name(self):
    return self.__name if not self.__name == None else self.id
  @name.setter
  def name(self, value):
    self.__name = value
  @property
  def image(self):
    return self.__image if not self.__image == None else 'default'
  @image.setter
  def image(self, value):
    self.__image = value
  def __repr__(self):
    return '<talk {}>'.format(self.id)