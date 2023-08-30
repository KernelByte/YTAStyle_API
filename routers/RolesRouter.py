from models.Roles import Role as RolModel
from config.database import Session
from fastapi.responses import JSONResponse
from fastapi import APIRouter
from schemas.RoleSchema import Rol as RolesSchema

roles_router = APIRouter()


#Creacion de Roles
@roles_router.post("/roles", tags=['ROLES'], response_model=dict, status_code=201) #, dependencies=[Depends(JWTBearer())] 
def create(rol: RolesSchema) -> dict:
    db = Session()
    new_rol = RolModel(**rol.dict())
    db.add(new_rol)
    db.commit()
    return JSONResponse(status_code=201, content={"message": "Rol creado correctamente!"}) #JSONResponse(content={"message":"Prueba de mensaje JSON"})
