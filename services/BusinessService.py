from models.Business import Busine as BusinessModel
from schemas.BusinessSchema import Business as BusinessSchema

class BusinessService():
    def __init__(self,db) -> None:
        self.db = db

    def get_business(self, id):
      result = self.db.query(BusinessModel).filter(BusinessModel.idBusiness == id).first()
      return result

    def get_all_business(self):
      result = self.db.query(BusinessModel).all()
      return result
   
    def create_business(self, business: BusinessSchema):
       new_business = BusinessModel(**business.dict())
       self.db.add(new_business)
       self.db.commit()
       return

    def update_business(self, id: int, data: BusinessSchema):
       update_business =  self.db.query(BusinessModel).filter(BusinessModel.idBusiness == id).first()
       update_business.nameBusiness = data.nameBusiness
       update_business.cellPhone = data.cellPhone
       update_business.Location = data.Location
       update_business.schedule = data.schedule
       self.db.commit()
       return 
    
    def delete_business(self, id: int):
       self.db.query(BusinessModel).filter(BusinessModel.idBusiness == id).delete()
       self.db.commit()
       return