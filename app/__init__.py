import sys, os
from app.config import Config
from flask import Flask, Blueprint
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
if(SENDGRID_API_KEY == None):
    from app.keys import SENDGRID_API_KEY as EMAIL_KEY
    SENDGRID_API_KEY = EMAIL_KEY


app = Flask(__name__)
csrf = CSRFProtect(app)
app.config.from_object(Config)
app.config["SECRET_KEY"] = "Some random key"
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.init_app(app)

from app.routes.index import index_bp
from app.routes.login import login_bp
from app.routes.logout import logout_bp
from app.routes.signup import signup_bp

app.register_blueprint(index_bp)
app.register_blueprint(login_bp)
app.register_blueprint(logout_bp)
app.register_blueprint(signup_bp)

if __name__ == "__main__":
    app.run(debug=True)