from config.database import Base
from sqlalchemy import Column, Integer, String, Date, Float

class Buy(Base):
    
    __tablename__ = "Buys"

    idBuy = Column(Integer, primary_key = True)
    idCategoryBuy = Column(Integer)
    priceUnitBuy = Column(Float)
    priceBuyTotal = Column(Float)
    dateBuy = Column(Date)
    idPaymentStatus = Column(Integer)
    idCustomerBuy = Column(Integer)
    discount = Column(Float)
    TypeDiscount = Column(String)
    quantityBuy = Column(Integer)
    paymentType = Column(String)