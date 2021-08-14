from __future__ import annotations
from typing import Any, Union
import rstr
from . import db
from . import exceptions
from . import nodata
from . import follow as _follow
from . import talk as _talk

class User(db.Model):
  id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
  firebase_id = db.Column('firebase_id', db.VARCHAR(128), unique=True, nullable=False)
  user_id = db.Column('user_id', db.VARCHAR(16), db.CheckConstraint(f"user_id REGEXP '{r'^[a-zA-Z0-9_]{4,16}$'}'"), unique=True, nullable=False)
  name = db.Column('name', db.VARCHAR(20))
  image = db.Column('image', db.LargeBinary)
  _follow = db.relationship('Follow', foreign_keys='Follow.user', cascade='delete')
  _followed = db.relationship('Follow', foreign_keys='Follow.target', cascade='delete')
  _member = db.relationship('Member', foreign_keys='Member.user', cascade='delete')
  _message = db.relationship('Message', foreign_keys='Message.user', cascade='delete-orphan, delete')
  def __init__(self, firebase_id:str, user_id:str, name:str=None, image:bytes=None):
    self.firebase_id = firebase_id
    self.user_id = user_id
    self.name = name
    self.image = image
  def __repr__(self):
    return '<User {}>'.format(self.id)
  #//////////////////////////////////////////////////////////////////////////////////////////
  @classmethod
  def create(cls, firebase_id:str)->User:
    try:
      user_id = rstr.xeger(r"^[a-zA-Z0-9_]{4,16}$")
      user = cls(firebase_id, user_id)
      db.session.add(user)
      db.session.commit()
    except exceptions.IntegrityError:
      db.session.rollback()
      user = cls.create(firebase_id)
    return user
  def update(self, name:Union[str, None, nodata]=nodata, user_id:Union[str, None, nodata]=nodata, image:Union[bytes, None, nodata]=nodata):
    if name is not nodata: self.name = name
    if user_id is not nodata: self.user_id = user_id
    if image is not nodata: self.image = image
    db.session.commit()
  def delete(self):
    db.session.delete(self)
    db.session.commit()
  #//////////////////////////////////////////////////////////////////////////////////////////
  @classmethod
  def get(cls, id:int)->Union[User, None]:
    return cls.query.get(id)
  @classmethod
  def from_firebase_id(cls, firebase_id:str)->Union[User, None]:
    return cls.query.filter(cls.firebase_id == firebase_id).one_or_none()
  @classmethod
  def from_user_id(cls, user_id:str)->Union[User, None]:
    return cls.query.filter(cls.user_id == user_id).one_or_none()
  #//////////////////////////////////////////////////////////////////////////////////////////
  def info(self)->dict[str, Any]:
    keys = ('id', 'name', 'user_id', 'image', 'follows_num', 'followers_num')
    follow = db.aliased(_follow.Follow)
    follower = db.aliased(_follow.Follow)
    values = db.session.query(\
      self.__class__.id, \
      self.__class__.name, \
      self.__class__.user_id, \
      self.__class__.image, \
      db.func.count(follow.target), \
      db.func.count(follower.user), \
    ).filter(self.__class__.id == self.id \
    ).outerjoin(follow, self.__class__.id == follow.user \
    ).outerjoin(follower, self.__class__.id == follower.target \
    ).group_by(self.__class__.id).one()
    return dict(zip(keys, values))
  def is_available_user_id(self, user_id:str)->bool:
    try:
      self.user_id = user_id
      db.session.flush()
    except (exceptions.IntegrityError, exceptions.OperationalError):
      temp = False
    else:
      temp = True
    finally:
      db.session.rollback()
    return temp
  def follow(self, target:int):
    _follow.Follow.follow(self.id, target)
  def unfollow(self, target:int):
    _follow.Follow.unfollow(self.id, target)
  def get_follows(self)->list[dict[str, Any]]:
    return _follow.Follow.get_follows(self.id)
  def get_followers(self)->list[dict[str, Any]]:
    return _follow.Follow.get_followers(self.id)
  def get_talks(self)->list[dict[str, Any]]:
    return _talk.Member.get_talks(self.id)