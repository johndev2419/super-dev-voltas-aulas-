from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+pymysql://root:admin@127.0.0.1:3306/pizza"

engine = create_engine(DATABASE_URL, echo=False)

sessionlocal = sessionmaker(bind=engine, autocommit = False, autoflush=False)


def get_db(): 
    db = sessionlocal()
    try:
        yield db 
    finally:
        db.close()