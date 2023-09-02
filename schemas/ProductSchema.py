from pydantic import BaseModel
from typing import Optional
from datetime import date

class Product(BaseModel):
      idProduct: Optional[int] = None
      nameProduct: str
      dateProduct: str
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
                              "nameProduct" : "Corbata clasica",
                              "dateProduct" : "02/09/2023",
                              "quantity" : 1,
                              "priceCost" : 15000,
                              "idCategoryProduct" : None,
                              "idStatusProduct" : None,
                              "color" : "Rojo",
                              "description" : "Corbata de rayas diagonales",
                              "barcode" : None,
                        }
                  ]
            }
      }