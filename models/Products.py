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
    idCategoryProduct = Column(Integer,ForeignKey("Categories.idCategory"),nullable=True)
    idBusinessProduct = Column(Integer,ForeignKey("Business.idBusiness"),nullable=True)
    idStatusProduct = Column(Integer,ForeignKey("Status.idStatus"),nullable=True)
    color = Column(String)
    productImage = Column(String)
    description = Column(String)
    barcode = Column(String)

    #categories = relationship("Categories")
    #status = relationship("Status")