from . import db

#class Talk(db.Model):
#  id = db.Column(db.Integer, primary_key=True)
#  name = db.Column(db.VARCHAR(20))
#  def __repr__(self):
#    return '<talk {}>'.format(self.id)

#class Member(db.Model):
#  id = db.Column(db.Integer, primary_key=True)
#  talk = db.relationship('talk')
#  user = db.relationship('user')
#  def __repr__(self):
#    return '<member {}>'.format(self.id)

#class Message(db.Model):
#  id = db.Column(db.Integer, primary_key=True)
#  def __repr__(self):
#    return '<message {}>'.format(self.id)
