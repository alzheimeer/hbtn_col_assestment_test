from schemas.order import Order
from fastapi import APIRouter, Response, status
from config.db import conn
from models.order import orders
from cryptography.fernet import Fernet
from starlette.status import HTTP_204_NO_CONTENT

# Generamos aleatorio unico
key = Fernet.generate_key()
# funcion para cifrar
f = Fernet(key)

order = APIRouter()


@order.get("/orders", response_model=list[Order], tags=["orders"])
def get_orders():
    return conn.execute(orders.select()).fetchall()


@order.get("/orders/{id}", response_model=Order, tags=["orders"])
def get_order(id: str):
    return conn.execute(orders.select().where(orders.c.id == id)).first()


@order.post("/orders", response_model=Order, tags=["orders"])
def create_order(order: Order):
    new_order = {
        "date": order.date, 
        "total": order.total,
        "subtotal": order.subtotal, 
        "taxes": order.taxes, 
        "paid": order.paid}
    result = conn.execute(orders.insert().values(new_order))
    # consultamos en la tabla por el id que acaba de generarse y lo retorna
    # y first es para que devuelva solo el primer resultado de la lista
    return conn.execute(orders.select().where(orders.c.id == result.lastrowid)).first()


@order.put("/orders/{id}", response_model=Order, tags=["orders"])
def update_order(id: str, order: Order):
    conn.execute(orders.update().values(
        date=order.date,
        total=order.total,
        subtotal=order.subtotal,
        taxes=order.taxes,
        paid=order.paid,
    ).where(orders.c.id == id))
    return conn.execute(orders.select().where(orders.c.id == id)).first()


@order.delete("/orders/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["orders"])
def delete_order(id: str):
    conn.execute(orders.delete().where(orders.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)
