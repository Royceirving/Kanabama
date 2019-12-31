from flask import Blueprint
from flask_login import current_user
from app.utils import delete_story_in_team_generator
from app.config import Config, basedir


import json
import sqlite3

deletestory_bp = Blueprint('deletestory',__name__,template_folder='templates',root_path=basedir)

@deletestory_bp.route('/deletestory/<story_id>',methods=["POST","GET"])
def deletestory(story_id):
    try:

        conn = sqlite3.connect(Config.DATABASE_FILENAME)
        cursor = conn.cursor()

        query = delete_story_in_team_generator(current_user.teamname,story_id)
        resp = cursor.execute(query)
        resp = resp.fetchall()
        conn.commit()
        return json.dumps({'succecss':True}),200,{'ContentType':'application/json'}
    except BaseException:
        return json.dumps({'fail':False}),500,{'ContentType':'application/json'}
     