import uuid
from datetime import datetime

from sqlalchemy import Column, String, Boolean, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Session

from database.sql_alchemy import Base
from schemas.user import UserCreate, UserUpdate
from utils.security import get_password_hash


class User(Base):
    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    cpf_cnpj = Column(String, unique=True, index=True)
    password = Column(String)
    address = Column(String)
    active = Column(Boolean, default=False)
    picture = Column(String, nullable=True, default=None)
    reset_password_token = Column(String, nullable=True, default=None)
    reset_password_expires_in = Column(DateTime, nullable=True, default=None)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)

    @staticmethod
    def create(db: Session, user: UserCreate):
        db_user = User(**user.dict(exclude={'password'}), password=get_password_hash(user.password))
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    @staticmethod
    def get(db: Session, user_id: UUID):
        return db.query(User).filter(User.id == user_id).first()

    @staticmethod
    def get_by_email(db: Session, email: str):
        return db.query(User).filter(User.email == email).first()

    @staticmethod
    def get_by_cpf_cnpj(db: Session, cpf_cnpj: str):
        return db.query(User).filter(User.cpf_cnpj == cpf_cnpj).first()

    @staticmethod
    def list(db: Session, page: int, page_size: int):
        offset = (page - 1) * page_size
        limit = offset + page_size
        return db.query(User).offset(offset).limit(limit).all()

    @staticmethod
    def delete(db: Session, user_id: UUID):
        db.query(User).filter(User.id == user_id).delete()
        db.commit()
        return True

    @staticmethod
    def update(db: Session, user_id: UUID, user: UserUpdate):
        db_user: User = db.query(User).filter(User.id == user_id).first()
        if user.name:
            db_user.name = user.name
        if user.address:
            db_user.address = user.address
        db_user.created_at = datetime.now()
        db.commit()
        db.refresh(db_user)
        return db_user
