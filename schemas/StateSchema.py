from pydantic import BaseModel
from typing import Optional

class State(BaseModel):
      idStatus: Optional[int] = None
      categoryStatus: str
      description: str