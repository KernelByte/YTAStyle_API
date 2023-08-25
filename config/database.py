from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


database_url = "postgresql://yta_user:yta20394.0@ServerKernel/yta_style"
# database_url = f"postgresql:///{os.path.join(base_dir, postgresql_file_name)}"

engine = create_engine(database_url, echo=True )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()