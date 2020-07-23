from src.helpers.appiumdriver import Driver
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
import time
import logging


def keyword_check(kwargs):
    kc = {}
    if 'index' in kwargs: kc['index'] = 'elements'
    if 'index' not in kwargs: kc['index'] = 'element'
    return ''.join(kc.values())


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

    def elements(self, locator, n=3):
        """
        locate element list by polling if the element list is not found
        maximum poll #2 with approx. ~10 secs
        """
        x = iter(CustomCall())
        while n > 1:
            try:
                return self.driver.find_elements(*locator)
            except Exception as e:
                logging.error(f"element list failed attempt {next(x)} - {locator}")
                n -= 1
                if n == 1: raise NoSuchElementException("Could not locate element list with value: %s" % str(locator))

    # need refactor on condition
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

    # need refactor on condition
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
        """
        custom wrapped single tap method
        -> wait until display
        -> element(s)
        """
        App.is_displayed(self, locator, True)

        actions = TouchAction(self.driver)
        return {
            'element': lambda x: actions.tap(App.element(self, locator)).perform(),
            'elements': lambda x: actions.tap(App.elements(self, locator)[kwargs['index']]).perform()
        }[keyword_check(kwargs)]('x')

    def double_tap(self, locator, **kwargs):
        """
        custom wrapped double tap method
        -> wait for element until display
        -> element(s)
        """
        App.is_displayed(self, locator, True)

        actions = TouchAction(self.driver)
        return {
            'element': lambda x: actions.tap(App.element(self, locator), count=2).perform(),
            'elements': lambda x: actions.tap(App.elements(self, locator)[kwargs['index']], count=2).perform()
        }[keyword_check(kwargs)]('x')

    def click(self, locator, **kwargs):
        """
        custom wrapped click method
        -> wait for element until display
        -> element(s)
        """
        App.is_displayed(self, locator, True)

        return {
            'element': lambda x: App.element(self, locator).click(),
            'elements': lambda x: App.elements(self, locator)[kwargs['index']].click()
        }[keyword_check(kwargs)]('x')

    def send_keys(self, locator, text='', **kwargs):
        """
        custom wrapped send_keys method
        -> wait for element until display
        -> element(s)
        """
        App.is_displayed(self, locator, True)

        return {
            'element': lambda text: App.element(self, locator).send_keys(text),
            'elements': lambda text: App.elements(self, locator)[kwargs['index']].send_keys(text)
        }[keyword_check(kwargs)](text)

    def skip_if_not_available(self, locator, action='click', text='', **kwargs):
        """
        optional method
        -> element(s)
        """
        try:
            if keyword_check(kwargs) == 'element':
                return {
                    'click': lambda x: App.click(self, locator),
                    'send_keys': lambda x: App.send_keys(self, locator, text=text),
                    'tap': lambda x: TouchAction(self.driver).tap(App.element(self, locator)).perform()
                }[action]('x')
            elif keyword_check(kwargs) == 'elements':
                return {
                    'click': lambda x: App.click(self, locator, index=kwargs['index']),
                    'send_keys': lambda x: App.send_keys(self, locator, text=text, index=kwargs['index']),
                    'tap': lambda x: TouchAction(self.driver).tap(
                        App.elements(self, locator)[kwargs['index']]).perform()
                }[action]('x')
        except Exception as e:
            print('skip this step if not available')

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

    def launch_app(self):
        self.driver.launch_app()


class CustomCall:

    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        k = self.a
        self.a += 1
        return k
