from schemas.shipping import Shipping
from fastapi import APIRouter, Response, status
from config.db import conn
from models.shipping import shippings
from cryptography.fernet import Fernet
from starlette.status import HTTP_204_NO_CONTENT

# Generamos aleatorio unico
key = Fernet.generate_key()
# funcion para cifrar
f = Fernet(key)

shipping = APIRouter()


@shipping.get("/shippings", response_model=list[Shipping], tags=["shippings"])
def get_shippings():
    return conn.execute(shippings.select()).fetchall()


@shipping.get("/shippings/{id}", response_model=Shipping, tags=["shippings"])
def get_shipping(id: str):
    return conn.execute(shippings.select().where(shippings.c.id == id)).first()


@shipping.post("/shippings", response_model=Shipping, tags=["shippings"])
def create_shipping(shipping: Shipping):
    new_shipping = {
        "address": shipping.address, 
        "city": shipping.city,
        "state": shipping.state, 
        "country": shipping.country, 
        "cost": shipping.cost}
    result = conn.execute(shippings.insert().values(new_shipping))
    # consultamos en la tabla por el id que acaba de generarse y lo retorna
    # y first es para que devuelva solo el primer resultado de la lista
    return conn.execute(shippings.select().where(shippings.c.id == result.lastrowid)).first()


@shipping.put("/shippings/{id}", response_model=Shipping, tags=["shippings"])
def update_shipping(id: str, shipping: Shipping):
    conn.execute(shippings.update().values(
        address=shipping.address,
        city=shipping.city,
        state=shipping.state,
        country=shipping.country,
        cost=shipping.cost,
    ).where(shippings.c.id == id))
    return conn.execute(shippings.select().where(shippings.c.id == id)).first()


@shipping.delete("/shippings/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["shippings"])
def delete_shipping(id: str):
    conn.execute(shippings.delete().where(shippings.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)
