from models.Roles import Role as RolesModel
from schemas.RoleSchema import Rol as RolesSchema

class RolService():
    def __init__(self,db) -> None:
        self.db = db

    def get_rol(self, id):
      result = self.db.query(RolesModel).filter(RolesModel.idRole == id).first()
      return result

    def get_all_roles(self):
      result = self.db.query(RolesModel).all()
      return result
   
    def create_rol(self, rol: RolesSchema):
       new_rol = RolesModel(**rol.dict())
       self.db.add(new_rol)
       self.db.commit()
       return

    def update_rol(self, id: int, data: RolesSchema):
       update_rol =  self.db.query(RolesModel).filter(RolesModel.idRole == id).first()
       update_rol.description = data.description
       self.db.commit()
       return 
    
    def delete_rol(self, id: int):
       self.db.query(RolesModel).filter(RolesModel.idRole == id).delete()
       self.db.commit()
       return