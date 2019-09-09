import unittest
from src.utility.webdriver import Driver
from src.locators.home_screen_locators import HomeLocators
from src.locators.login_screen_locators import LoginLocators

class LoginTest(Driver):

    def __init__(self, driver):
        Driver.__init__(self, driver)
        
    def test_login(self):
        self.driver.find_element_by_id(HomeLocators.loginMenu).click()
        self.driver.find_element_by_id(LoginLocators.inputField).send_keys("johnsmith@gmail.com")
        self.driver.find_element_by_id(LoginLocators.passwordField).send_keys("password")
        self.driver.find_element_by_id(LoginLocators.loginButton).click()