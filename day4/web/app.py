from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://postgres:secret@localhost:5432/flights"

db = SQLAlchemy(app)

class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000))
    lastname = db.Column(db.String(6000))

@app.route("/users", methods=["GET"])
def index():
    users = Users.query.all()
    result = [{"name": user.name, "lastname": user.lastname} for user in users]
    return result


@app.route("/users", methods=["POST"])
def add_posts():
    data = request.get_json()
    name = data.get("name")
    lastname = data.get("lastname")
    user = Users(name=name, lastname=lastname)
    db.session.add(user)
    db.session.commit()
    return "OK"


if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # <--- create db object.
    app.run(debug=True)
