from models.Roles import Role as RolModel
from pydantic import BaseModel
from typing import Optional
from config.database import Session
from fastapi.responses import JSONResponse
from fastapi import APIRouter

roles_router = APIRouter()

class Rol(BaseModel):
      idRole: Optional[int] = None
      description: str

#Creacion de Roles
@roles_router.post("/roles", tags=['Roles'], response_model=dict, status_code=201) #, dependencies=[Depends(JWTBearer())] 
def create_rol(rol: Rol) -> dict:
    db = Session()
    new_rol = RolModel(**rol.dict())
    db.add(new_rol)
    db.commit()
    return JSONResponse(status_code=201, content={"message": "Rol creado correctamente!"}) #JSONResponse(content={"message":"Prueba de mensaje JSON"})
