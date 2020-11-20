from uuid import UUID

from sqlalchemy.orm import Session
from starlette import status

from handlers.error_handler import handle_error
from models.user import User
from schemas.user import UserCreate, UserUpdate
from utils.exceptions import MappedException


def handle_create_user(db: Session, user: UserCreate):
    try:
        user_with_email = User.get_by_email(db, user.email)
        if user_with_email:
            raise MappedException(status.HTTP_400_BAD_REQUEST, 'Email already registered')
        user_with_cpf_cnpj = User.get_by_cpf_cnpj(db, user.cpf_cnpj)
        if user_with_cpf_cnpj:
            raise MappedException(status.HTTP_400_BAD_REQUEST, 'CPF/CNPJ already registered')
        return User.create(db, user)
    except Exception as e:
        return handle_error(e)


def handle_list_users(db: Session, page: int = 1, page_size: int = 10):
    try:
        return User.list(db, page, page_size)
    except Exception as e:
        return handle_error(e)


def handle_get_user(db: Session, user_id: UUID):
    try:
        user = User.get(db, user_id)
        if user is None:
            raise MappedException(status.HTTP_404_NOT_FOUND, 'User not found')
    except Exception as e:
        return handle_error(e)


def handle_delete_user(db: Session, user_id: UUID):
    try:
        return User.delete(db, user_id)
    except Exception as e:
        return handle_error(e)


def handle_update_user(db: Session, user_id: UUID, user: UserUpdate):
    try:
        return User.update(db, user_id, user)
    except Exception as e:
        return handle_error(e)
