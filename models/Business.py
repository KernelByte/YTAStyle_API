from config.database import Base
from sqlalchemy import Column, Integer, String, Float, LargeBinary, DateTime

class Busine(Base):
    
    __tablename__ = "Business"

    idBusiness = Column(Integer, primary_key = True)
    nameBusiness = Column(String)
    cellPhone = Column(Integer)
    Location = Column(String)
    schedule = Column(DateTime)
