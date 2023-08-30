from pydantic import BaseModel
from typing import Optional
from datetime import date

class Business(BaseModel):

      idBusiness: Optional[int] = None
      nameBusiness: str
      cellPhone: int
      Location: str
      schedule: date