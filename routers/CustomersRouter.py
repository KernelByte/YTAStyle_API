from datetime import date
from models.Customers import Customer as CustomersModel
from pydantic import BaseModel
from typing import Optional
from config.database import Session
from fastapi.responses import JSONResponse
from fastapi import APIRouter
from schemas.CustomerSchema import Customer as CustomersSchema

customers_router = APIRouter()


#Creacion de Roles
@customers_router.post("/customers", tags=['CUSTOMERS'], response_model=dict, status_code=201) #, dependencies=[Depends(JWTBearer())] 
def create(customer: CustomersSchema) -> dict:
    db = Session()
    new_customer = CustomersModel(**customer.dict())
    db.add(new_customer)
    db.commit()
    return JSONResponse(status_code=201, content={"message": "Cliente creado correctamente!"}) #JSONResponse(content={"message":"Prueba de mensaje JSON"})