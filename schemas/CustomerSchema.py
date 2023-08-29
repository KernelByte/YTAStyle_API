from pydantic import BaseModel
from typing import Optional
from datetime import date

class Customer(BaseModel):
      
      idCustomer: Optional[int] = None
      nameCustomer: str
      cellPhoneCustomer: int
      address: str
      email: str
      observation: str