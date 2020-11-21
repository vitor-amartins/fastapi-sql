import unittest
from unittest.mock import patch

from handlers import user_handler
from tests.fixtures import database_factory, user_factory


class TestUserHandler(unittest.TestCase):
    def setUp(self) -> None:
        self.sqlalchemy_db = database_factory.FakeSQLAlchemyDatabase()

    @patch('models.user.User.get_by_email', return_value=None)
    @patch('models.user.User.get_by_cpf_cnpj', return_value=None)
    @patch('models.user.User.create', return_value=user_factory.valid_user_one())
    def test_handle_create_user(self, create, get_by_cpf_cnpj, get_by_email):
        result = user_handler.handle_create_user(self.sqlalchemy_db, user_factory.valid_user_one_create())

        self.assertEqual(user_factory.valid_user_one(), result)
        create.assert_called_once_with(self.sqlalchemy_db, user_factory.valid_user_one_create())
        get_by_cpf_cnpj.assert_called_once_with(self.sqlalchemy_db, user_factory.valid_user_one_create().cpf_cnpj)
        get_by_email.assert_called_once_with(self.sqlalchemy_db, user_factory.valid_user_one_create().email)

    @patch('models.user.User.list', return_value=[user_factory.valid_user_one()])
    def test_handle_list_user(self, list_users):
        page = 1
        page_size = 10
        result = user_handler.handle_list_users(self.sqlalchemy_db, page, page_size)

        self.assertEqual([user_factory.valid_user_one()], result)
        list_users.assert_called_once_with(self.sqlalchemy_db, page, page_size)

    @patch('models.user.User.get', return_value=user_factory.valid_user_one())
    def test_handle_get_user(self, get_user):
        result = user_handler.handle_get_user(self.sqlalchemy_db, user_factory.valid_user_one().id)

        self.assertEqual(user_factory.valid_user_one(), result)
        get_user.assert_called_once_with(self.sqlalchemy_db, user_factory.valid_user_one().id)

    @patch('models.user.User.delete', return_value=True)
    def test_handle_delete_user(self, delete_user):
        result = user_handler.handle_delete_user(self.sqlalchemy_db, user_factory.valid_user_one().id)

        self.assertEqual(True, result)
        delete_user.assert_called_once_with(self.sqlalchemy_db, user_factory.valid_user_one().id)

    @patch('models.user.User.update', return_value=user_factory.valid_user_one_updated())
    def test_handle_update_user(self, update_user):
        result = user_handler.handle_update_user(self.sqlalchemy_db, user_factory.valid_user_one().id,
                                                 user_factory.valid_user_one_update())

        self.assertEqual(user_factory.valid_user_one_updated(), result)
        update_user.assert_called_once_with(self.sqlalchemy_db, user_factory.valid_user_one().id,
                                            user_factory.valid_user_one_update())


if __name__ == '__main__':
    unittest.main()
