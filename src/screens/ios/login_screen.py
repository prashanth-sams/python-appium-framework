from appium.webdriver.common.mobileby import MobileBy
from src.helpers.appiumdriver import Driver


class LoginScreen(Driver):
    """
    login screen locators
    """
    inputField = (MobileBy.ACCESSIBILITY_ID, 'input-email')
    passwordField = (MobileBy.ACCESSIBILITY_ID, 'input-password')
    loginButton = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="LOGIN"]')

    def __init__(self, driver):
        super().__init__(driver)