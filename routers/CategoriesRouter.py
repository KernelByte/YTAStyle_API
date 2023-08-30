from datetime import date
from models.Categories import Category as CategoriesModel
from pydantic import BaseModel
from typing import Optional
from config.database import Session
from fastapi.responses import JSONResponse
from fastapi import APIRouter
from schemas.CategoriesSchema import Categori as CategoriesSchema

categories_router = APIRouter()


#Creacion de Business
@categories_router.post("/categories", tags=['CATEGORIES'], response_model=dict, status_code=201) #, dependencies=[Depends(JWTBearer())] 
def create(category: CategoriesSchema) -> dict:
    db = Session()
    new_category = CategoriesModel(**category.dict())
    db.add(new_category)
    db.commit()
    return JSONResponse(status_code=201, content={"message": "Categoria creada correctamente!"}) #JSONResponse(content={"message":"Prueba de mensaje JSON"})

