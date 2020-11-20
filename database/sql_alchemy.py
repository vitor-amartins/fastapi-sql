from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class SQLAlchemyDatabase:
    def __init__(self, db_type: str, username: str, password: str, host: str, port: str, db_name: str):
        self.SQLALCHEMY_DATABASE_URL = f'{db_type}://{username}:{password}@{host}:{port}/{db_name}'
        self.engine = create_engine(self.SQLALCHEMY_DATABASE_URL)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        self.Base = Base

    def get_db(self):
        db = self.SessionLocal()
        try:
            yield db
        finally:
            db.close()

    def create_tables(self):
        self.Base.metadata.create_all(bind=self.engine)
