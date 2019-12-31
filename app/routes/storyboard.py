from flask import Blueprint, redirect, render_template
from flask_login import current_user

import sqlite3

from app.utils import get_stories_for_team
from app.config import Config
storyboard_bp = Blueprint('storyboard',__name__,template_folder='templates')


@storyboard_bp.route('/storyboard')
def storyboard():

    if( not current_user.is_active):
        return redirect("/index")

    conn = sqlite3.connect(Config.DATABASE_FILENAME)
    cursor = conn.cursor()

    resp = cursor.execute(get_stories_for_team(current_user.teamname))
    stories = resp.fetchall()
    outp = []
    for story in stories:
        temp = list(story)
        if(temp[3] == 0):
            temp[3] = "High"
        if(temp[3] == 1):
            temp[3] = "Medium"
        if(temp[3] == 2):
            temp[3] = "Low"
        outp.append(temp)
    stories = tuple(outp)
    return render_template('/storyboard.html', stories=stories)

