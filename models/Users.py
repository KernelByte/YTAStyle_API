from config.database import Base
from sqlalchemy import Column, Integer, String, Float, LargeBinary
#from models import Base

class User(Base):
    
    __tablename__ = "Users2"

    idUser = Column(Integer, primary_key = True)
    nameUser = Column(String)
    mailUser = Column(String)
    passwordUser = Column(String)
    idRoleUser = Column(Integer)
    tokenUser = Column(String)
    codeReference = Column(String)
    profilePicture = Column(LargeBinary)
    idBusinessUser = Column(Integer)