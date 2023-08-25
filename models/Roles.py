from config.database import Base
from sqlalchemy import Column, Integer, String, Float, LargeBinary
#from models import Base

class Role(Base):
    
    __tablename__ = "Roles"

    idRole = Column(Integer, primary_key = True)
    description = Column(String)