import os
basedir = os.path.abspath(os.path.dirname(__file__))
class Config(object):

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    STATIC_FOLDER_PATH = basedir + '/static'
    DATABASE_FILENAME = 'app.db'