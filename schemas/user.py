from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    email: str
    cpf_cnpj: str
    address: str


class UserCreate(UserBase):
    password: str


class UserUpdate(BaseModel):
    name: Optional[str]
    address: Optional[str]


class User(UserBase):
    id: UUID
    active: bool = False
    picture: Optional[str]
    reset_password_token: Optional[str]
    reset_password_expires_in: Optional[datetime]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True
