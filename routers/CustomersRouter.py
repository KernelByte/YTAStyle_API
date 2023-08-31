from config.database import Session
from fastapi.responses import JSONResponse
from fastapi import APIRouter
from schemas.CustomerSchema import Customer as CustomersSchema
from fastapi.encoders import jsonable_encoder
from typing import  List
from services.CustomersService import CustomerService

customers_router = APIRouter()

# CRUD CUSTOMER #########################################################################

# Search by customer
@customers_router.get("/customers/", tags=['CUSTOMERS'],response_model = CustomersSchema )
def get(id: int) -> CustomersSchema:
     db = Session()
     result = CustomerService(db).get_customer(id)
     if not result:
          return JSONResponse(status_code=404, content={"message":"Cliente no encontrado"})
     return JSONResponse(status_code=200, content=jsonable_encoder(result))

# Search all customers
@customers_router.get("/customers", tags=['CUSTOMERS'], response_model=List[CustomersSchema], status_code=200)
def get_all() -> List[CustomersSchema]:
     db = Session()
     result = CustomerService(db).get_all_customers()
     return JSONResponse(status_code=200, content=jsonable_encoder(result))

# customer creation
@customers_router.post("/customers", tags=['CUSTOMERS'], response_model=dict, status_code=201) #, dependencies=[Depends(JWTBearer())] 
def create(customer: CustomersSchema) -> dict:
    db = Session()
    CustomerService(db).create_customer(customer)
    return JSONResponse(status_code=201, content={"message": "Cliente creado correctamente"}) #JSONResponse(content={"message":"Prueba de mensaje JSON"})

# Update customer
@customers_router.put("/customers/", tags=['CUSTOMERS'], response_model=dict, status_code=200)
def update(id: int, customer: CustomersSchema) -> dict:
     db = Session()
     result = CustomerService(db).get_customer(id)
     if not result:
          return JSONResponse(status_code=404, content={"message":"Cliente no encontrado"})
     CustomerService(db).update_customer(id,customer)
     return JSONResponse(status_code=200, content={"message":"Se ha modificado el Cliente"})

# Delete customer     
@customers_router.delete("/customers/", tags=['CUSTOMERS'], response_model=dict, status_code=200)
def delete(id: int) -> dict:
     db = Session()
     result = CustomerService(db).get_customer(id)
     if not result:
          return JSONResponse(status_code=404, content={"message":"Cliente no encontrado"})
     CustomerService(db).delete_customer(id)
     return JSONResponse(status_code=200, content={"message":"Cliente eliminado"})

#######################################################################################