from src.helpers.appiumdriver import Driver
from src.locators.home_screen_locators import HomeLocators
from src.helpers.app import App


class HomeTest(Driver):
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def test_home_1(self):
        App.element(self, HomeLocators.homeMenu)
        App.element(self, HomeLocators.loginMenu)
        App.element(self, HomeLocators.formsMenu)
        App.element(self, HomeLocators.swipeMenu)

    def test_home_2(self):
        App.element(self, HomeLocators.homeMenu)
        App.element(self, HomeLocators.loginMenu)