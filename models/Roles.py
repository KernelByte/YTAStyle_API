from config.database import Base
from sqlalchemy import Column, Integer, String, Float, LargeBinary
from sqlalchemy.orm import relationship

class Role(Base):
    
    __tablename__ = "Roles"

    idRole = Column(Integer, primary_key = True)
    description = Column(String)

    #Users = relationship("Users", back_populates="owner")