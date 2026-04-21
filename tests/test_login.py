import pytest 
from pages.login_page import LoginPage

class TestLogin:

    def test_valid_login(self, page):
        login = LoginPage(page)
        login.navigate()
        login.login("tomsmith", "SuperSecretPassword!")
        assert login.success_message.is_visible()
        assert "You logged into a secure area!" in login.success_message.inner_text()

    def test_invalid_username(self, page):
        login = LoginPage(page)
        login.navigate()
        login.login("wronguser", "SuperSecretPassword!")
        assert login.error_message.is_visible()

    def test_invalid_password(self, page):
        login = LoginPage(page)
        login.navigate()
        login.login("tomsmith", "wrongpassword")
        assert login.error_message.is_visible()

    def test_empty_fields(self, page):
        login = LoginPage(page)
        login.navigate()
        login.login("", "")
        assert login.error_message.is_visible()
