from __future__ import annotations
from typing import Any, Union
from . import db
from . import exceptions
from . import user as _user

class Follow(db.Model):
  __table_args__ = (db.CheckConstraint('user != target'), db.UniqueConstraint('user', 'target'))
  id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
  user = db.Column('user', db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)
  target = db.Column('target', db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)
  def __init__(self, user:int, target:int):
    self.user = user
    self.target = target
  def __repr__(self):
    return '<follow {} [{} -> {}>]'.format(self.id, self.user, self.target)
  #//////////////////////////////////////////////////////////////////////////////////////////
  @classmethod
  def follow(cls, user:int, target:int):
    temp = cls(user, target)
    db.session.add(temp)
    db.session.commit()
  @classmethod
  def unfollow(cls, user:int, target:int):
    temp = cls.get(user, target)
    db.session.delete(temp)
    db.session.commit()
  #//////////////////////////////////////////////////////////////////////////////////////////
  @classmethod
  def get(cls, user:int, target:int)->Union[Follow, None]:
    return cls.query.filter(cls.user==user, cls.target==target).one_or_none()
  #//////////////////////////////////////////////////////////////////////////////////////////
  @classmethod
  def get_follows(cls, user:int)->list[dict[str, Any]]:
    keys = ('id', 'name', 'user_id', 'image')
    values = db.session.query(_user.User.id, _user.User.name, _user.User.user_id, _user.User.image)\
      .filter(cls.user==user)\
      .join(cls, _user.User.id==cls.target)
    return list(map(lambda v: dict(zip(keys, v)), values))
  @classmethod
  def get_followers(cls, user:int)->list[dict[str, Any]]:
    keys = ('id', 'name', 'user_id', 'image')
    values = db.session.query(_user.User.id, _user.User.name, _user.User.user_id, _user.User.image)\
      .filter(cls.target==user)\
      .join(cls, _user.User.id==cls.user)
    return list(map(lambda v: dict(zip(keys, v)), values))
