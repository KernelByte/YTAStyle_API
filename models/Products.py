from config.database import Base
from sqlalchemy import Column, Integer, String, DateTime, Float

class Producto(Base):
    
    __tablename__ = "Products"

    idProduct = Column(Integer, primary_key = True)
    nameProduct = Column(String)
    dateProduct = Column(DateTime)
    quantity = Column(Integer)
    priceCost = Column(Float)
    priceBuy  = Column(Float)
    idCategoryProduct = Column(Integer)
    idStatusProduct = Column(Integer)
    color = Column(String)
    #productImage = Column()
    description = Column(String)
    barcode = Column(String)