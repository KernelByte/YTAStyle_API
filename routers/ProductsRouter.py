from datetime import date
from models.Products import Product as ProductsModel
from pydantic import BaseModel
from typing import Optional
from config.database import Session
from fastapi.responses import JSONResponse
from fastapi import APIRouter
from schemas.ProductSchema import Product as ProductSchema

products_router = APIRouter()


#Creacion de Roles
@products_router.post("/products", tags=['PRODUCTS'], response_model=dict, status_code=201) #, dependencies=[Depends(JWTBearer())] 
def create(product: ProductSchema) -> dict:
    db = Session()
    new_product = ProductsModel(**product.dict())
    db.add(new_product)
    db.commit()
    return JSONResponse(status_code=201, content={"message": "Producto creado correctamente!"}) #JSONResponse(content={"message":"Prueba de mensaje JSON"})