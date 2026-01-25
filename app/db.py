from flask import current_app, g
from pymongo import MongoClient

def get_db():
    if 'db' not in g:
        client = MongoClient(current_app.config['MONGO_URI'])
        g.db = client.get_database()  # This gets the database from the connection string
    return g.db

# Add helper functions to the database object
def get_user_by_email(email):
    db = get_db()
    return db.users.find_one({"email": email})