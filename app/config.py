import os
import app.keys
basedir = os.path.abspath(os.path.dirname(__file__))
class Config(object):

    STATIC_FOLDER_PATH = basedir + '/static'
    DATABASE_FILENAME = basedir + '/app.db'


    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    USE_SENDGRID_API = False
    # Maybe want to remove a keys file all together...
    SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY") or app.keys.SENDGRID_API_KEY