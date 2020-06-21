from src.helpers.appiumdriver import Driver
from src.locators.home_screen_locators import HomeLocators
from src.locators.login_screen_locators import LoginLocators
from src.helpers.app import App


class LoginTest(Driver):

    def __init__(self, driver):
        super().__init__(driver)

    def test_login(self):
        App.element(self, HomeLocators.loginMenu).click()
        App.element(self, LoginLocators.inputField).send_keys("johnsmith@gmail.com")
        App.elements(self, LoginLocators.passwordField)[0].send_keys("password")
        App.element(self, LoginLocators.inputField).click()