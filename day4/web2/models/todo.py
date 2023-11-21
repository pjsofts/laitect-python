from app import db
from sqlalchemy.dialects.postgresql import TEXT
from sqlalchemy.orm import relationship


class Todos(db.Model):
    __tablename__ = "todos"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(TEXT)
    done = db.Column(db.Boolean)
    users_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    users = relationship("Users", back_populates="todos")
