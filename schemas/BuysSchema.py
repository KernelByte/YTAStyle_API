from pydantic import BaseModel
from typing import Optional
from datetime import date

class Buy(BaseModel):
      
      idBuy: Optional[int] = None
      idCategoryBuy: int
      priceUnitBuy: float
      priceBuyTotal: float
      dateBuy: date
      idPaymentStatus: int
      idCustomerBuy: int
      idBusinessBuy: Optional[int] = None
      discount: float
      TypeDiscount: str
      quantityBuy: int
      paymentType: str

      model_config = {
            "json_schema_extra": {
                  "examples": [
                        {
                        
                        }
                  ]
            }
      }