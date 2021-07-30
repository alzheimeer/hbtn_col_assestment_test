from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    id: Optional[str]
    name: str
    lastname: str
    email: str
    password: str
    gov_id: int
    company: str
    active: bool