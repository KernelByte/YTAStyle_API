from models.Status import State as StatusModel
from schemas.StateSchema import State as StatusSchema

class stateService():
    def __init__(self,db) -> None:
        self.db = db

    def get_state(self, id):
      result = self.db.query(StatusModel).filter(StatusModel.idStatus == id).first()
      return result

    def get_all_status(self):
      result = self.db.query(StatusModel).all()
      return result
   
    def create_state(self, state: StatusSchema):
       new_state = StatusModel(**state.dict())
       self.db.add(new_state)
       self.db.commit()
       return

    def update_state(self, id: int, data: StatusSchema):
       update_state =  self.db.query(StatusModel).filter(StatusModel.idStatus == id).first()
       update_state.categoryStatus = data.categoryStatus
       update_state.description = data.description
       self.db.commit()
       return 
    
    def delete_state(self, id: int):
       self.db.query(StatusModel).filter(StatusModel.idStatus == id).delete()
       self.db.commit()
       return