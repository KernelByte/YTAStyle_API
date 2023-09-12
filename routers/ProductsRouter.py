from config.database import Session
from fastapi.responses import JSONResponse
from fastapi import APIRouter, File, UploadFile, Form
from schemas.ProductSchema import Product as ProductSchema
from fastapi.encoders import jsonable_encoder
from typing import  List
from services.ProductsService import ProductService
from schemas.ProductSchema import Product as ProductsSchema
#from util.upload_image import upload_file
from os import getcwd

products_router = APIRouter()
PATH_FILES = getcwd() + "/image/"

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
async def create(
    nameProduct: str = Form(...),
    dateProduct: str = Form(...),
    quantity: int = Form(...),
    priceCost: float = Form(0),
    priceBuy: float = Form(...),
    color: str = Form(""),
    productImage: UploadFile = File(None),
    idCategoryProduct: int = Form(None),
    idStatusProduct: int = Form(None),
    description: str = Form(""),
    barcode: str = Form("")) -> dict:

     with open(PATH_FILES + productImage.filename, "wb") as myfile:
         content = await productImage.read()
         myfile.write(content)
         myfile.close()

     nombre_imagen = productImage.filename
    #nombre_imagen =  await upload_file(productImage)

     new_product = ProductsSchema(
        nameProduct=nameProduct,
        dateProduct=dateProduct,
        quantity=quantity,
        priceCost=priceCost,
        priceBuy=priceBuy,
        color=color,
        productImage=nombre_imagen,
        idCategoryProduct=idCategoryProduct,
        idStatusProduct=idStatusProduct,
        description=description,
        barcode=barcode
    )

     db = Session()
     ProductService(db).create_product(new_product)
     return JSONResponse(status_code=201, content={"message": "Producto registrado"}) #JSONResponse(content={"message":"Prueba de mensaje JSON"})

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