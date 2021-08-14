from __future__ import annotations
from typing import Any, Union
from . import db
from . import exceptions
from . import nodata
from . import user as _user
from datetime import datetime

class Talk(db.Model):
  id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
  name = db.Column('name', db.VARCHAR(20))
  image = db.Column('image', db.LargeBinary)
  member = db.relationship("Member", foreign_keys='Member.talk', cascade='delete')
  message = db.relationship("Message", foreign_keys='Message.talk', cascade='delete')
  def __init__(self, name:Union[str, None]=None, image:Union[bytes, None]=None):
    self.name = name
    self.image = image
  def __repr__(self):
    return '<talk {}>'.format(self.id)
  #//////////////////////////////////////////////////////////////////////////////////////////
  @classmethod
  def create(cls, user:int, name:Union[str, None]=None, image:Union[bytes, None]=None)->Talk:
    talk = cls(name, image)
    db.session.add(talk)
    db.session.flush()
    member = Member(talk.id, user, is_participated=True)
    db.session.add(member)
    db.session.commit()
    return talk
  @classmethod
  def update(self, user:int, name:Union[str, None, nodata]=nodata, image:Union[bytes, None, nodata]=nodata):
    Member.get(self.id, user).have_authority()
    if name is not nodata: self.name = name
    if image is not nodata: self.image = image
    db.session.commit()
  def delete(self, user:int):
    Member.get(self.id, user).have_authority()
    db.session.delete(self)
    db.session.commit()
  #//////////////////////////////////////////////////////////////////////////////////////////
  @classmethod
  def get(cls, id:int)->Union[Talk, None]:
    return cls.query.get(id)
  #//////////////////////////////////////////////////////////////////////////////////////////
  def get_members(self, user:int)->list[dict[str, Any]]:
    return Member.get_members(self.id, user)
  #//////////////////////////////////////////////////////////////////////////////////////////
  def info(self):
    keys = ('id', 'name', 'image', 'members_num')
    values = db.session.query(\
      self.__class__.id, \
      self.__class__.name, \
      self.__class__.image, \
      db.func.count(Member.id), \
    ).filter(\
      self.__class__.id==self.id, \
    ).outerjoin(Member, db.and_(\
      self.__class__.id==Member.talk,
      Member.is_participated\
    )).group_by(self.__class__.id).one()
    return dict(zip(keys, values))
  def add_members(self, user:int, targets:list[int]):
    Member.add_members(self.id, user, targets)
  def del_members(self, user:int, targets:list[int]):
    Member.del_members(self.id, user, targets)
  def participate(self, user:int):
    member = Member.get(self.id, user)
    member.participate()

class Member(db.Model):
  __table_args__ = (db.UniqueConstraint('talk', 'user'), )
  id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
  talk = db.Column('talk', db.Integer, db.ForeignKey('talk.id', ondelete="CASCADE"), nullable=False)
  user = db.Column('user', db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)
  is_participated = db.Column('is_participated', db.Boolean, nullable=False, default=False)
  def __init__(self, talk:int, user:int, is_participated:bool=False):
    self.talk = talk
    self.user = user
    self.is_participated = is_participated
  def __repr__(self):
    return '<Member {} [{}))){}]>'.format(self.id, self.talk, self.user)
  #//////////////////////////////////////////////////////////////////////////////////////////
  @classmethod
  def add_members(cls, talk:int, user:int, targets:list[int]):
    cls.get(talk, user).have_authority()
    members = [cls(talk, u) for u in targets]
    db.session.add_all(members)
    db.session.commit()
  @classmethod
  def del_members(cls, talk:int, user:int, targets:list[int]):
    cls.get(talk, user).have_authority()
    for u in targets:
      db.session.delete(cls.get(talk, u))
    db.session.commit()
  #//////////////////////////////////////////////////////////////////////////////////////////
  @classmethod
  def get(cls, talk:int, user:int)->Union[Member, None]:
    return cls.query.filter(cls.talk==talk, cls.user==user).one_or_none()
  #//////////////////////////////////////////////////////////////////////////////////////////
  @classmethod
  def get_talks(cls, user:int)->list[dict[str, Any]]:
    keys = ('id', 'name', 'image')
    values = db.session.query(Talk.id, Talk.name, Talk.image)\
      .filter(cls.user==user)\
      .join(cls, cls.talk==Talk.id)
    return list(map(lambda v: dict(zip(keys, v)), values))
  @classmethod
  def get_members(cls, talk:int, user:int)->list[dict[str, Any]]:
    cls.get(talk, user).have_authority()
    keys = ('id', 'name', 'user_id', 'image')
    values = db.session.query(_user.User.id, _user.User.name, _user.User.user_id, _user.User.image)\
      .filter(cls.talk==talk)\
      .join(cls, cls.user==_user.User.id)
    return list(map(lambda v: dict(zip(keys, v)), values))
  #//////////////////////////////////////////////////////////////////////////////////////////
  def participate(self):
    self.is_participated = True
    db.session.commit()
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
