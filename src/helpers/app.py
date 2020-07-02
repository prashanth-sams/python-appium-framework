from src.helpers.appiumdriver import Driver
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
import time


class App(Driver):

    def __init__(self, driver):
        super().__init__(driver)

    def element(self, locator, n=5):
        """
        locate an element by polling if element not found
        maximum poll #4 with approx. ~20 secs
        """
        while n > 1:
            try:
                return self.driver.find_element(*locator)
            except Exception as e:
                n -= 1
                if n is 1: raise NoSuchElementException("Could not locate element with value: %s" % str(locator))

    def elements(self, locator):
        return self.driver.find_elements(*locator)

    def assert_text(self, locator, text, n=40):
        """
        assert element's text by polling if match is not found
        maximum poll #40 with approx. ~20 secs
        """
        while n > 1:
            try:
                assert App.element(self, locator).text == text
                break
            except Exception as e:
                time.sleep(0.5)
                n -= 1
                if n is 1: assert App.element(self, locator).text == text

    def is_displayed(self, locator, expected=True, n=3):
        """
        assert boolean value by polling if match is not found
        maximum poll #3 with approx. ~10 secs
        """
        while n > 1:
            try:
                assert self.driver.find_element(*locator).is_displayed() == expected
                break
            except Exception as e:
                n -= 1
                if n is 1: assert False == expected

    def tap(self, locator):
        actions = TouchAction(self.driver)
        actions.tap(App.element(self, locator))
        actions.perform()

    def double_tap(self, locator):
        actions = TouchAction(self.driver)
        actions.tap(App.element(self, locator), count=2)
        actions.perform()

    def click(self, locator):
        App.element(self, locator).click()

    def send_keys(self, locator, text):
        App.element(self, locator).send_keys(text)
