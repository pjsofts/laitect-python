from models.todo import Todos
from app import db


def get_todos():
    todos = Todos.query.all()
    result = [
        {"title": todo.title, "done": todo.done, 
        "user_id": todo.users.id, "user_name": todo.users.name, 
        "user_lastname": todo.users.lastname}
        for todo in todos
    ]
    return result
