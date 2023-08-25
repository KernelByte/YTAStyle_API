from fastapi import FastAPI, Query, HTTPException, Depends
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.security.http import HTTPAuthorizationCredentials
from pydantic import BaseModel, Field
from typing import Any, Coroutine, Optional, List

from starlette.requests import Request
from jwt_manager import create_token, validate_token
from fastapi.security import HTTPBearer

from config.database import Session, Base, engine
from models.Users import User as UserModel

movies = [{
    "id":1,
    "Titulo": "hombres de negro",
    "año": 2021
},
{
    "id":2,
    "Titulo": "avion gris",
    "año": 2021
}]


app = FastAPI()
app.title = "API - YTA Style"
app.version = "1.0"

#Creacion de tablas
Base.metadata.create_all(bind=engine)

class User(BaseModel):
      idUser: Optional[int] = None
      nameUser: str
      mailUser: str
      passwordUser: str
      idRoleUser: int
      tokenUser: str
      codeReference: str
      #profilePicture: bytes
      idBusinessUser: int





class JWTBearer(HTTPBearer):
      async def __call__(self, request: Request):
            auth = await super().__call__(request)
            data = validate_token(auth.credentials)
            if data['email'] != "admin@gmail.com":
                  raise HTTPException(status_code=403,detail="Credenciales invalidas")





#Creacion de usuario
@app.post("/users", tags=['User'], response_model=dict, status_code=201) #, dependencies=[Depends(JWTBearer())] 
def create_user(user: User) -> dict:
    db = Session()
    new_user = UserModel(**user.dict())
    db.add(new_user)
    db.commit()
    return JSONResponse(status_code=201, content={"message": "Usuario creado correctamente"}) #JSONResponse(content={"message":"Prueba de mensaje JSON"})




'''
class Movie(BaseModel):
    id:int 
    title: str = Field(max_length=15, min_length=12, default="titleprueba")
    description: Optional[str] = 'Descripcion'

@app.get("/", tags=['home'])
def message():
    return HTMLResponse('<h1>Hola Mundo</h1>')

@app.post('/movies',tags=['movies'])
def crear(movie: Movie):
        movies.append({
            "id":3,
            "Titulo": "Tiburon",
            "año": 2023
        })


@app.post('/moviesid',tags=['movies'])
def crear(Titulo: str = Query(min_length=5, max_length=15)):
        movies.append({
            "id":3,
            "Titulo": "Tiburon",
            "año": 2023
        })        

@app.post("/login", tags=['auth'])
def login(user: User):
    #if user.email == "admin@gmail.com" and user.password == "12345":
        token: str = create_token(user.dict())
        return JSONResponse(content=token, status_code=200)

'''