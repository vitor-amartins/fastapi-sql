from os import environ

from fastapi import FastAPI

from database.sql_alchemy import SQLAlchemyDatabase
from routes.user import user_router


sqlalchemy_db = SQLAlchemyDatabase(
    db_type=environ.get('DB_TYPE', 'postgresql'),
    username=environ.get('DB_USERNAME', 'postgres'),
    password=environ.get('DB_PASSWORD', 'postgres'),
    host=environ.get('DB_HOST', 'localhost'),
    port=environ.get('DB_PORT', '5432'),
    db_name=environ.get('DB_NAME', 'postgres'),
)

app = FastAPI()

app.include_router(
    router=user_router(sqlalchemy_db.get_db),
    prefix='/users'
)
