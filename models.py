from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


class User():
  pass
  
  def __repr__(self):
        return '<User {}>'.format(self.username)


class Post():
    #id = db.Column(db.Integer, primary_key=True)
    #city = db.Column(db.String(140))
    #country = db.Column(db.String(140))
    #description = db.Column(db.String(140))
    #timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    #user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.description)