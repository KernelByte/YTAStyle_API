from fastapi import APIRouter
from fastapi.responses import JSONResponse
from typing import  List
from config.database import Session
from fastapi.encoders import jsonable_encoder
from services.UserService import userService
from schemas.UserSchema import User as UsersSchema
#from middlewares.jwt_bearer import JWTBearer

users_router = APIRouter()


# CRUD USER #########################################################################

# Search by user
@users_router.get("/users/", tags=['USERS'],response_model = UsersSchema )
def get(id: int) -> UsersSchema:
     db = Session()
     result = userService(db).get_user(id)
     if not result:
          return JSONResponse(status_code=404, content={"message":"Usuario no encontrado"})
     return JSONResponse(status_code=200, content=jsonable_encoder(result))

# Search all users
@users_router.get("/users", tags=['USERS'], response_model=List[UsersSchema], status_code=200)
def get_all() -> List[UsersSchema]:
     db = Session()
     result = userService(db).get_all_users()
     return JSONResponse(status_code=200, content=jsonable_encoder(result))

# User creation
@users_router.post("/users", tags=['USERS'], response_model=dict, status_code=201) #, dependencies=[Depends(JWTBearer())] 
def create(user: UsersSchema) -> dict:
    db = Session()
    userService(db).create_user(user)
    return JSONResponse(status_code=201, content={"message": "Usuario creado correctamente"}) #JSONResponse(content={"message":"Prueba de mensaje JSON"})

# Update Users
@users_router.put("/users/", tags=['USERS'], response_model=dict, status_code=200)
def update(id: int, user: UsersSchema) -> dict:
     db = Session()
     result = userService(db).get_user(id)
     if not result:
          return JSONResponse(status_code=404, content={"message":"Usuario no encontrado"})
     userService(db).update_user(id,user)
     return JSONResponse(status_code=200, content={"message":"Se ha modificado el usuario"})

# Delete Users     
@users_router.delete("/users/", tags=['USERS'], response_model=dict, status_code=200)
def delete(id: int) -> dict:
     db = Session()
     result = userService(db).get_user(id)
     if not result:
          return JSONResponse(status_code=404, content={"message":"Usuario no encontrado"})
     userService(db).delete_user(id)
     return JSONResponse(status_code=200, content={"message":"Usuario eliminado"})

#######################################################################################