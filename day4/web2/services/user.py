from models.user import Users
from app import db

def get_users():
    users = Users.query.all()
    result = [{"name": user.name, "lastname": user.lastname} for user in users]
    return result

def add_user(name, lastname):
    user = Users(name=name, lastname=lastname)
    db.session.add(user)
    db.session.commit()
