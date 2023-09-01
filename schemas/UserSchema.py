from pydantic import BaseModel
from typing import  Optional

class User(BaseModel):
      idUser: Optional[int] = None
      nameUser: str
      mailUser: str
      passwordUser: str
      idRoleUser: int
      tokenUser: str
      codeReference: str
      #profilePicture: bytes
      idBusinessUser: Optional[int] = None

      model_config = {
            "json_schema_extra": {
                  "examples": [
                        {
                        "nameUser": "Oscar Lopez",
                        "mailUser": "oca2394@gmail.com",
                        "passwordUser": "12345",
                        "idRoleUser": None,
                        "tokenUser": None,
                        "codeReference": None,
                        #profilePicture: bytes
                        "idBusinessUser": 1,
                        }
                  ]
            }
      }