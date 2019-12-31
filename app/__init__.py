import sys, os
from app.config import Config
from flask import Flask, Blueprint
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
csrf = CSRFProtect(app)
app.config.from_object(Config)
app.config["SECRET_KEY"] = "Some random key"
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.init_app(app)

from app.models import users, teams

# TODO: Find a better way to do all of these dynamic blueprint imports
from app.routes.index import index_bp
from app.routes.login import login_bp
from app.routes.logout import logout_bp
from app.routes.signup import signup_bp
from app.routes.storyboard import storyboard_bp
from app.routes.deletestory import deletestory_bp
from app.routes.updatestory import updatestory_bp
from app.routes.newstory import newstory_bp

app.register_blueprint(index_bp)
app.register_blueprint(login_bp)
app.register_blueprint(logout_bp)
app.register_blueprint(signup_bp)
app.register_blueprint(storyboard_bp)
app.register_blueprint(deletestory_bp)
app.register_blueprint(updatestory_bp)
app.register_blueprint(newstory_bp)


if __name__ == "__main__":
    app.run(debug=True)