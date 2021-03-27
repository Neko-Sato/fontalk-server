from main import db

class User(db.Model):
  id = db.Column(db.Text, primary_key=True, nullable=False)
  name = db.Column(db.String(20))
  image = db.Column(db.LargeBinary)

  def __repr__(self):
    return '<User {}>'.format(self.id)

