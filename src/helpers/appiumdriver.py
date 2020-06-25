from appium import webdriver
import unittest
import os
from datetime import datetime
import pytest
import logging

logging.FileHandler('app.log', mode='w')
logging.basicConfig(
    filename='app.log',
    format='%(asctime)s - %(levelname)s: %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p',
    level=logging.INFO
)


class Driver(unittest.TestCase):

    def __init__(self, driver):
        super().__init__(driver)

    def setUp(self):
        """
        This method instantiates the appium driver
        """
        Driver.cli

        logging.info("Configuring desired capabilities")
        if os.getenv('PYTEST_XDIST_WORKER'):
            if self.app == 'ios':
                desired_caps = {
                    'platformName': 'ios',
                    'platformVersion': '',
                    'deviceName': 'PF'
                }

            elif self.app == 'android':
                desired_caps = {
                    'platformName': 'Android',
                    'platformVersion': '',
                    'deviceName': 'PF',
                    'wdaLocalPort': Driver.wda_port(self),
                    'udid': Driver.android_device_name(self),
                    'app': '/Users/prashanth/Projects/apps/app-staging-debug.apk'
                }

        else:
            if self.app == 'ios':
                desired_caps = {
                    'platformName': 'ios',
                    'platformVersion': '',
                    'deviceName': 'PF'
                }

            elif self.app == 'android':
                desired_caps = {
                    'platformName': 'Android',
                    'platformVersion': '',
                    'deviceName': 'PF',
                    'app': '/Users/prashanth/Projects/apps/app-staging-debug.apk'
                }

        logging.info("Initiating Appium driver")
        self.driver = webdriver.Remote("http://0.0.0.0:4723/wd/hub", desired_caps)

        # set waits
        self.driver.implicitly_wait(5)  # waits 5 seconds

    def tearDown(self):
        Driver.screenshot_on_failure(self)
        self.driver.quit()

    def screenshot_on_failure(self):
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        test_name = self._testMethodName
        for self._testMethodName, error in self._outcome.errors:
            if error:
                logging.error("Taking screenshot on failure")
                if not os.path.exists('screenshots'):
                    os.makedirs('screenshots')

                self.driver.save_screenshot(f"screenshots/{test_name}_{now}.png")

    @pytest.fixture(autouse=True)
    def cli(self, app):
        self.app = app

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
