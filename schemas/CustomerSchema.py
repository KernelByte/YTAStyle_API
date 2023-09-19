from pydantic import BaseModel
from typing import Optional
from datetime import date

class Customer(BaseModel):
      
      idCustomer: Optional[int] = None
      nameCustomer: str
      cellPhoneCustomer: int
      address: str
      email: str
      idBusinessCustomer: Optional[int] = None
      observation: str

      model_config = {
            "json_schema_extra": {
                  "examples": [
                        {
                        
                        }
                  ]
            }
      }