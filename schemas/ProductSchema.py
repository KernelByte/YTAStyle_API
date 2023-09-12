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
      idCategoryProduct: Optional[int] = None
      idStatusProduct: Optional[int] = None
      color: str
      productImage: str
      description: str
      barcode: Optional[str] = None

      model_config = {
            "json_schema_extra": {
                  "examples": [
                        {
                              "nameProduct" : "Corbata clasica",
                              "dateProduct" : "02/09/2023",
                              "quantity" : 1,
                              "priceCost" : 15000,
                              "priceBuy" : 25000,
                              "idCategoryProduct" : 0,
                              "idStatusProduct" : 0,
                              "color" : "Rojo",
                              "productImage": None,
                              "description" : "Corbata de rayas diagonales",
                              "barcode" : None,
                        }
                  ]
            }
      }