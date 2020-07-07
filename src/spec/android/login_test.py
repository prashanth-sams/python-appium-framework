from src.helpers.appiumdriver import Driver
from src.screens.android.home_screen import HomeScreen
from src.screens.android.login_screen import LoginScreen
from src.helpers.app import App


class TestLogin(Driver):

    def __init__(self, driver):
        super().__init__(driver)

    def test_login(self):
        App.click(self, HomeScreen.loginMenu)
        App.send_keys(self, LoginScreen.inputField, "johnsmith@gmail.com")
        """
        Need fix here
        """
        # App.elements(self, LoginLocators.passwordField)[0].send_keys("password")
        # App.send_keys(self, LoginLocators.passwordField[0], "password")
        App.tap(self, LoginScreen.inputField)