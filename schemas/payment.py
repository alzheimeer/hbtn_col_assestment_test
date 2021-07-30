from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class Payment(BaseModel):
              idPayments: Optional[str]
              type: str
              date: datetime
              txn_id: int
              total: float
              status: bool