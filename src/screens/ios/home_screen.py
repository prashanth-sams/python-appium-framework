from appium.webdriver.common.mobileby import MobileBy
from src.helpers.appiumdriver import Driver


class HomeScreen(Driver):
    """
    home screen locators
    """
    loginMenu = (MobileBy.ID, "Login")
    formsMenu = (MobileBy.ID, "Forms")
    homeMenu = (MobileBy.ID, "Home")
    swipeMenu = (MobileBy.ID, "Swipe")

    # swipeMenu = {'ANDROID': (MobileBy.ACCESSIBILITY_ID, "Swipe"),'IOS': (MobileBy.ACCESSIBILITY_ID, "Swipe")}

    def __init__(self, driver):
        super().__init__(driver)