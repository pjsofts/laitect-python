from models.todo import Todos
from models.user import Users
from app import db


def get_todos():
    todos = Todos.query.all()
    result = [
        {
            "id": todo.id,
            "title": todo.title, "done": todo.done, 
        "user_id": todo.users.id,
         "user_name": todo.users.name, 
        "user_lastname": todo.users.lastname}
        for todo in todos
    ]
    return result

def add_todos(title, user_id):
    user = Users.query.get(user_id)
    todo = Todos(title = title, done=False,
     users_id=user.id)
    db.session.add(todo)
    db.session.commit()

def done_todos(id):
    todo = Todos.query.get(id)
    todo.done = True
    db.session.add(todo)
    db.session.commit()