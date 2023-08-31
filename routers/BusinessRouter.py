from config.database import Session
from fastapi.responses import JSONResponse
from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from typing import  List
from schemas.BusinessSchema import Business as BusinessSchema

business_router = APIRouter()


# CRUD BUSINESS #########################################################################

# Search by rol
@business_router.get("/business/", tags=['BUSINESS'],response_model = BusinessSchema )
def get(id: int) -> BusinessSchema:
     db = Session()
     result = rolService(db).get_rol(id)
     if not result:
          return JSONResponse(status_code=404, content={"message":"Rol no encontrado"})
     return JSONResponse(status_code=200, content=jsonable_encoder(result))

# Search all roles
@business_router.get("/business", tags=['BUSINESS'], response_model=List[BusinessSchema], status_code=200)
def get_all() -> List[BusinessSchema]:
     db = Session()
     result = rolService(db).get_all_roles()
     return JSONResponse(status_code=200, content=jsonable_encoder(result))

# Rol creation
@business_router.post("/business", tags=['BUSINESS'], response_model=dict, status_code=201) #, dependencies=[Depends(JWTBearer())] 
def create(rol: BusinessSchema) -> dict:
    db = Session()
    rolService(db).create_rol(rol)
    return JSONResponse(status_code=201, content={"message": "Rol creado correctamente"}) #JSONResponse(content={"message":"Prueba de mensaje JSON"})

# Update Status
@business_router.put("/business/", tags=['BUSINESS'], response_model=dict, status_code=200)
def update(id: int, rol: BusinessSchema) -> dict:
     db = Session()
     result = rolService(db).get_rol(id)
     if not result:
          return JSONResponse(status_code=404, content={"message":"Rol no encontrado"})
     rolService(db).update_rol(id,rol)
     return JSONResponse(status_code=200, content={"message":"Se ha modificado el Rol"})

# Delete Status     
@business_router.delete("/business/", tags=['BUSINESS'], response_model=dict, status_code=200)
def delete(id: int) -> dict:
     db = Session()
     result = rolService(db).get_rol(id)
     if not result:
          return JSONResponse(status_code=404, content={"message":"Rol no encontrado"})
     rolService(db).delete_rol(id)
     return JSONResponse(status_code=200, content={"message":"Rol eliminado"})

#######################################################################################