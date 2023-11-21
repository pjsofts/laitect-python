from app import db
from sqlalchemy.dialects.postgresql import TEXT


class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(TEXT)
    lastname = db.Column(TEXT)
