from . import db

class User(db.Model):
  __id = db.Column('id', db.VARCHAR(128), primary_key=True)
  __name = db.Column('name', db.VARCHAR(20), nullable=False)
  __image = db.Column('image', db.LargeBinary)
  __member = db.relationship("Member", backref="user", lazy=True)
  __message = db.relationship("Message", backref="user", lazy=True)
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
