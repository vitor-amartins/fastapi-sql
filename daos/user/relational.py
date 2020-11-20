from datetime import datetime

from peewee import CharField, DateTimeField, BooleanField

from daos.base.base_dao import BaseDAO


class RelationalUserDAO(BaseDAO):
    name = CharField()
    email = CharField(unique=True)
    cpf_cnpj = CharField(unique=True, max_length=14)
    password = CharField()
    address = CharField()
    active = BooleanField(default=False)
    picture = CharField(null=True)
    reset_password_token = CharField(null=True)
    reset_password_expires_in = DateTimeField(null=True)
    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField(default=datetime.now)

    class Meta:
        table_name = 'users'

    def dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'cpf_cnpj': self.cpf_cnpj,
            'password': self.password,
            'address': self.address,
            'active': self.active,
            'picture': self.picture,
            'reset_password_token': self.reset_password_token,
            'reset_password_expires_in': self.reset_password_expires_in,
        }
