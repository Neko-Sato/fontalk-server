from . import db

class User(db.Model):
  id = db.Column(db.VARCHAR(128), primary_key=True)
  name = db.Column(db.VARCHAR(20))
  image = db.Column(db.LargeBinary)
  def __repr__(self):
    return '<User {}>'.format(self.id)

class Talk(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.VARCHAR(20))
  def __repr__(self):
    return '<talk {}>'.format(self.id)

class Member(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  talk = db.relationship('talk')\?
  user = db.relationship('user')\?
  def __repr__(self):
    return '<member {}>'.format(self.id)

class Message(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  def __repr__(self):
    return '<message {}>'.format(self.id)
