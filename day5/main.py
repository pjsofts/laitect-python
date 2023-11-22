from typing import Union

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import motor.motor_asyncio

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

db = client.flights

users_collection = db.get_collection("users")

from views import user