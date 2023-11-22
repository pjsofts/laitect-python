from main import app
from main import users_collection

@app.get("/")
async def read_root():
    data = await users_collection.find_one({}) 
    print(data)  
    return {"name": data["name"]}