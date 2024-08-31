from flask_pymongo import PyMongo

def get_user_model(mongo):
    return mongo.db.users

def get_event_model(mongo):
    return mongo.db.events
