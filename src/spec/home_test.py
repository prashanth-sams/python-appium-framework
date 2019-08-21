import unittest
from time import sleep
from appium import webdriver
import pdb
from src.locators.home_screen_locators import HomeLocators
from src.locators.login_screen_locators import LoginLocators

class AppiumTest(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = ''
        desired_caps['deviceName'] = 'PF'
        desired_caps['appPackage'] = 'com.wdiodemoapp'
        desired_caps['appActivity'] = 'com.wdiodemoapp.MainActivity'
        self.driver = webdriver.Remote("http://0.0.0.0:4723/wd/hub", desired_caps)
    
    def tearDown(self):
        self.driver.quit()
    
    def test_home(self):
        self.driver.find_element_by_id(HomeLocators.homeMenu)
        self.driver.find_element_by_id(HomeLocators.loginMenu)
        self.driver.find_element_by_id(HomeLocators.formsMenu)
        self.driver.find_element_by_id(HomeLocators.swipeMenu)
        # pdb.set_trace()
    
    def test_login(self):
        self.driver.find_element_by_id(HomeLocators.loginMenu).click()
        self.driver.find_element_by_id(LoginLocators.inputField).send_keys("johnsmith@gmail.com")
        self.driver.find_element_by_id(LoginLocators.passwordField).send_keys("password")
        self.driver.find_element_by_id(LoginLocators.loginButton).click()