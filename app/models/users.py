from flask_login import UserMixin

from app import db, login_manager

from sqlalchemy import Column
from sqlalchemy.types import Integer, String, Text

class User(db.Model,UserMixin):

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    username = Column(String(64), index=True, unique=True, nullable=False)
    password_hash = Column(String(128), nullable=False)
    #TODO: Remove teamname column, hotfix
    teamname = Column(Text())
    teams = Column(Text(), nullable=True)

    def __repr__(self):
        output = "User: {}\n".format(self.username)
        teamlist = list(self.teams.split(','))
        for team in teamlist:
            output = output + "> {}\n".format(team)
        return output


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
