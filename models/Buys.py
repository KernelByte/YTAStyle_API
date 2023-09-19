from config.database import Base
from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.orm import relationship

class Buy(Base):
    
    __tablename__ = "Buys"

    idBuy = Column(Integer, primary_key = True)
    idCategoryBuy = Column(Integer,ForeignKey("Categories.idCategory"),nullable=True)
    priceUnitBuy = Column(Float)
    priceBuyTotal = Column(Float)
    dateBuy = Column(Date)
    idPaymentStatus = Column(Integer,ForeignKey("Status.idStatus"),nullable=True)
    idCustomerBuy = Column(Integer,ForeignKey("Customers.idCustomer"),nullable=True)
    idBusinessBuy = Column(Integer,ForeignKey("Business.idBusiness"),nullable=True)
    discount = Column(Float)
    TypeDiscount = Column(String)
    quantityBuy = Column(Integer)
    paymentType = Column(String)

    #customers = relationship("Customers")
   # categories = relationship("Categories")
    #status = relationship("Status")