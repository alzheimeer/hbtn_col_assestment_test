from typing import Optional
from pydantic import BaseModel

class Shipping(BaseModel):
              id: Optional[str]
              address: str
              city: str
              state: str
              country: str
              cost: float