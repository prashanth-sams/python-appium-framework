from appium.webdriver.common.mobileby import MobileBy
from src.helpers.appiumdriver import Driver


class BaseScreen(Driver):
    """
    common screen locators
    """

    def __init__(self, driver):
        super().__init__(driver)