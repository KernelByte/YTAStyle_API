from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


database_url = "postgresql://postgres:Hack20394@localhost:5432/yta_style"
# Encargado de interactuar con la base de datos
engine = create_engine(database_url, echo=True )
# Encargado de mantener el estado de los elementos
Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Base para crear los modelos.
Base = declarative_base()