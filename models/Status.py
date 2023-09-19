from config.database import Base
from sqlalchemy import Column, Integer, String,ForeignKey
from sqlalchemy.orm import relationship

class State(Base):
    
    __tablename__ = "Status"

    idStatus = Column(Integer, primary_key = True)
    categoryStatus = Column(String)
    idBussinesState = Column(Integer,ForeignKey("Business.idBusiness"),nullable=True)
    description = Column(String)

    #Buys = relationship("Buys", back_populates="owner")
    #Products = relationship("Products", back_populates="owner")