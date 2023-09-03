from config.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.Buys import Buy

class Category(Base):
    
    __tablename__ = "Categories"

    idCategory = Column(Integer, primary_key = True)
    description = Column(String)

   #Buys = Base.relationship("Buys", back_populates="Categories")
    #Products = relationship("Products", back_populates="Categories")