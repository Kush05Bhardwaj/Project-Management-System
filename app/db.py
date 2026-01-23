from pymongo import MongoClient
from flask import current_app as app

client = None

def get_db():
    global client
    if not client:
        client = MongoClient(app.config['Mongo_URI'])
    return client.mini_pms