from fastapi import APIRouter,BackgroundTasks
from schemas.AuthSchema import Auth as AuthSchema
from util.jwt_manager import create_token
from fastapi.responses import  JSONResponse
from fastapi.encoders import jsonable_encoder
from services.UserService import userService as userService
from config.database import Session
import bcrypt 
from schemas.UserSchema import User as UsersSchema
import datetime

auth_router = APIRouter()

'''
@auth_router.post("/login", tags=['AUTH'])
def login(mail: str, password: str) :
        # Consultar si el mail existe en la base de datos
        db = Session()
        result = userService(db).get_user_email(mail)

        if not result:
            return JSONResponse(content=None, status_code=200)
        else:
            pwd = result.passwordUser.encode('utf-8')
            pas = password.encode('utf-8')
    
            if bcrypt.checkpw(pas,pwd):
                token: str = create_token(jsonable_encoder(result))
                result.passwordUser = None
                return JSONResponse(content={"success":True, "data": {"user":jsonable_encoder(result),"jwt":token}}, status_code=200)
            else:
               return JSONResponse(content={"success":False, "data": {"user":{ "mailUser": None,"passwordUser": None,"idUser": None,"idRoleUser": None,"nameUser": None,"tokenUser": None,"idBusinessUser": None,"codeReference": None},"jwt":None}}, status_code=200)
'''

hora_actual = datetime.datetime.now()

@auth_router.post("/login", tags=['AUTH'])
def login(background_task : BackgroundTasks, data: AuthSchema):

    # Consultar si el mail existe en la base de datos
    db = Session()
    result = userService(db).get_user_email(data.mailUser)
    PAYLOAD: dict = {
        "sub": str(result.idUser),
        "role": "user",
        "iat": str(hora_actual.microsecond)
        }

    if not result:
        return JSONResponse(content={"success":False, "data": {"user":{ "mailUser": None,"passwordUser": None,"idUser": None,"idRoleUser": None,"nameUser": None,"tokenUser": None,"idBusinessUser": None,"codeReference": None},"jwt":None}}, status_code=200)
    else:
        pwd = result.passwordUser.encode('utf-8')
        pas = data.passwordUser.encode('utf-8')
    
        if bcrypt.checkpw(pas,pwd):
            token: str = create_token(PAYLOAD)
            result.tokenUser = token
            background_task.add_task(update_user,result.idUser,result)
            data.passwordUser = None
            return JSONResponse(content={"success":True, "data": {"user":jsonable_encoder(result),"jwt":token}}, status_code=200)
        else:
            return JSONResponse(content={"success":False, "data": {"user":{ "mailUser": None,"passwordUser": None,"idUser": None,"idRoleUser": None,"nameUser": None,"tokenUser": None,"idBusinessUser": None,"codeReference": None},"jwt":None}}, status_code=200)

def update_user(id: int, user: UsersSchema):
    db = Session()
    result = userService(db).get_user(id)
    if not result:
        return
    userService(db).update_user(id,user)
    return
