#1. POST add todo(view, service)
#2. GET list todo(view, service)
#3. POST done todo(view, service)

from app import app
from services.todo import get_todos
from flask import request

@app.route("/todos", methods=["GET"])
def get_todos_view():
    todos = get_todos()
    return todos

@app.route("/todos", methods=["POST"])
def add_todo_view():
    data = request.get_json()
    title = data.get("title")
    user_id = data.get("user_id")
    add_todo(title, user_id)
    return ""