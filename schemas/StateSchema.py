from pydantic import BaseModel
from typing import Optional

class State(BaseModel):
      idStatus: Optional[int] = None
      categoryStatus: str
      description: str

      model_config = {
            "json_schema_extra": {
                  "examples": [
                        {
                        
                        }
                  ]
            }
      }