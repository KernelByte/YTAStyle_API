from models.Customers import Customer as CustomersModel
from schemas.CustomerSchema import Customer as CustomersSchema

class CustomerService():
    def __init__(self,db) -> None:
        self.db = db

    def get_customer(self, id):
      result = self.db.query(CustomersModel).filter(CustomersModel.idCustomer == id).first()
      return result

    def get_all_customers(self):
      result = self.db.query(CustomersModel).all()
      return result
   
    def create_customer(self, customer: CustomersSchema):
       new_customer = CustomersModel(**customer.dict())
       self.db.add(new_customer)
       self.db.commit()
       return

    def update_customer(self, id: int, data: CustomersSchema):
       update_customer =  self.db.query(CustomersModel).filter(CustomersModel.idCustomer == id).first()
       update_customer.nameCustomer = data.nameCustomer
       update_customer.cellPhoneCustomer = data.cellPhoneCustomer
       update_customer.address = data.address
       update_customer.email = data.email
       update_customer.observation = data.observation
       self.db.commit()
       return 
    
    def delete_customer(self, id: int):
       self.db.query(CustomersModel).filter(CustomersModel.idCustomer == id).delete()
       self.db.commit()
       return