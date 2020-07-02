from src.helpers.appiumdriver import Driver
from src.screens.android.home_screen import HomeLocators
from src.screens.android.login_screen import LoginLocators
from src.helpers.app import App


class TestLogin(Driver):

    def __init__(self, driver):
        super().__init__(driver)

    def test_login(self):
        App.click(self, HomeLocators.loginMenu)
        App.send_keys(self, LoginLocators.inputField, "johnsmith@gmail.com")
        """
        Need fix here
        """
        # App.elements(self, LoginLocators.passwordField)[0].send_keys("password")
        # App.send_keys(self, LoginLocators.passwordField[0], "password")
        App.tap(self, LoginLocators.inputField)