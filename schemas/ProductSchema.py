from pydantic import BaseModel
from typing import Optional
from datetime import date

class Product(BaseModel):
      idProduct: Optional[int] = None
      nameProduct: str
      dateProduct: date
      quantity: int
      priceCost: float
      priceBuy:  float
      idCategoryProduct: int
      idStatusProduct: int
      color: str
      description: str
      barcode: str

      model_config = {
            "json_schema_extra": {
                  "examples": [
                        {
                        
                        }
                  ]
            }
      }