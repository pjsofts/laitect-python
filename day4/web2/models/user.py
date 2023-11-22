from app import db
from sqlalchemy.dialects.postgresql import TEXT
from sqlalchemy.orm import relationship


class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(TEXT)
    lastname = db.Column(TEXT)
    todos = relationship("Todos", back_populates="users")

    def __repr__(self):
        return self.name + " " + self.lastname
