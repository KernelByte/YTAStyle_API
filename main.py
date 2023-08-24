from fastapi import FastAPI, Query, HTTPException, Depends
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.security.http import HTTPAuthorizationCredentials
from pydantic import BaseModel, Field
from typing import Any, Coroutine, Optional, List

from starlette.requests import Request
from jwt_manager import create_token, validate_token
from fastapi.security import HTTPBearer


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

class User(BaseModel):
      email: str
      password: str

class Movie(BaseModel):
    id:int 
    title: str = Field(max_length=15, min_length=12, default="titleprueba")
    description: Optional[str] = 'Descripcion'

class JWTBearer(HTTPBearer):
      async def __call__(self, request: Request):
            auth = await super().__call__(request)
            data = validate_token(auth.credentials)
            if data['email'] != "admin@gmail.com":
                  raise HTTPException(status_code=403,detail="Credenciales invalidas")


@app.get("/", tags=['home'])
def message():
    return HTMLResponse('<h1>Hola Mundo</h1>')


@app.get("/movies", tags=['movies'], response_model=List[Movie], status_code=200, dependencies=[Depends(JWTBearer())]) 
def get_movies() -> List[Movie]:
    return JSONResponse(status_code=200, content=movies) #JSONResponse(content={"message":"Prueba de mensaje JSON"})

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