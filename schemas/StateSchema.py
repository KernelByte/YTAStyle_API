from pydantic import BaseModel
from typing import Optional

class State(BaseModel):
      idStatus: Optional[int] = None
      categoryStatus: str
      idBussinesState: Optional[int] = None
      description: str

      model_config = {
            "json_schema_extra": {
                  "examples": [
                        {
                        
                        }
                  ]
            }
      }