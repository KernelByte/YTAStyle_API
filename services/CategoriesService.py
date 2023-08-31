from models.Categories import Category as CategoriesModel
from schemas.CategoriesSchema import Categori as CategoriesSchema

class CategoryService():
    def __init__(self,db) -> None:
        self.db = db

    def get_category(self, id):
      result = self.db.query(CategoriesModel).filter(CategoriesModel.idCategory == id).first()
      return result

    def get_all_categories(self):
      result = self.db.query(CategoriesModel).all()
      return result
   
    def create_category(self, category: CategoriesSchema):
       new_category = CategoriesModel(**category.dict())
       self.db.add(new_category)
       self.db.commit()
       return

    def update_category(self, id: int, data: CategoriesSchema):
       update_category =  self.db.query(CategoriesModel).filter(CategoriesModel.idCategory == id).first()
       update_category.description = data.description
       self.db.commit()
       return 
    
    def delete_category(self, id: int):
       self.db.query(CategoriesModel).filter(CategoriesModel.idCategory == id).delete()
       self.db.commit()
       return