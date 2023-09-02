from config.database import Base
from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.orm import relationship

class Product(Base):
    
    __tablename__ = "Products"

    idProduct = Column(Integer, primary_key = True)
    nameProduct = Column(String)
    dateProduct = Column(String)
    quantity = Column(Integer)
    priceCost = Column(Float)
    priceBuy  = Column(Float)
    idCategoryProduct = Column(Integer,ForeignKey("Categories.idCategory"))
    idStatusProduct = Column(Integer,ForeignKey("Status.idStatus"))
    color = Column(String)
    #productImage = Column()
    description = Column(String)
    barcode = Column(String)

    owner = relationship("Categories", back_populates="Products")
    owner = relationship("Status", back_populates="Products")