from fastapi import FastAPI
from routes.user import user

app = FastAPI(
    title="Challenger Holberton API",
    description="API CRUD USERS",
    version="0.1",
    openapi_tags=[{
        "name": "users",
        "description": "users routes"
    }]
)

app.include_router(user)