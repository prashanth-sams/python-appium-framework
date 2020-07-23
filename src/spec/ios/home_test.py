import pytest
from src.helpers.appiumdriver import Driver
from src.screens.ios.home_screen import HomeScreen
from src.helpers.app import App


class TestHome(Driver):
    
    def __init__(self, driver):
        super().__init__(driver)

    @pytest.mark.home
    def test_home_1(self):
        App.is_displayed(self, HomeScreen.homeMenu, True)
        App.is_displayed(self, HomeScreen.loginMenu, True)
        App.is_displayed(self, HomeScreen.formsMenu, True)
        App.is_displayed(self, HomeScreen.swipeMenu, True)

    @pytest.mark.home
    def test_home_2(self):
        App.is_displayed(self, HomeScreen.homeMenu, True)
        App.is_displayed(self, HomeScreen.loginMenu, True)