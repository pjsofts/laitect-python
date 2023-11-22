#1. POST add todo(view, service)
#2. GET list todo(view, service)
#3. POST done todo(view, service)
from app import app
from services.todo import get_todos

@app.route("/todos", methods=["GET"])
def get_todos_view():
    todos = get_todos()
    return todos