from models.user import Users

def get_users():
    users = Users.query.all()
    result = [{"name": user.name, "lastname": user.lastname} for user in users]
    return result