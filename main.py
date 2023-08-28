from fastapi import FastAPI
from fastapi.responses import  JSONResponse
from pydantic import BaseModel
from typing import Optional
from config.database import Session, Base, engine
from models.Business import Busine as BusineModel
from middlewares.error_handler import ErrorHandler
#from middlewares.jwt_bearer import JWTBearer
from routers.UserRouter import users_router
from routers.RolRouter import roles_router
from routers.BusineRouter import business_router

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

app.add_middleware(ErrorHandler)
app.include_router(users_router)
app.include_router(roles_router)
app.include_router(business_router)

#Creacion de tablas
Base.metadata.create_all(bind=engine)

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