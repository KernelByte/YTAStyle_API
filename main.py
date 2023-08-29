from fastapi import FastAPI
from config.database import Base, engine
from middlewares.error_handler import ErrorHandler
from routers.UserRouter import users_router
from routers.RolRouter import roles_router
from routers.BusineRouter import business_router
from routers.UtilRouter import auth_router


# APPLICATION DATA
app = FastAPI()
app.title = "API - YTA Style"
app.version = "0.0.1"

# MIDDLEWARE
app.add_middleware(ErrorHandler)

# ROUTERS
app.include_router(users_router)
app.include_router(roles_router)
app.include_router(business_router)
app.include_router(auth_router)

# CREATE TABLES
Base.metadata.create_all(bind=engine)
