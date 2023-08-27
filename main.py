from datetime import date
from fastapi import FastAPI
from fastapi.responses import  JSONResponse
from pydantic import BaseModel
from typing import Optional
from config.database import Session, Base, engine
from models.Roles import Role as RolModel
from models.Business import Busine as BusineModel
from middlewares.error_handler import ErrorHandler
#from middlewares.jwt_bearer import JWTBearer
from routers.Users import user_router

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
app.include_router(user_router)

#Creacion de tablas
Base.metadata.create_all(bind=engine)



class Rol(BaseModel):
      idRole: Optional[int] = None
      description: str

class Busine(BaseModel):
    idBusiness : Optional[int] = None
    nameBusiness : str
    cellPhone : int
    Location : str
    schedule : date




#Creacion de Roles
@app.post("/roles", tags=['Roles'], response_model=dict, status_code=201) #, dependencies=[Depends(JWTBearer())] 
def create_rol(rol: Rol) -> dict:
    db = Session()
    new_rol = RolModel(**rol.dict())
    db.add(new_rol)
    db.commit()
    return JSONResponse(status_code=201, content={"message": "Rol creado correctamente!"}) #JSONResponse(content={"message":"Prueba de mensaje JSON"})



#Creacion de Business
@app.post("/business", tags=['Business'], response_model=dict, status_code=201) #, dependencies=[Depends(JWTBearer())] 
def create_busine(busine: Busine) -> dict:
    db = Session()
    new_busine = BusineModel(**busine.dict())
    db.add(new_busine)
    db.commit()
    return JSONResponse(status_code=201, content={"message": "Business creado correctamente!"}) #JSONResponse(content={"message":"Prueba de mensaje JSON"})



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