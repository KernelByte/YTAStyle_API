from config.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Customer(Base):
    
    __tablename__ = "Customers"

    idCustomer = Column(Integer, primary_key = True)
    nameCustomer = Column(String)
    cellPhoneCustomer = Column(Integer)
    address = Column(String)
    email = Column(String)
    observation = Column(String)

    #Buys = relationship("Buys", back_populates="owner")