import unittest
import pdb
from time import sleep
from src.utility.appiumdriver import Driver
from src.locators.home_screen_locators import HomeLocators

class HomeTest(Driver):
    
    def __init__(self, driver):
        Driver.__init__(self, driver)
    
    def test_home(self):
        self.driver.find_element_by_id(HomeLocators.homeMenu)
        self.driver.find_element_by_id(HomeLocators.loginMenu)
        self.driver.find_element_by_id(HomeLocators.formsMenu)
        self.driver.find_element_by_id(HomeLocators.swipeMenu)
        # pdb.set_trace()