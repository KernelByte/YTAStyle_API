from config.database import Base
from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.orm import relationship

class Buy(Base):
    
    __tablename__ = "Buys"

    idBuy = Column(Integer, primary_key = True)
    idCategoryBuy = Column(Integer)
    priceUnitBuy = Column(Float)
    priceBuyTotal = Column(Float)
    dateBuy = Column(Date)
    idPaymentStatus = Column(Integer)
    idCustomerBuy = Column(Integer,ForeignKey("Customers.idCustomer"))
    discount = Column(Float)
    TypeDiscount = Column(String)
    quantityBuy = Column(Integer)
    paymentType = Column(String)

    owner = relationship("Customers", back_populates="Buys")