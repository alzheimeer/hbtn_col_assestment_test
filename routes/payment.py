from schemas.payment import Payment
from fastapi import APIRouter, Response, status
from config.db import conn
from models.payment import payments
from cryptography.fernet import Fernet
from starlette.status import HTTP_204_NO_CONTENT

# Generamos aleatorio unico
key = Fernet.generate_key()
# funcion para cifrar
f = Fernet(key)

payment = APIRouter()


@payment.get("/payments", response_model=list[Payment], tags=["payments"])
def get_payments():
    return conn.execute(payments.select()).fetchall()


@payment.get("/payments/{id}", response_model=Payment, tags=["payments"])
def get_payment(id: str):
    return conn.execute(payments.select().where(payments.c.id == id)).first()


@payment.post("/payments", response_model=Payment, tags=["payments"])
def create_payment(payment: Payment):
    new_payment = {
        "type": payment.type, 
        "date": payment.date,
        "txn_id": payment.txn_id, 
        "total": payment.total, 
        "status": payment.status}
    
    result = conn.execute(payments.insert().values(new_payment))
    # consultamos en la tabla por el id que acaba de generarse y lo retorna
    # y first es para que devuelva solo el primer resultado de la lista
    return conn.execute(payments.select().where(payments.c.id == result.lastrowid)).first()


@payment.put("/payments/{id}", response_model=Payment, tags=["payments"])
def update_payment(id: str, payment: Payment):
    conn.execute(payments.update().values(
        type=payment.type,
        date=payment.date,
        txn_id=payment.txn_id,
        total=payment.total,
        status=payment.status,
    ).where(payments.c.id == id))
    return conn.execute(payments.select().where(payments.c.id == id)).first()


@payment.delete("/payments/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["payments"])
def delete_payment(id: str):
    conn.execute(payments.delete().where(payments.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)
