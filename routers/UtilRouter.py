from fastapi import APIRouter
from schemas.UserSchema import User as UserSchema
from util.jwt_manager import create_token
from fastapi.responses import  JSONResponse

auth_router = APIRouter()

@auth_router.post("/login", tags=['AUTH'])
def login(user: UserSchema):
    #if user.email == "admin@gmail.com" and user.password == "12345":
        token: str = create_token(user.dict())
        return JSONResponse(content=token, status_code=200)