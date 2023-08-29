from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from config.database import Session, Base, engine
from models.Business import Busine as BusineModel
from middlewares.error_handler import ErrorHandler
#from middlewares.jwt_bearer import JWTBearer
from routers.UserRouter import users_router
from routers.RolRouter import roles_router
from routers.BusineRouter import business_router
from routers.UtilRouter import auth_router


app = FastAPI()
app.title = "API - YTA Style"
app.version = "1.0"

app.add_middleware(ErrorHandler)
app.include_router(users_router)
app.include_router(roles_router)
app.include_router(business_router)
app.include_router(auth_router)

#Creacion de tablas
Base.metadata.create_all(bind=engine)
