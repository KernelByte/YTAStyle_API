from datetime import date
from models.Buys import Buy as BuysModel
from pydantic import BaseModel
from typing import Optional
from config.database import Session
from fastapi.responses import JSONResponse
from fastapi import APIRouter
from schemas.BuysSchema import Buy as BuysSchema

buys_router = APIRouter()


#Creacion de Buys
@buys_router.post("/buys", tags=['BUYS'], response_model=dict, status_code=201) #, dependencies=[Depends(JWTBearer())] 
def create(buy: BuysSchema) -> dict:
    db = Session()
    new_buy = BuysModel(**buy.dict())
    db.add(new_buy)
    db.commit()
    return JSONResponse(status_code=201, content={"message": "Venta creada correctamente!"}) #JSONResponse(content={"message":"Prueba de mensaje JSON"})

