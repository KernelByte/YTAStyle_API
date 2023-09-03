from config.database import Base
from sqlalchemy import Column, Integer, String, LargeBinary,ForeignKey
from sqlalchemy.orm import relationship

class User(Base):
    
    __tablename__ = "Users"

    idUser = Column(Integer, primary_key = True, index=True)
    nameUser = Column(String)
    mailUser = Column(String)
    passwordUser = Column(String)
    idRoleUser = Column(Integer,ForeignKey("Roles.idRole"),nullable=True)
    tokenUser = Column(String)
    codeReference = Column(String)
    profilePicture = Column(LargeBinary)
    idBusinessUser = Column(Integer,ForeignKey("Business.idBusiness"),nullable=True)

    #roles = relationship("Role")
    #business = relationship("Busine")