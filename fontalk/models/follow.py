from . import db
from . import exceptions

class Follow(db.Model):
  __table_args__ = (db.CheckConstraint('user != target'), )
  id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
  user = db.Column('user', db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)
  target = db.Column('target', db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)
  def __init__(self, user, target):
    self.user = user
    self.target = target
  def __repr__(self):
    return '<follow {} [{} -> {}>]'.format(self.id, self.user, self.target)
  #//////////////////////////////////////////////////////////////////////////////////////////
  def delete(self):
    db.session.delete(self)
    db.session.commit()
  #//////////////////////////////////////////////////////////////////////////////////////////
  @classmethod
  def follow(cls, user, target):
    temp = cls(user.id, target.id)
    db.session.add(temp)
    db.session.commit()
  @classmethod
  def unfollow(cls, user, target):
    temp = cls.query.filter(cls.user == user.id, cls.target == target.id).one()
    temp.delete()
  @classmethod
  def get_follows(cls, user):
    temp = db.session.query(db.User.id, db.User.name, db.User.user_id, db.User.image)\
      .filter(cls.user == user.id)\
      .join(cls, db.User.id == cls.target)
    return temp
  @classmethod
  def get_followers(cls, user):
    temp = db.session.query(db.User.id, db.User.name, db.User.user_id, db.User.image)\
      .filter(cls.target == user.id)\
      .join(cls, db.User.id == cls.user)
    return temp
