from config.database import Session
from fastapi.responses import JSONResponse
from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from typing import  List
from schemas.BusinessSchema import Business as BusinessSchema
from services.BusinessService import BusinessService as businessService

business_router = APIRouter()

# CRUD BUSINESS #########################################################################

# Search by business
@business_router.get("/business/", tags=['BUSINESS'],response_model = BusinessSchema )
def get(id: int) -> BusinessSchema:
     db = Session()
     result = businessService(db).get_business(id)
     if not result:
          return JSONResponse(status_code=404, content={"message":"Negocio no encontrado"})
     return JSONResponse(status_code=200, content=jsonable_encoder(result))

# Search all business
@business_router.get("/business", tags=['BUSINESS'], response_model=List[BusinessSchema], status_code=200)
def get_all() -> List[BusinessSchema]:
     db = Session()
     result = businessService(db).get_all_business()
     return JSONResponse(status_code=200, content=jsonable_encoder(result))

# Business creation
@business_router.post("/business", tags=['BUSINESS'], response_model=dict, status_code=201) #, dependencies=[Depends(JWTBearer())] 
def create(business: BusinessSchema) -> dict:
    db = Session()
    businessService(db).create_business(business)
    return JSONResponse(status_code=201, content={"message": "Negocio creado correctamente"}) #JSONResponse(content={"message":"Prueba de mensaje JSON"})

# Update business
@business_router.put("/business/", tags=['BUSINESS'], response_model=dict, status_code=200)
def update(id: int, business: BusinessSchema) -> dict:
     db = Session()
     result = businessService(db).get_business(id)
     if not result:
          return JSONResponse(status_code=404, content={"message":"Negocio no encontrado"})
     businessService(db).update_business(id,business)
     return JSONResponse(status_code=200, content={"message":"Se ha modificado el Negocio"})

# Delete business     
@business_router.delete("/business/", tags=['BUSINESS'], response_model=dict, status_code=200)
def delete(id: int) -> dict:
     db = Session()
     result = businessService(db).get_business(id)
     if not result:
          return JSONResponse(status_code=404, content={"message":"Negocio no encontrado"})
     businessService(db).delete_business(id)
     return JSONResponse(status_code=200, content={"message":"Negocio eliminado"})

# ######################################################################################