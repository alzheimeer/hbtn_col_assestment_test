from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from routes.user import user
from routes.order import order
from routes.shipping import shipping
from routes.payment import payment
from auth import AuthHandler
from pydantic import BaseModel

auth_handler = AuthHandler()


class AuthDetails(BaseModel):
    username: str
    password: str

app = FastAPI(
    title="Challenger Holberton API",
    description="API CRUD",
    version="0.1",
    openapi_tags=[{
        "name": "users",
        "description": "users routes"
    }]
)


@app.post('/register', status_code=201)
def register(auth_details: AuthDetails):
    if any(x['username'] == auth_details.username for x in users):
        raise HTTPException(status_code=400, detail='Username is taken')
    hashed_password = auth_handler.get_password_hash(auth_details.password)
    users.append({
        'username': auth_details.username,
        'password': hashed_password
    })
    return


@app.post('/login')
def login(auth_details: AuthDetails):
    user = None
    for x in users:
        if x['username'] == auth_details.username:
            user = x
            break

    if (user is None) or (not auth_handler.verify_password(auth_details.password, user['password'])):
        raise HTTPException(
            status_code=401, detail='Invalid username and/or password')
    token = auth_handler.encode_token(user['username'])
    return {'token': token}


app.include_router(payment)
app.include_router(user)
app.include_router(order)
app.include_router(shipping)
