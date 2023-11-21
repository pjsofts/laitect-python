from app import app
from services.user import get_users

@app.route("/users", methods=["GET"])
def index():
    users = get_users()
    return users
