from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from starlette import status

from handlers import auth_handler
from schemas.authentication import Token


def auth_router(get_db: callable):
    router = APIRouter()
    tags = ['Authentication']

    @router.post('/login/', status_code=status.HTTP_200_OK, response_model=Token, tags=tags)
    def login(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
        return auth_handler.handle_authenticate(db, form_data.username, form_data.password)

    return router
