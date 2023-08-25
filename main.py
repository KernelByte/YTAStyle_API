from datetime import date
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
from models.Roles import Role as RolModel
from models.Business import Busine as BusineModel
from fastapi.encoders import jsonable_encoder

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
      idBusinessUser: Optional[int] = None

class Rol(BaseModel):
      idRole: Optional[int] = None
      description: str

class Busine(BaseModel):
    idBusiness : Optional[int] = None
    nameBusiness : str
    cellPhone : int
    Location : str
    schedule : date



class JWTBearer(HTTPBearer):
      async def __call__(self, request: Request):
            auth = await super().__call__(request)
            data = validate_token(auth.credentials)
            if data['email'] != "admin@gmail.com":
                  raise HTTPException(status_code=403,detail="Credenciales invalidas")




#CRUD USER #########################################################################

# User creation
@app.post("/users", tags=['Users'], response_model=dict, status_code=201) #, dependencies=[Depends(JWTBearer())] 
def create_user(user: User) -> dict:
    db = Session()
    new_user = UserModel(**user.dict())
    db.add(new_user)
    db.commit()
    return JSONResponse(status_code=201, content={"message": "Usuario creado correctamente"}) #JSONResponse(content={"message":"Prueba de mensaje JSON"})

# Search by user
@app.get("/users/", tags=['Users'],response_model = User )
def get_user(id: int) -> User:
     db = Session()
     result = db.query(UserModel).filter(UserModel.idUser == id).first()
     if not result:
          return JSONResponse(status_code=404, content={"message":"Usuario no encontrado"})
     return JSONResponse(status_code=200, content=jsonable_encoder(result))

# Search all users
@app.get("/users", tags=['Users'], response_model=List[User], status_code=200)
def get_all_user() -> List[User]:
     db = Session()
     result = db.query(UserModel).all()
     return JSONResponse(status_code=200, content=jsonable_encoder(result))

# Update Users
@app.put("/users/", tags=['Users'], response_model=dict, status_code=200)
def update_user(id: int, user: User) -> dict:
     db = Session()
     result = db.query(UserModel).filter(UserModel.idUser == id).first()
     if not result:
          return JSONResponse(status_code=404, content={"message":"Usuario no encontrado"})
     result.nameUser = user.nameUser
     result.mailUser = user.mailUser
     result.idBusinessUser = user.idBusinessUser
     db.commit()

# Delete Users     

     return JSONResponse(status_code=200, content={"message":"Se ha modificado el usuario"})





#######################################################################################




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