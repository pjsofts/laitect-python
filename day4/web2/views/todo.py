#1. POST add todo(view, service)
#2. GET list todo(view, service)
#3. POST done todo(view, service)

from app import app
from services.todo import get_todos, add_todos, done_todos
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
    add_todos(title, user_id)
    return ""

@app.route("/todos/<id>/done", methods=["POST"])
def done_todo_view(id):
    done_todos(id)
    return ""
