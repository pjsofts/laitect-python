from main import app
from main import users_collection
from pydantic import BaseModel 

class User(BaseModel):
    name: str
    lastname: str

@app.get("/users")
async def get_users():
    data = await users_collection.find({}).to_list(100)
    users = [{"name": user["name"], "lastname": user["lastname"]} for user in data]
    return users



@app.post("/users")
async def add_user(user: User):
    await users_collection.insert_one({"name":user.name,
     "lastname": user.lastname})
    return ""