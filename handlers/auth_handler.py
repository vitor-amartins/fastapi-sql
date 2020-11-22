from sqlalchemy.orm import Session
from starlette import status

from handlers.error_handler import handle_error
from models.user import User
from schemas.authentication import Token
from utils.exceptions import MappedException
from utils.security import verify_password, create_access_token


def handle_authenticate(db: Session, email: str, password: str):
    try:
        user = User.get_by_email(db, email)
        if user is None:
            raise MappedException(status.HTTP_400_BAD_REQUEST, 'Incorrect email')
        if not verify_password(password, user.password):
            raise MappedException(status.HTTP_400_BAD_REQUEST, 'Incorrect password')
        if not user.active:
            raise MappedException(status.HTTP_400_BAD_REQUEST, 'Inactive user')
        return Token(access_token=create_access_token(user.id), token_type='bearer')
    except Exception as e:
        return handle_error(e)
