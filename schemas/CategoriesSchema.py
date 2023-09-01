from pydantic import BaseModel
from typing import Optional

class Categori(BaseModel):
      
      idCategory: Optional[int] = None
      description: str

      model_config = {
            "json_schema_extra": {
                  "examples": [
                        {
                        
                        }
                  ]
            }
      }