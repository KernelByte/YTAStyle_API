from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import  Optional, List
from config.database import Session
from models.Users import User as UserModel
from fastapi.encoders import jsonable_encoder
#from middlewares.jwt_bearer import JWTBearer

users_router = APIRouter()

class User(BaseModel):
      idUser: Optional[int] = None
      nameUser: str
      mailUser: str
      passwordUser: str
      idRoleUser: int
      tokenUser: str
      codeReference: str
      #profilePicture: bytes
      idBusinessUser: Optional[int] = None

#CRUD USER #########################################################################

# User creation
@users_router.post("/users", tags=['Users'], response_model=dict, status_code=201) #, dependencies=[Depends(JWTBearer())] 
def create_user(user: User) -> dict:
    db = Session()
    new_user = UserModel(**user.dict())
    db.add(new_user)
    db.commit()
    return JSONResponse(status_code=201, content={"message": "Usuario creado correctamente"}) #JSONResponse(content={"message":"Prueba de mensaje JSON"})

# Search by user
@users_router.get("/users/", tags=['Users'],response_model = User )
def get_user(id: int) -> User:
     db = Session()
     result = db.query(UserModel).filter(UserModel.idUser == id).first()
     if not result:
          return JSONResponse(status_code=404, content={"message":"Usuario no encontrado"})
     return JSONResponse(status_code=200, content=jsonable_encoder(result))

# Search all users
@users_router.get("/users", tags=['Users'], response_model=List[User], status_code=200)
def get_all_user() -> List[User]:
     db = Session()
     result = db.query(UserModel).all()
     return JSONResponse(status_code=200, content=jsonable_encoder(result))

# Update Users
@users_router.put("/users/", tags=['Users'], response_model=dict, status_code=200)
def update_user(id: int, user: User) -> dict:
     db = Session()
     result = db.query(UserModel).filter(UserModel.idUser == id).first()
     if not result:
          return JSONResponse(status_code=404, content={"message":"Usuario no encontrado"})
     result.nameUser = user.nameUser
     result.mailUser = user.mailUser
     result.idBusinessUser = user.idBusinessUser
     db.commit()
     return JSONResponse(status_code=200, content={"message":"Se ha modificado el usuario"})

# Delete Users     
@users_router.delete("/users/", tags=['Users'], response_model=dict, status_code=200)
def delete_user(id: int) -> dict:
     db = Session()
     result = db.query(UserModel).filter(UserModel.idUser == id).first()
     if not result:
          return JSONResponse(status_code=404, content={"message":"Usuario no encontrado"})
     db.delete(result)
     db.commit()
     return JSONResponse(status_code=200, content={"message":"Usuario eliminado"})

#######################################################################################