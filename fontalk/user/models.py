from . import db

def randam_string(n):
  from string import digits, ascii_lowercase, ascii_uppercase
  from random import choice
  dat = digits + ascii_lowercase + ascii_uppercase + '_'
  return ''.join([choice(dat) for i in range(n)])

class User(db.Model):
  _id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
  _firebase_id = db.Column('firebase_id', db.VARCHAR(128), unique=True, nullable=False)
  _user_id = db.Column('user_id', db.VARCHAR(16), unique=True, nullable=False)
  _name = db.Column('name', db.VARCHAR(20))
  _image = db.Column('image', db.LargeBinary)
  _follow = db.relationship('Follow', backref='user', foreign_keys='Follow._user', lazy=True)
  _followed = db.relationship('Follow', backref='follow', foreign_keys='Follow._follow', lazy=True)
  def __init__(self, firebase_id, user_id=None, name=None, image=None):
    self._firebase_id = firebase_id
    self._user_id = user_id if user_id is not None else randam_string(16)
    self._name = name
    self._image = image
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
      self._user_id = user_id
  @property
  def name(self):
    return self._name if self._name is not None else '@{}'.format(self.user_id)
  @name.setter
  def name(self, name):
    if name is not None:
      self._name = name  
  @property
  def image(self):
    return self._image if self._image is not None else 'default'
  @image.setter
  def image(self, image):
    if image == b'\0':
      self._image = None
    elif image is not None:
      self._image = image
  def __repr__(self):
    return '<User {}>'.format(self._id)

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