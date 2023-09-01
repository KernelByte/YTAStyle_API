from config.database import Base
from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.orm import relationship

class Buy(Base):
    
    __tablename__ = "Buys"

    idBuy = Column(Integer, primary_key = True)
    idCategoryBuy = Column(Integer,ForeignKey("Categories.idCategory"))
    priceUnitBuy = Column(Float)
    priceBuyTotal = Column(Float)
    dateBuy = Column(Date)
    idPaymentStatus = Column(Integer,ForeignKey("Status.idStatus"))
    idCustomerBuy = Column(Integer,ForeignKey("Customers.idCustomer"))
    discount = Column(Float)
    TypeDiscount = Column(String)
    quantityBuy = Column(Integer)
    paymentType = Column(String)

    owner = relationship("Customers", back_populates="Buys")
    owner = relationship("Categories", back_populates="Buys")
    owner = relationship("Status", back_populates="Buys")