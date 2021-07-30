from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class Order(BaseModel):
              idOrder: Optional[str]
              date: datetime
              total: float
              subtotal: float
              taxes: float
              paid: float