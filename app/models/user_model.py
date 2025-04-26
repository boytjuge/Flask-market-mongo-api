from app import mongo

def get_user_by_username(username):
    return mongo.db.users.find_one({'username': username})

def create_user(user_data):
    return mongo.db.users.insert_one(user_data)
