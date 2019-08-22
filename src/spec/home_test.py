import unittest
from time import sleep
from src.support.webdriver import Driver
import pdb
from src.locators.home_screen_locators import HomeLocators
from src.locators.login_screen_locators import LoginLocators

class HomeTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = Driver().driver
    
    def tearDown(self):
        self.driver.quit()
    
    def test_home(self):
        self.driver.find_element_by_id(HomeLocators.homeMenu)
        self.driver.find_element_by_id(HomeLocators.loginMenu)
        self.driver.find_element_by_id(HomeLocators.formsMenu)
        self.driver.find_element_by_id(HomeLocators.swipeMenu)
        # pdb.set_trace()