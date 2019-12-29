from flask_login import UserMixin

from app import db, login_manager

class User(db.Model,UserMixin):

    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    teams = db.Column(db.String(64),nullable=True)

    def __repr__(self):
        return '<User {} on team {}>'.format(self.username,self.teamname)    


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
