from flask import Blueprint, render_template
from flask_login import logout_user, current_user, login_required
logout_bp = Blueprint('logout',__name__, template_folder='templates')

@logout_bp.route('/logout')
@login_required
def logout():
    logout_user()
    if(current_user.is_active):
        message = "Error logging out! Please try again."
    else:
        message = "Log out successful"
    return render_template('/logout.html',message=message)
