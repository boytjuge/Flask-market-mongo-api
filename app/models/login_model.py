from app import mongo

def create_login_log(username, success):
    return mongo.db.logins.insert_one({
        'username': username,
        'success': success
    })
