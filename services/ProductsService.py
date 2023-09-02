from models.Products import Product as ProductsModel
from schemas.ProductSchema import Product as ProductsSchema
from datetime import datetime

class ProductService():
    def __init__(self,db) -> None:
        self.db = db

    def get_product(self, id):
      result = self.db.query(ProductsModel).filter(ProductsModel.idProduct == id).first()
      return result

    def get_all_products(self):
      result = self.db.query(ProductsModel).all()
      return result
   
    def create_product(self, product: ProductsSchema):
       new_product = ProductsModel(**product.dict())
       self.db.add(new_product)
       self.db.commit()
       return

    def update_product(self, id: int, data: ProductsSchema):
       update_product =  self.db.query(ProductsModel).filter(ProductsModel.idProduct == id).first()
       update_product.nameProduct = data.nameProduct
       update_product.quantity = data.quantity
       update_product.priceCost = data.priceCost
       update_product.priceBuy = data.priceBuy
       update_product.idCategoryProduct = data.idCategoryProduct
       update_product.idStatusProduct = data.idStatusProduct
       update_product.color = data.color
       update_product.description = data.description
       update_product.barcode = data.barcode
       self.db.commit()
       return 
    
    def delete_product(self, id: int):
       self.db.query(ProductsModel).filter(ProductsModel.idProduct == id).delete()
       self.db.commit()
       return