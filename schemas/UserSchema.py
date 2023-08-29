from pydantic import BaseModel
from typing import  Optional
from services.UserService import userService

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