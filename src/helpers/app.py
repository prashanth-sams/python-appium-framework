from src.helpers.appiumdriver import Driver
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
import time
import logging


class App(Driver):

    def __init__(self, driver):
        super().__init__(driver)

    def element(self, locator, n=3):
        """
        locate an element by polling if element not found
        maximum poll #2 with approx. ~10 secs
        """
        while n > 1:
            try:
                return self.driver.find_element(*locator)
            except Exception as e:
                logging.error(f"element failed attempt - {locator}")
                n -= 1
                if n is 1: raise NoSuchElementException("Could not locate element with value: %s" % str(locator))

    def elements(self, locator):
        return self.driver.find_elements(*locator)

    def assert_text(self, locator, text, n=20):
        """
        assert element's text by polling if match is not found
        maximum poll #20 with approx. ~10 secs
        """
        while n > 1:
            try:
                assert App.element(self, locator).text == text
                break
            except Exception as e:
                logging.error(f'assert_text failed attempt - {locator}')
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
                logging.error(f'is_displayed failed attempt - {locator}')
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

    def skip_if_not_available(self, locator, action='click', text=''):
        try:
            if action == 'click': App.click(self, locator)
            if action == 'send_keys': App.send_keys(self, locator, text)
        except Exception as e:
            print('skip this step if not available')