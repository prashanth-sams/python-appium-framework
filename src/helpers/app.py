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
        x = iter(CustomCall())
        while n > 1:
            try:
                return self.driver.find_element(*locator)
            except Exception as e:
                logging.error(f"element failed attempt {next(x)} - {locator}")
                n -= 1
                if n == 1: raise NoSuchElementException("Could not locate element with value: %s" % str(locator))

    def elements(self, locator):
        return self.driver.find_elements(*locator)

    def assert_text(self, locator, text, n=20, **kwargs):
        """
        assert element's text by polling if match is not found
        maximum poll #20 with approx. ~10 secs
        """
        App.is_displayed(self, locator, True)

        x = iter(CustomCall())
        while n > 1:
            try:
                if len(kwargs) == 0:
                    assert App.element(self, locator).text == text
                else:
                    assert App.element(self, locator)[kwargs['index']].text == text
                break
            except Exception as e:
                logging.error(f'assert_text failed attempt {next(x)}- {locator}')
                time.sleep(0.5)
                n -= 1
                if len(kwargs) == 0:
                    if n == 1: assert App.element(self, locator).text == text
                else:
                    if n == 1: assert App.element(self, locator)[kwargs['index']].text == text

    def is_displayed(self, locator, expected=True, n=3, **kwargs):
        """
        assert boolean value by polling if match is not found
        maximum poll #3 with approx. ~10 secs
        """
        x = iter(CustomCall())
        while n > 1:
            try:
                if len(kwargs) == 0:
                    assert self.driver.find_element(*locator).is_displayed() == expected
                else:
                    assert self.driver.find_element(*locator)[kwargs['index']].is_displayed() == expected
                break
            except Exception as e:
                logging.error(f'is_displayed failed attempt {next(x)}- {locator}')
                n -= 1
                if n == 1: assert False == expected

    def tap(self, locator, **kwargs):
        actions = TouchAction(self.driver)
        if len(kwargs) == 0:
            actions.tap(App.element(self, locator))
        else:
            actions.tap(App.element(self, locator)[kwargs['index']])
        actions.perform()

    def double_tap(self, locator, **kwargs):
        actions = TouchAction(self.driver)
        if len(kwargs) == 0:
            actions.tap(App.element(self, locator), count=2)
        else:
            actions.tap(App.element(self, locator)[kwargs['index']], count=2)
        actions.perform()

    def click(self, locator, **kwargs):
        if len(kwargs) == 0:
            App.element(self, locator).click()
        else:
            App.elements(self, locator)[kwargs['index']].click()

    # text to be under arbitrary keyword
    def send_keys(self, locator, text, **kwargs):
        if len(kwargs) == 0:
            App.element(self, locator).send_keys(text)
        else:
            App.elements(self, locator)[kwargs['index']].send_keys(text)

    # Need fix for kwargs elements
    def skip_if_not_available(self, locator, action='click', text=''):
        {
            'click': App.click(self, locator),
            'send_keys': App.send_keys(self, locator, text)
        }.get(action, 'Action not available')

    def get_screen_size(self):
        return self.driver.get_window_size()

    def back(self):
        """
        generally minimize app
        """
        self.driver.back()

    def close(self):
        self.driver.close_app()

    def reset(self):
        self.driver.reset()


class CustomCall:

    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        k = self.a
        self.a += 1
        return k