from pydantic import BaseModel
from typing import Optional

class Categories(BaseModel):
      
      idCategory: Optional[int] = None
      description: str