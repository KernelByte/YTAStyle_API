from config.database import Base
from sqlalchemy import Column, Integer, String

class Category(Base):
    
    __tablename__ = "Categories2"

    idCategory = Column(Integer, primary_key = True)
    description = Column(String)