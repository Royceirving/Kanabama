import os
from app import db

def setup_database(database_name = 'app.db'):
    if(database_name not in os.listdir()):
        print("Creating database...")
        db.create_all()
        print("{} created!".format(database_name))
    else:
        print("Already found {}".format(database_name))

if __name__ == '__main__':
    setup_database()