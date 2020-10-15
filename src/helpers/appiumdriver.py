from appium import webdriver
import unittest
import os
from datetime import datetime
import pytest
from src.helpers.business import *
from pytest_html_reporter import attach


class Driver(unittest.TestCase):

    def __init__(self, driver):
        super().__init__(driver)

    def setUp(self):
        """
        This method instantiates the appium driver
        """
        global desired_caps

        self.logger.info("Configuring desired capabilities")
        if os.getenv('PYTEST_XDIST_WORKER'):
            if self.app == 'ios':
                desired_caps = {
                    'deviceName': 'iPhone 8',
                    'platformName': 'iOS',
                    'platformVersion': '13.3',
                    'automationName': 'XCUITest',
                    'app': f'{os.popen("pwd").read().rstrip()}/data/apps/iOS-Simulator-NativeDemoApp-0.2.1.app'
                }

            elif self.app == 'android':
                desired_caps = {
                    'platformName': 'Android',
                    'platformVersion': '',
                    'deviceName': 'PF',
                    'wdaLocalPort': Driver.wda_port(self),
                    'udid': Driver.android_device_name(self),
                    'app': f'{os.popen("pwd").read().rstrip()}/data/apps/app-staging-debug.apk',
                    'noReset': True
                }

        else:
            if self.app == 'ios':
                desired_caps = self.ios()

            elif self.app == 'android':
                desired_caps = self.android()

        self.logger.info("Initiating Appium driver")
        self.driver = webdriver.Remote("http://0.0.0.0:4723/wd/hub", desired_caps)

        # set waits
        self.driver.implicitly_wait(5)  # waits 5 seconds

    def android(self):
        if self.device == 'emulator':
            return dict(platformName='Android', platformVersion='', deviceName='PF',
                        app=f'{os.popen("pwd").read().rstrip()}/data/apps/Android-NativeDemoApp-0.2.1.apk', noReset=True)
        elif self.device == 'real device':
            return dict(platformName='Android', platformVersion='', deviceName='PF',
                        app=f'{os.popen("pwd").read().rstrip()}/data/apps/Android-NativeDemoApp-0.2.1.apk', noReset=True)

    def ios(self):
        if self.device == 'simulator':
            return dict(platformName='iOS', platformVersion='13.3', deviceName='iPhone 11',
                        app=f'{os.popen("pwd").read().rstrip()}/data/apps/iOS-Simulator-NativeDemoApp-0.2.1.app',
                        automationName='XCUITest')
        elif self.device == 'real device':
            return dict(platformName='iOS', platformVersion='14.0', deviceName='iPhone X',
                        udid=f'{UDID}', useNewWDA=True,
                        app=f'{os.popen("pwd").read().rstrip()}/data/apps/iOS-RealDevice-NativeDemoApp-0.2.1.ipa',
                        automationName='XCUITest')
        elif self.device == 'bitrise':
            return dict(platformName='iOS', platformVersion='13.0', deviceName='iPhone-11',
                        udid='E04A6F53-4C3B-4810-B210-DD2015D0D064', useNewWDA=True,
                        app=f'{os.popen("pwd").read().rstrip()}/data/apps/iOS-Simulator-NativeDemoApp-0.2.1.app', automationName='XCUITest')

    def tearDown(self):
        Driver.screenshot_on_failure(self)
        attach(data=self.driver.get_screenshot_as_png())
        self.driver.quit()

    def screenshot_on_failure(self):
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        test_name = self._testMethodName
        for self._testMethodName, error in self._outcome.errors:
            if error:
                self.logger.error("Taking screenshot on failure")
                if not os.path.exists('screenshots'):
                    os.makedirs('screenshots')

                self.driver.save_screenshot(f"screenshots/{test_name}_{now}.png")

    @pytest.fixture(autouse=True)
    def cli(self, app, device, get_logger):
        self.app = app
        self.device = device
        self.logger = get_logger

    def wda_port(self):
        if os.getenv('PYTEST_XDIST_WORKER') == 'gw1':
            return 8101
        else:  # include 'master' and 'gw0'
            return 8100

    def android_device_name(self):
        if os.getenv('PYTEST_XDIST_WORKER') == 'gw0':
            return 'emulator-5554'
        elif os.getenv('PYTEST_XDIST_WORKER') == 'gw1':
            return 'emulator-5556'
        else:  # default
            return 'emulator-5554'


if __name__ == '__main__':
    unittest.main()
