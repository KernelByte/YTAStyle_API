from fastapi import APIRouter
from schemas.AuthSchema import Auth as AuthSchema
from util.jwt_manager import create_token
from fastapi.responses import  JSONResponse
from fastapi.encoders import jsonable_encoder

auth_router = APIRouter()

@auth_router.post("/login", tags=['AUTH'])
def login(data: AuthSchema):
    if data.mailUser == "admin@gmail.com" and data.passwordUser == "12345":
        token: str = create_token(data.dict())
        return JSONResponse(content={"success":"true", "data": {"user":jsonable_encoder(data),"jwt":token}}, status_code=200)
    return JSONResponse(status_code=404, content={"message": "Usuario o contraseña invalida"})