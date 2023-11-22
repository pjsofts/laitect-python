from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config[
    "SQLALCHEMY_DATABASE_URI"
] = f"postgresql://postgres:secret@localhost:5432/flights"

db = SQLAlchemy(app)

from views import user
from views import todo

from models import todo
from models import user

print("here")
