from pydantic import BaseModel
from typing import Optional

class Auth(BaseModel):

      mailUser: str
      passwordUser: str