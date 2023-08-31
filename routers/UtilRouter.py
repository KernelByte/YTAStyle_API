from fastapi import APIRouter
from schemas.AuthSchema import Auth as AuthSchema
from util.jwt_manager import create_token
from fastapi.responses import  JSONResponse
from fastapi.encoders import jsonable_encoder
from services.UserService import userService as userService
from config.database import Session
import bcrypt 

auth_router = APIRouter()

@auth_router.post("/login", tags=['AUTH'])
def login(data: AuthSchema):

    # Consultar si el mail existe en la base de datos
    #db = Session()
    #result = userService(db).get_user_email(data.mailUser)
    return JSONResponse(status_code=201, content={"message": "Usuario creado correctamente"})


    #if not result:
   #     return JSONResponse(status_code=404, content={"message":"Usuario o contraseña invalidos"})
   # else:
  #      pwd = result.passwordUser
  #      mail = bytes(data.passwordUser,'utf-8')
    
   #     if bcrypt.checkpw(mail,pwd):
  #          return JSONResponse(status_code=200, content={"message":"Usuario si encontrado"})
   #     else:
  #          return JSONResponse(status_code=404, content={"message":"Usuario o contraseña invalidos"})

    #if data.mailUser == "admin@gmail.com" and data.passwordUser == "12345":
    #    token: str = create_token(data.dict())
    #    return JSONResponse(content={"success":"true", "data": {"user":jsonable_encoder(data),"jwt":token}}, status_code=200)
    #return JSONResponse(status_code=404, content={"message": "Usuario o contraseña invalida"})