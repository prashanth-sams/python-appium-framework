from src.helpers.appiumdriver import Driver
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

    def assert_text(self, locator, text, n=5):
        """
        assert element's text by polling if match is not found
        maximum poll #4 with approx. ~20 secs
        """
        while n > 1:
            try:
                assert App.element(self, locator).text == text
                break
            except Exception as e:
                time.sleep(5)
                n -= 1
                if n is 1: assert App.element(self, locator).text == text
