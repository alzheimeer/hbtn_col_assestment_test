from fastapi import APIRouter
from config.db import conn
from models.user import users


user = APIRouter()

@user.get("/users")
def get_users():
    return conn.execute(users.select()).fetchall()

@user.get("/users/:id")
def helloworld():
    return "dd"
@user.post("/users")
def helloworld():
    return "dd"
@user.put("/users/:id")
def helloworld():
    return "dd"
@user.delete("/users/:id")
def helloworld():
    return "dd"