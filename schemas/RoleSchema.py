from pydantic import BaseModel
from typing import Optional

class Rol(BaseModel):
      idRole: Optional[int] = None
      description: str


      model_config = {
            "json_schema_extra": {
                  "examples": [
                        {
                        "description": None
                        }
                  ]
            }
      }