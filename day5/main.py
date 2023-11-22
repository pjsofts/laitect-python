from typing import Union

from fastapi import FastAPI

import motor.motor_asyncio

app = FastAPI()


MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

db = client.flights

users_collection = db.get_collection("users")

from views import user