from config.database import Session
from fastapi.responses import JSONResponse
from fastapi import APIRouter
from schemas.CategoriesSchema import Categori as CategoriesSchema
from fastapi.encoders import jsonable_encoder
from typing import  List
from services.CategoriesService import CategoryService

categories_router = APIRouter()

# CRUD CATEGORIES #########################################################################

# Search by category
@categories_router.get("/categories/", tags=['CATEGORIES'],response_model = CategoriesSchema )
def get(id: int) -> CategoriesSchema:
     db = Session()
     result = CategoryService(db).get_category(id)
     if not result:
          return JSONResponse(status_code=404, content={"message":"Categoria no encontrada"})
     return JSONResponse(status_code=200, content=jsonable_encoder(result))

# Search all categories
@categories_router.get("/categories", tags=['CATEGORIES'], response_model=List[CategoriesSchema], status_code=200)
def get_all() -> List[CategoriesSchema]:
     db = Session()
     result = CategoryService(db).get_all_categories()
     return JSONResponse(status_code=200, content=jsonable_encoder(result))

# Category creation
@categories_router.post("/categories", tags=['CATEGORIES'], response_model=dict, status_code=201) #, dependencies=[Depends(JWTBearer())] 
def create(category: CategoriesSchema) -> dict:
    db = Session()
    CategoryService(db).create_category(category)
    return JSONResponse(status_code=201, content={"message": "Categoria creada correctamente"}) #JSONResponse(content={"message":"Prueba de mensaje JSON"})

# Update Category
@categories_router.put("/categories/", tags=['CATEGORIES'], response_model=dict, status_code=200)
def update(id: int, category: CategoriesSchema) -> dict:
     db = Session()
     result = CategoryService(db).get_category(id)
     if not result:
          return JSONResponse(status_code=404, content={"message":"Categoria no encontrada"})
     CategoryService(db).update_category(id,category)
     return JSONResponse(status_code=200, content={"message":"Se ha modificado la Categoria"})

# Delete Category     
@categories_router.delete("/categories/", tags=['CATEGORIES'], response_model=dict, status_code=200)
def delete(id: int) -> dict:
     db = Session()
     result = CategoryService(db).get_category(id)
     if not result:
          return JSONResponse(status_code=404, content={"message":"Categoria no encontrada"})
     CategoryService(db).delete_category(id)
     return JSONResponse(status_code=200, content={"message":"Categoria eliminada"})

# ######################################################################################
