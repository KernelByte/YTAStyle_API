from datetime import date
from models.Categories import Category as CategoriesModel
from pydantic import BaseModel
from typing import Optional
from config.database import Session
from fastapi.responses import JSONResponse
from fastapi import APIRouter
from schemas.CategoriesSchema import Categori as CategoriesSchema
from fastapi.encoders import jsonable_encoder
from typing import  List

categories_router = APIRouter()


#Creacion de Business
@categories_router.post("/categories", tags=['CATEGORIES'], response_model=dict, status_code=201) #, dependencies=[Depends(JWTBearer())] 
def create(category: CategoriesSchema) -> dict:
    db = Session()
    new_category = CategoriesModel(**category.dict())
    db.add(new_category)
    db.commit()
    return JSONResponse(status_code=201, content={"message": "Categoria creada correctamente!"}) #JSONResponse(content={"message":"Prueba de mensaje JSON"})

# CRUD ROL #########################################################################

# Search by rol
@roles_router.get("/roles/", tags=['ROLES'],response_model = RolesSchema )
def get(id: int) -> RolesSchema:
     db = Session()
     result = rolService(db).get_rol(id)
     if not result:
          return JSONResponse(status_code=404, content={"message":"Rol no encontrado"})
     return JSONResponse(status_code=200, content=jsonable_encoder(result))

# Search all roles
@roles_router.get("/roles", tags=['ROLES'], response_model=List[RolesSchema], status_code=200)
def get_all() -> List[RolesSchema]:
     db = Session()
     result = rolService(db).get_all_roles()
     return JSONResponse(status_code=200, content=jsonable_encoder(result))

# Rol creation
@roles_router.post("/roles", tags=['ROLES'], response_model=dict, status_code=201) #, dependencies=[Depends(JWTBearer())] 
def create(rol: RolesSchema) -> dict:
    db = Session()
    rolService(db).create_rol(rol)
    return JSONResponse(status_code=201, content={"message": "Rol creado correctamente"}) #JSONResponse(content={"message":"Prueba de mensaje JSON"})

# Update Status
@roles_router.put("/roles/", tags=['ROLES'], response_model=dict, status_code=200)
def update(id: int, rol: RolesSchema) -> dict:
     db = Session()
     result = rolService(db).get_rol(id)
     if not result:
          return JSONResponse(status_code=404, content={"message":"Rol no encontrado"})
     rolService(db).update_rol(id,rol)
     return JSONResponse(status_code=200, content={"message":"Se ha modificado el Rol"})

# Delete Status     
@roles_router.delete("/roles/", tags=['ROLES'], response_model=dict, status_code=200)
def delete(id: int) -> dict:
     db = Session()
     result = rolService(db).get_rol(id)
     if not result:
          return JSONResponse(status_code=404, content={"message":"Rol no encontrado"})
     rolService(db).delete_rol(id)
     return JSONResponse(status_code=200, content={"message":"Rol eliminado"})

#######################################################################################
