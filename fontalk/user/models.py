from . import db

class User(db.Model):
  __id = db.Column('id', db.VARCHAR(128), primary_key=True)
  __name = db.Column('name', db.VARCHAR(20))
  __image = db.Column('image', db.LargeBinary)
  def __init__(self, id, name=None, image=None):
    self.__id = id
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
    return '<User {}>'.format(self.__id)

#class Talk(db.Model):
#  id = db.Column(db.Integer, primary_key=True)
#  name = db.Column(db.VARCHAR(20))
#  def __repr__(self):
#    return '<talk {}>'.format(self.id)

#class Member(db.Model):
#  id = db.Column(db.Integer, primary_key=True)
#  talk = db.relationship('talk')\?
#  user = db.relationship('user')\?
#  def __repr__(self):
#    return '<member {}>'.format(self.id)

#class Message(db.Model):
#  id = db.Column(db.Integer, primary_key=True)
#  def __repr__(self):
#    return '<message {}>'.format(self.id)
