from pydantic import BaseModel
from typing import  Optional

class User(BaseModel):
      idUser: Optional[int] = None
      nameUser: str
      mailUser: str
      passwordUser: str
      idRoleUser: Optional[int] = None
      tokenUser: Optional[str] = None
      codeReference: Optional[str] = None
      #profilePicture: bytes
      idBusinessUser: Optional[int] = None

      model_config = {
            "json_schema_extra": {
                  "examples": [
                        {
                        "nameUser": "Oscar Lopez",
                        "mailUser": "oca2394@gmail.com",
                        "passwordUser": "12345"
                        }
                  ]
            }
      }