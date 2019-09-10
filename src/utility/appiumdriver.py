from appium import webdriver
import unittest
import sys, os
import pdb
from datetime import datetime
import argparse

class Driver(unittest.TestCase):
    
    def __init__(self, driver):
        unittest.TestCase.__init__(self, driver)
        
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = ''
        desired_caps['deviceName'] = 'PF'
        desired_caps['appPackage'] = 'com.wdiodemoapp'
        desired_caps['appActivity'] = 'com.wdiodemoapp.MainActivity'
        
        self.driver = webdriver.Remote("http://0.0.0.0:4723/wd/hub", desired_caps)

    def tearDown(self):
        Driver.screenshot_on_failure(self)
        self.driver.quit()
    
    def screenshot_on_failure(self):
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        test_name = self._testMethodName
        for self._testMethodName, error in self._outcome.errors:
            if error:
                if not os.path.exists('screenshots'):
                    os.makedirs('screenshots')
                    
                self.driver.save_screenshot(f"screenshots/{test_name}_{now}.png")
    
if __name__ == '__main__':
    unittest.main()