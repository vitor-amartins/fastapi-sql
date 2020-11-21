import unittest
from unittest.mock import patch

from fastapi import FastAPI
from fastapi.testclient import TestClient
from starlette import status

from routes.user_routes import user_router
from tests.fixtures import database_factory, user_factory


class TestUserRoutes(unittest.TestCase):
    def setUp(self) -> None:
        self.sqlalchemy_db = database_factory.FakeSQLAlchemyDatabase()
        app = FastAPI()
        app.include_router(user_router(self.sqlalchemy_db.get_db))
        self.client = TestClient(app)

    @patch('handlers.user_handler.handle_create_user', return_value=user_factory.valid_user_one_data())
    def test_create_user(self, handle_create_user):
        response = self.client.post(
            '/',
            json=user_factory.valid_user_one_create().dict(),
        )

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(user_factory.valid_user_one_data_without_password(), response.json())
        handle_create_user.assert_called_once_with(self.sqlalchemy_db, user_factory.valid_user_one_create())

    @patch('handlers.user_handler.handle_list_users', return_value=[user_factory.valid_user_one_data()])
    def test_list_users(self, handle_list_users):
        page = 1
        page_size = 5
        response = self.client.get(
            '/',
            params={
                'page': page,
                'page_size': page_size,
            },
        )

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual([user_factory.valid_user_one_data_without_password()], response.json())
        handle_list_users.assert_called_once_with(self.sqlalchemy_db, page, page_size)

    @patch('handlers.user_handler.handle_get_user', return_value=user_factory.valid_user_one_data())
    def test_get_user(self, handle_get_user):
        user_id = user_factory.valid_user_one().id
        response = self.client.get(
            f'/{user_id}',
        )

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(user_factory.valid_user_one_data_without_password(), response.json())
        handle_get_user.assert_called_once_with(self.sqlalchemy_db, user_id)

    @patch('handlers.user_handler.handle_delete_user', return_value=True)
    def test_delete_user(self, handle_delete_user):
        user_id = user_factory.valid_user_one().id
        response = self.client.delete(
            f'/{user_id}',
        )

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertTrue(response.json())
        handle_delete_user.assert_called_once_with(self.sqlalchemy_db, user_id)

    @patch('handlers.user_handler.handle_update_user',
           return_value=user_factory.valid_user_one_updated_without_password())
    def test_update_user(self, handle_update_user):
        user_id = user_factory.valid_user_one().id
        response = self.client.patch(
            f'/{user_id}',
            json=user_factory.valid_user_one_update().dict(),
        )

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(user_factory.valid_user_one_updated_without_password(), response.json())
        handle_update_user.assert_called_once_with(self.sqlalchemy_db, user_id, user_factory.valid_user_one_update())


if __name__ == '__main__':
    unittest.main()
