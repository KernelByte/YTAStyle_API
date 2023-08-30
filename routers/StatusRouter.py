from models.Status import State as StateModel
from config.database import Session
from fastapi.responses import JSONResponse
from fastapi import APIRouter
from schemas.StateSchema import State as StateSchema

status_router = APIRouter()


#Creacion de State
@status_router.post("/status", tags=['STATUS'], response_model=dict, status_code=201) #, dependencies=[Depends(JWTBearer())] 
def create(state: StateSchema) -> dict:
    db = Session()
    new_state = StateModel(**state.dict())
    db.add(new_state)
    db.commit()
    return JSONResponse(status_code=201, content={"message": "Estado creado correctamente!"}) #JSONResponse(content={"message":"Prueba de mensaje JSON"})
