from app import db

from sqlalchemy import Column
from sqlalchemy.types import Integer, String, Text

class Teams(db.Model):
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(64), index=True, unique=True, nullable=False)
    password_hash = Column(String(128), nullable=False)
    users = Column(Text())

    def __repr__(self):
        return "<Teamname: {} | Users: {}".format(self.name,len(self.users.split(','))-1)