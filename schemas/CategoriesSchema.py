from pydantic import BaseModel
from typing import Optional

class Categori(BaseModel):
      
      idCategory: Optional[int] = None
      description: str