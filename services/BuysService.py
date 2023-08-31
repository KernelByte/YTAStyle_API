from models.Buys import Buy as BuysModel
from schemas.BuysSchema import Buy as BuysSchema

class BuyService():
    def __init__(self,db) -> None:
        self.db = db

    def get_buy(self, id):
      result = self.db.query(BuysModel).filter(BuysModel.idBuy == id).first()
      return result

    def get_all_buys(self):
      result = self.db.query(BuysModel).all()
      return result
   
    def create_buy(self, buy: BuysSchema):
       new_buy = BuysModel(**buy.dict())
       self.db.add(new_buy)
       self.db.commit()
       return

    def update_buy(self, id: int, data: BuysSchema):
       update_buy =  self.db.query(BuysModel).filter(BuysModel.idBuy == id).first()
       update_buy.idCategoryBuy = data.idCategoryBuy
       update_buy.priceUnitBuy = data.priceUnitBuy
       update_buy.priceBuyTotal = data.priceBuyTotal
       update_buy.dateBuy = data.dateBuy
       update_buy.idPaymentStatus = data.idPaymentStatus
       update_buy.idCustomerBuy = data.idCustomerBuy
       update_buy.discount = data.discount
       update_buy.TypeDiscount = data.TypeDiscount
       update_buy.quantityBuy = data.quantityBuy
       update_buy.paymentType = data.paymentType
       self.db.commit()
       return 
    
    def delete_buy(self, id: int):
       self.db.query(BuysModel).filter(BuysModel.idBuy == id).delete()
       self.db.commit()
       return