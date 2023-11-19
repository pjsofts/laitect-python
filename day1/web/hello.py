from flask import Flask, request

app = Flask(__name__)

users = [
    {"name": "pouria", "lastname": "jahandideh"},
    {"name": "ali", "lastname": "ahmadi"},
]

@app.route("/users")
def get_users():
    return users

@app.route("/users", methods=["POST"])
def add_user():
    data = request.get_json()
    # validate
    users.append({"name": data["name"], "lastname" : data["lastname"]})
    return "OK"
