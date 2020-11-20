from peewee import Model, UUIDField

from app.main import database_manager


class BaseDAO(Model):
    id = UUIDField(primary_key=True)

    class Meta:
        database = database_manager.get_db()
