from schemas.user import User
from fastapi import APIRouter, Response, status
from config.db import conn
from models.user import users
from cryptography.fernet import Fernet
from starlette.status import HTTP_204_NO_CONTENT

# Generamos aleatorio unico
key = Fernet.generate_key()
# funcion para cifrar
f = Fernet(key)

user = APIRouter()


@user.get("/users", response_model=list[User], tags=["users"])
def get_users():
    return conn.execute(users.select()).fetchall()


@user.get("/users/{id}", response_model=User, tags=["users"])
def get_user(id: str):
    return conn.execute(users.select().where(users.c.id == id)).first()


@user.post("/users", response_model=User, tags=["users"])
def create_user(user: User):
    new_user = {
        "name": user.name, 
        "lastname": user.lastname,
        "email": user.email, 
        "company": user.company, 
        "gov_id": user.gov_id,
        "active": user.active}
    new_user["password"] = f.encrypt(user.password.encode("utf-8"))
    result = conn.execute(users.insert().values(new_user))
    # consultamos en la tabla por el id que acaba de generarse y lo retorna
    # y first es para que devuelva solo el primer resultado de la lista
    return conn.execute(users.select().where(users.c.id == result.lastrowid)).first()


@user.put("/users/{id}", response_model=User, tags=["users"])
def update_user(id: str, user: User):
    conn.execute(users.update().values(
        name=user.name,
        lastname=user.lastname,
        email=user.email,
        company=user.company,
        gov_id=user.gov_id,
        active=user.active,
        password=f.encrypt(user.password.encode("utf-8"))
    ).where(users.c.id == id))
    return conn.execute(users.select().where(users.c.id == id)).first()


@user.delete("/users/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["users"])
def delete_user(id: str):
    conn.execute(users.delete().where(users.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)
