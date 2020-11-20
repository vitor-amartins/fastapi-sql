from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from handlers import user_handler
from schemas.user import User, UserCreate, UserUpdate


def user_router(get_db: callable):
    router = APIRouter()
    tags = ['User']

    @router.post('/', response_model=User, tags=tags)
    def create_user(user: UserCreate, db: Session = Depends(get_db)):
        return user_handler.handle_create_user(db, user)

    @router.get('/', response_model=List[User], tags=tags)
    def list_users(page: int = 1, page_size: int = 10, db: Session = Depends(get_db)):
        return user_handler.handle_list_users(db, page, page_size)

    @router.get('/{user_id}', response_model=User, tags=tags)
    def get_user(user_id: UUID, db: Session = Depends(get_db)):
        return user_handler.handle_get_user(db, user_id)

    @router.delete('/{user_id}', response_model=bool, tags=tags)
    def delete_user(user_id: UUID, db: Session = Depends(get_db)):
        return user_handler.handle_delete_user(db, user_id)

    @router.patch('/{user_id}', response_model=User, tags=tags)
    def update_user(user_id: UUID, user: UserUpdate, db: Session = Depends(get_db)):
        return user_handler.handle_update_user(db, user_id, user)

    return router
