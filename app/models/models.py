from app import db, login_manager
from flask_login import UserMixin, login_user, login_required
from flask_sqlalchemy import SQLAlchemy



class StoryBoard:
    pass

class Story:

    def __init__(self, name,description="",priority=0,date="01-01-1970"):
        self.name = name
        self.description = description
        self.priority = priority
        self.date = date
