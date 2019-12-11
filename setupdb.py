import os
from app import db
if('app.db' not in os.listdir()):
    print("Creating database...")
    db.create_all()
    print("Database created!")
else:
    print("Already found app.db")