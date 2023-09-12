from fastapi import APIRouter, UploadFile, File, BackgroundTasks
from schemas.AuthSchema import Auth as AuthSchema
from util.jwt_manager import create_token
from fastapi.responses import  JSONResponse
from fastapi.encoders import jsonable_encoder
from services.UserService import userService as userService
from config.database import Session
import bcrypt 
from os import getcwd
from PIL import Image


auth_router = APIRouter()

#IMAGEDIR = "images/"

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
def login(data: AuthSchema):

    # Consultar si el mail existe en la base de datos
    db = Session()
    result = userService(db).get_user_email(data.mailUser)

    if not result:
        return JSONResponse(status_code=404, content={"message":"Usuario o contraseña invalidos"})
    else:
        pwd = result.passwordUser.encode('utf-8')
        pas = data.passwordUser.encode('utf-8')
    
        if bcrypt.checkpw(pas,pwd):
            token: str = create_token(data.dict())
            data.passwordUser = None
            return JSONResponse(content={"success":"true", "data": {"user":jsonable_encoder(data),"jwt":token}}, status_code=200)
        else:
            return JSONResponse(status_code=404, content={"message":"Usuario o contraseña invalidos"})
            '''

@auth_router.post("/upload/image", tags=['UPLOAD'])
async def upload_file(background_task : BackgroundTasks,file:UploadFile = File(...)) :

    #SAVE FILE ORIGINAL
    with open(PATH_FILES + file.filename, "wb") as myfile:
        content = await file.read()
        myfile.write(content)
        myfile.close()
    
    background_task.add_task(resize_image,filename=file.filename)
    return JSONResponse(content={"message":"success"})



def resize_image(filename: str):
    sizes = [
        {
            "width": 640,
            "heigth": 480
        }
    ]

    for size in sizes:
      size_define = size["width"], size["heigth"]
      image = Image.open(PATH_FILES + filename, mode="r")
      image.thumbnail(size_define)
      image.save(PATH_FILES + str(size["heigth"])+"_"+filename)