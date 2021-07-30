from typing import Optional
from pydantic import BaseModel

class Shipping(BaseModel):
              idShipping: Optional[str]
              address: str
              city: str
              state: str
              country: str
              cost: float