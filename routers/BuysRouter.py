from config.database import Session
from fastapi.responses import JSONResponse
from fastapi import APIRouter
from schemas.BuysSchema import Buy as BuysSchema
from fastapi.encoders import jsonable_encoder
from typing import  List
from services.BuysService import BuyService as buyService

buys_router = APIRouter()

# CRUD ROL #########################################################################

# Search by business
@buys_router.get("/buys/", tags=['BUYS'],response_model = BuysSchema )
def get(id: int) -> BuysSchema:
     db = Session()
     result = buyService(db).get_buy(id)
     if not result:
          return JSONResponse(status_code=404, content={"message":"Compra no encontrada"})
     return JSONResponse(status_code=200, content=jsonable_encoder(result))

# Search all business
@buys_router.get("/buys", tags=['BUYS'], response_model=List[BuysSchema], status_code=200)
def get_all() -> List[BuysSchema]:
     db = Session()
     result = buyService(db).get_all_buys()
     return JSONResponse(status_code=200, content=jsonable_encoder(result))

# Business creation
@buys_router.post("/buys", tags=['BUYS'], response_model=dict, status_code=201) #, dependencies=[Depends(JWTBearer())] 
def create(buy: BuysSchema) -> dict:
    db = Session()
    buyService(db).create_buy(buy)
    return JSONResponse(status_code=201, content={"message": "Compra creada correctamente"}) #JSONResponse(content={"message":"Prueba de mensaje JSON"})

# Update business
@buys_router.put("/buys/", tags=['BUYS'], response_model=dict, status_code=200)
def update(id: int, buy: BuysSchema) -> dict:
     db = Session()
     result = buyService(db).get_buy(id)
     if not result:
          return JSONResponse(status_code=404, content={"message":"Compra no encontrada"})
     buyService(db).update_buy(id,buy)
     return JSONResponse(status_code=200, content={"message":"Se ha modificado la Compra"})

# Delete business     
@buys_router.delete("/buys/", tags=['BUYS'], response_model=dict, status_code=200)
def delete(id: int) -> dict:
     db = Session()
     result = buyService(db).get_buy(id)
     if not result:
          return JSONResponse(status_code=404, content={"message":"Compra no encontrada"})
     buyService(db).delete_buy(id)
     return JSONResponse(status_code=200, content={"message":"Compra eliminada"})

#######################################################################################