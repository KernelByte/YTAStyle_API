from datetime import date
from models.Business import Busine as BusineModel
from pydantic import BaseModel
from typing import Optional
from config.database import Session
from fastapi.responses import JSONResponse
from fastapi import APIRouter

business_router = APIRouter()


class Busine(BaseModel):
    idBusiness : Optional[int] = None
    nameBusiness : str
    cellPhone : int
    Location : str
    schedule : date

#Creacion de Business
@business_router.post("/business", tags=['BUSINESS'], response_model=dict, status_code=201) #, dependencies=[Depends(JWTBearer())] 
def create(busine: Busine) -> dict:
    db = Session()
    new_busine = BusineModel(**busine.dict())
    db.add(new_busine)
    db.commit()
    return JSONResponse(status_code=201, content={"message": "Business creado correctamente!"}) #JSONResponse(content={"message":"Prueba de mensaje JSON"})

