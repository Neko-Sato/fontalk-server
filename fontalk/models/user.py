from . import db
from . import exceptions
import re
import rstr

class User(db.Model):
  _id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
  _firebase_id = db.Column('firebase_id', db.VARCHAR(128), unique=True, nullable=False)
  _user_id = db.Column('user_id', db.VARCHAR(16), unique=True)
  _name = db.Column('name', db.VARCHAR(20))
  _image = db.Column('image', db.LargeBinary)
  _follow = db.relationship('Follow', backref='user', foreign_keys='Follow._user', lazy=True)
  _followed = db.relationship('Follow', backref='follow', foreign_keys='Follow._follow', lazy=True)
  _member = db.relationship('Member', backref='user', foreign_keys='Member._user', lazy=True)
  _message = db.relationship('Message', backref='user', foreign_keys='Message._user', lazy=True)
  def __init__(self, firebase_id, user_id=None, name=None, image=None):
    self._firebase_id = firebase_id
    self.user_id = user_id
    self.name = name
    self.image = image
  @property
  def id(self):
    return self._id
  @property
  def firebase_id(self):
    return self._firebase_id
  @property
  def user_id(self):
    return self._user_id
  @user_id.setter
  def user_id(self, user_id):
    if user_id is not None:
      if not self.is_available_user_id(user_id):
        raise exceptions.InvalidUsage("ダメな感じ")
    else:
      while True:
        user_id = rstr.xeger(r"^[a-zA-Z0-9_]{4,16}$")
        if self.is_available_user_id(user_id):
          break
    self._user_id = user_id
  @property
  def name(self):
    return self._name if self._name is not None else f'@{self.user_id}'
  @name.setter
  def name(self, name):
    self._name = name
  @property
  def image(self):
    return self._image
  @image.setter
  def image(self, image):
    self._image = image
  def __repr__(self):
    return '<User {}>'.format(self._id)
  @classmethod
  def from_firebase_id(cls, firebase_id):
    return cls.query.filter(cls._firebase_id==firebase_id).one_or_none()
  @classmethod
  def from_user_id(cls, user_id):
    return cls.query.filter(cls._user_id==user_id).one_or_none()
  @classmethod
  def from_user_id_list(cls, user_ids):
    return cls.query.filter(cls._user_id.in_(user_ids))
  @classmethod
  def is_available_user_id(cls, user_id):
    return re.match(r"^[a-zA-Z0-9_]{4,16}$", user_id) and cls.from_firebase_id(user_id) is None

class Follow(db.Model):
  _id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
  _user = db.Column('user', db.Integer, db.ForeignKey('user.id'), nullable=False)
  _follow = db.Column('follow', db.Integer, db.ForeignKey('user.id'), nullable=False)
  def __init__(self, user, follow):
    if user == follow: raise Exception
    self._user = user
    self._follow = follow
  @property
  def user(self):
    return self._user
  @property
  def follow(self):
    return self._follow
  def __repr__(self):
    return '<follow {}>'.format(self._id)