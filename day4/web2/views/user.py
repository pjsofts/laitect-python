from app import app
from services.user import get_users, add_user
from flask import request

@app.route("/users", methods=["GET"])
def index():
    users = get_users()
    return users


@app.route("/users", methods=["POST"])
def add_posts():
    data = request.get_json()
    name = data.get("name")
    lastname = data.get("lastname")
    add_user(name, lastname)
    return "OK"