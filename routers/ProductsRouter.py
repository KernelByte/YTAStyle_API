from config.database import Session
from fastapi.responses import JSONResponse
from fastapi import APIRouter
from schemas.ProductSchema import Product as ProductSchema
from fastapi.encoders import jsonable_encoder
from typing import  List
from services.ProductsService import ProductService

products_router = APIRouter()


# CRUD PRODUCT #########################################################################

# Search by product
@products_router.get("/products/", tags=['PRODUCTS'],response_model = ProductSchema )
def get(id: int) -> ProductSchema:
     db = Session()
     result = ProductService(db).get_product(id)
     if not result:
          return JSONResponse(status_code=404, content={"message":"Producto no encontrado"})
     return JSONResponse(status_code=200, content=jsonable_encoder(result))

# Search all products
@products_router.get("/products", tags=['PRODUCTS'], response_model=List[ProductSchema], status_code=200)
def get_all() -> List[ProductSchema]:
     db = Session()
     result = ProductService(db).get_all_products()
     return JSONResponse(status_code=200, content=jsonable_encoder(result))

# Product creation
@products_router.post("/products", tags=['PRODUCTS'], response_model=dict, status_code=201) #, dependencies=[Depends(JWTBearer())] 
def create(product: ProductSchema) -> dict:
    db = Session()
    ProductService(db).create_product(product)
    return JSONResponse(status_code=201, content={"message": "Producto creado correctamente"}) #JSONResponse(content={"message":"Prueba de mensaje JSON"})

# Update product
@products_router.put("/products/", tags=['PRODUCTS'], response_model=dict, status_code=200)
def update(id: int, product: ProductSchema) -> dict:
     db = Session()
     result = ProductService(db).get_product(id)
     if not result:
          return JSONResponse(status_code=404, content={"message":"Producto no encontrado"})
     ProductService(db).update_product(id,product)
     return JSONResponse(status_code=200, content={"message":"Se ha modificado el Producto"})

# Delete product     
@products_router.delete("/products/", tags=['PRODUCTS'], response_model=dict, status_code=200)
def delete(id: int) -> dict:
     db = Session()
     result = ProductService(db).get_product(id)
     if not result:
          return JSONResponse(status_code=404, content={"message":"Producto no encontrado"})
     ProductService(db).delete_product(id)
     return JSONResponse(status_code=200, content={"message":"Producto eliminado"})

#######################################################################################