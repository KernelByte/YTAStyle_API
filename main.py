from fastapi import FastAPI
from config.database import Base, engine
from middlewares.error_handler import ErrorHandler

# ROUTERS IMPORTS
from routers.UsersRouter import users_router
from routers.RolesRouter import roles_router
from routers.BusinessRouter import business_router
from routers.StatusRouter import status_router
from routers.ProductsRouter import products_router
from routers.CustomersRouter import customers_router
from routers.CategoriesRouter import categories_router
from routers.BuysRouter import buys_router
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
app.include_router(status_router)
app.include_router(products_router)
app.include_router(customers_router)
app.include_router(categories_router)
app.include_router(buys_router)

# CREATE TABLES
Base.metadata.create_all(bind=engine)
