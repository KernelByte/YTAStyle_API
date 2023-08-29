from fastapi import APIRouter
from fastapi.responses import JSONResponse
from typing import  List
from config.database import Session
from models.Users import User as UserModel
from fastapi.encoders import jsonable_encoder
#from middlewares.jwt_bearer import JWTBearer
from services.UserService import userService
from schemas.UserSchema import User as UserSchema

users_router = APIRouter()



#CRUD USER #########################################################################

# User creation
@users_router.post("/users", tags=['Users'], response_model=dict, status_code=201) #, dependencies=[Depends(JWTBearer())] 
def create_user(user: UserSchema) -> dict:
    db = Session()
    userService(db).create_user(user)
    return JSONResponse(status_code=201, content={"message": "Usuario creado correctamente"}) #JSONResponse(content={"message":"Prueba de mensaje JSON"})

# Search by user
@users_router.get("/users/", tags=['Users'],response_model = UserSchema )
def get_user(id: int) -> UserSchema:
     db = Session()
     result = userService(db).get_user(id)
     if not result:
          return JSONResponse(status_code=404, content={"message":"Usuario no encontrado"})
     return JSONResponse(status_code=200, content=jsonable_encoder(result))

# Search all users
@users_router.get("/users", tags=['Users'], response_model=List[UserSchema], status_code=200)
def get_all_user() -> List[UserSchema]:
     db = Session()
     result = userService(db).get_all_users()
     return JSONResponse(status_code=200, content=jsonable_encoder(result))

# Update Users
@users_router.put("/users/", tags=['Users'], response_model=dict, status_code=200)
def update_user(id: int, user: UserSchema) -> dict:
     db = Session()
     result = userService(db).get_user(id)
     if not result:
          return JSONResponse(status_code=404, content={"message":"Usuario no encontrado"})
     userService(db).update_user(id,user)
     return JSONResponse(status_code=200, content={"message":"Se ha modificado el usuario"})

# Delete Users     
@users_router.delete("/users/", tags=['Users'], response_model=dict, status_code=200)
def delete_user(id: int) -> dict:
     db = Session()
     result = userService(db).get_user(id)
     if not result:
          return JSONResponse(status_code=404, content={"message":"Usuario no encontrado"})
     userService(db).delete_user(id)
     return JSONResponse(status_code=200, content={"message":"Usuario eliminado"})

#######################################################################################