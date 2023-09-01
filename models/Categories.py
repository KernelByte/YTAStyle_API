from config.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Category(Base):
    
    __tablename__ = "Categories"

    idCategory = Column(Integer, primary_key = True)
    description = Column(String)

    Buys = relationship("Buys", back_populates="owner")
    Products = relationship("Products", back_populates="owner")