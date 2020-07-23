import pytest
from src.helpers.appiumdriver import Driver
from src.screens.ios.home_screen import HomeScreen
from src.screens.ios.login_screen import LoginScreen
from src.helpers.app import App


class TestLogin(Driver):

    def __init__(self, driver):
        super().__init__(driver)

    @pytest.mark.login
    def test_login(self):
        App.click(self, HomeScreen.loginMenu)
        App.send_keys(self, LoginScreen.inputField, "johnsmith@gmail.com")
        App.send_keys(self, LoginScreen.passwordField, "password", index=0)
        App.tap(self, LoginScreen.inputField)