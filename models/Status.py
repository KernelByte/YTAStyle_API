from config.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class State(Base):
    
    __tablename__ = "Status"

    idStatus = Column(Integer, primary_key = True)
    categoryStatus = Column(String)
    description = Column(String)

    Buys = relationship("Buys", back_populates="owner")