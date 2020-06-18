import unittest
from selenium.webdriver.common.by import By
from src.utility.appiumdriver import Driver
from src.locators.home_screen_locators import HomeLocators
from src.locators.login_screen_locators import LoginLocators

class LoginTest(Driver):

    def __init__(self, driver):
        super().__init__(driver)

    def test_login(self):
        self.driver.find_element_by_xpath(HomeLocators.loginMenu).click()
        self.driver.find_element(by=By.XPATH, value=LoginLocators.inputField).send_keys("johnsmith@gmail.com")
        self.driver.find_elements_by_accessibility_id(LoginLocators.passwordField)[0].send_keys("password")
        self.driver.find_element_by_xpath(LoginLocators.loginButton).click()