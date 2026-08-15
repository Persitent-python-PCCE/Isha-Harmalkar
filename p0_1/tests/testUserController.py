

from unittest.mock import patch

import pytest

from controllers.userController import UserController
from models.user import User


@pytest.fixture
def user_controller():
    with patch("controllers.userController.UserService") as MockUserService:
        controller = UserController()
        controller.mock_service = MockUserService.return_value
        yield controller


class TestUserController:
    @patch("builtins.input", side_effect=["Alice", "alice@example.com", "pass123"] )
    def test_register_success(self, mock_input, user_controller):
        expected_user = User(name="ALice", email="alice@example.com", password="pass123")
        expected_user.id = 1
        expected_user.isAdmin = False


        user_controller.mock_service.register.return_value = expected_user
        result = user_controller.register()


        assert result is not None
        assert result.id == 1
        assert result.email == "alice@example.com"
        user_controller.mock_service.register.assert_called_once()


    @patch("builtins.input", side_effect=["alice@example.com", "pass123"])
    def test_login_success(self, mock_input, user_controller):
        expected_user = User(
            name="Alice", email="alice@example.com", password="pass123"
        )
        expected_user.id = 1
        expected_user.isAdmin = False

        user_controller.mock_service.login.return_value = expected_user
        result = user_controller.login(loginAsAdmin=False)
        assert result is not None
        assert result.id == 1
        user_controller.mock_service.login.assert_called_once_with("alice@example.com", "pass123", False)



    @patch("builtins.input", side_effect=["1"])
    def test_get_user_success(self, mock_input, user_controller):
        expected_user = User(
            name="Alice", email="alice@example.com", password="pass123"
        )
        expected_user.id = 1
        expected_user.isAdmin = False

        user_controller.mock_service.getUser.return_value = expected_user
        result = user_controller.getUser()
        assert result is not None
        assert result.id == 1
        user_controller.mock_service.getUser.assert_called_once_with(1)


    def test_get_all_sers_success(self, user_controller):
        u1 = User(name="U1", email="u1@ex.com", password="pass")
        u1.id = 1
        u1.isAdmin = False

        u2 = User(name="Admin", email="admin@exa.com", password="pass")
        u2.id = 2
        u2.isAdmin = True
        user_controller.mock_service.getAllUsers.return_value = [u1, u2]

        result = user_controller.getAllUsers()
        assert len(result) == 2
        assert result[0].id == 1
        assert result[1].isAdmin is True
   
    @patch("builtins.input", side_effect=["1", "Alice Admin", "admin.alice@example.com", "newpass123"])
    def test_update_user_and_promote_to_admin(self, mock_input, user_controller):
        user_controller.mock_service.updateUser.return_value = True

        result = user_controller.updateUser()

        assert result is True
        called_user = user_controller.mock_service.updateUser.call_args[0][0]
        called_user.isAdmin = True
        assert called_user.id == 1
        assert called_user.name =="Alice Admin"
        assert called_user.email == "admin.alice@example.com"
        assert called_user.isAdmin is True



