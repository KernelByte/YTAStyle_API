from config.database import Session
from fastapi.responses import JSONResponse
from fastapi import APIRouter
from schemas.StateSchema import State as StatusSchema
from services.StatusService import stateService
from fastapi.encoders import jsonable_encoder
from typing import  List

status_router = APIRouter()

# CRUD STATE #########################################################################

# Search by state
@status_router.get("/status/", tags=['STATUS'],response_model = StatusSchema )
def get(id: int) -> StatusSchema:
     db = Session()
     result = stateService(db).get_state(id)
     if not result:
          return JSONResponse(status_code=404, content={"message":"Estado no encontrado"})
     return JSONResponse(status_code=200, content=jsonable_encoder(result))

# Search all status
@status_router.get("/status", tags=['STATUS'], response_model=List[StatusSchema], status_code=200)
def get_all() -> List[StatusSchema]:
     db = Session()
     result = stateService(db).get_all_status()
     return JSONResponse(status_code=200, content=jsonable_encoder(result))

# State creation
@status_router.post("/status", tags=['STATUS'], response_model=dict, status_code=201) #, dependencies=[Depends(JWTBearer())] 
def create(state: StatusSchema) -> dict:
    db = Session()
    stateService(db).create_state(state)
    return JSONResponse(status_code=201, content={"message": "Estado creado correctamente"}) #JSONResponse(content={"message":"Prueba de mensaje JSON"})

# Update Status
@status_router.put("/status/", tags=['STATUS'], response_model=dict, status_code=200)
def update(id: int, state: StatusSchema) -> dict:
     db = Session()
     result = stateService(db).get_state(id)
     if not result:
          return JSONResponse(status_code=404, content={"message":"Estado no encontrado"})
     stateService(db).update_state(id,state)
     return JSONResponse(status_code=200, content={"message":"Se ha modificado el estado"})

# Delete Status     
@status_router.delete("/status/", tags=['STATUS'], response_model=dict, status_code=200)
def delete(id: int) -> dict:
     db = Session()
     result = stateService(db).get_state(id)
     if not result:
          return JSONResponse(status_code=404, content={"message":"Estado no encontrado"})
     stateService(db).delete_state(id)
     return JSONResponse(status_code=200, content={"message":"Estado eliminado"})

#######################################################################################