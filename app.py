from fastapi import FastAPI
from routes.user import user
from routes.order import order
from routes.shipping import shipping
from routes.payment import payment

app = FastAPI(
    title="Challenger Holberton API",
    description="API CRUD",
    version="0.1",
    openapi_tags=[{
        "name": "users",
        "description": "users routes"
    }]
)

app.include_router(payment)
app.include_router(user)
app.include_router(order)
app.include_router(shipping)
