from models.Users import User as UserModel

class UserService():
    def __init__(self,db) -> None:
        self.db = db

    def get_all_users(self):
      result = self.db.query(UserModel).all()
      return result
    
    def get_user(self, id):
      result = self.db.query(UserModel).filter(UserModel.idUser == id).first()
      return result