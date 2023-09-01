from config.database import Base
from sqlalchemy import Column, Integer, String, Float, LargeBinary,ForeignKey
#from models import Base

class User(Base):
    
    __tablename__ = "Users"

    idUser = Column(Integer, primary_key = True, index=True)
    nameUser = Column(String)
    mailUser = Column(String)
    passwordUser = Column(String)
    idRoleUser = Column(Integer,ForeignKey("Roles.idRole"))
    tokenUser = Column(String)
    codeReference = Column(String)
    #profilePicture = Column(LargeBinary)
    idBusinessUser = Column(Integer)