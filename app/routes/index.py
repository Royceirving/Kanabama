
from flask import Blueprint, render_template
from flask_login import current_user

index_bp = Blueprint('index',__name__,template_folder='templates')

@index_bp.route("/")
@index_bp.route("/index")
@index_bp.route("/home")
def index():
    return render_template('index.html',current_user=current_user)
