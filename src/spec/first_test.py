import unittest
from time import sleep
from appium import webdriver
import pdb

class AppiumTest(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = ''
        desired_caps['deviceName'] = 'PF'
        desired_caps['appPackage'] = 'com.wdiodemoapp'
        desired_caps['appActivity'] = 'com.wdiodemoapp.MainActivity'
        self.driver = webdriver.Remote("http://0.0.0.0:4723/wd/hub", desired_caps)
    
    def tearDown(self):
        self.driver.quit()
    
    def test_demo(self):
        self.driver.find_element_by_id("Login").click()
        self.driver.find_element_by_id("input-email").send_keys("johnsmith@gmail.com")
        self.driver.find_element_by_id("input-password").send_keys("password")
        self.driver.find_element_by_id("button-LOGIN").click()
        # pdb.set_trace()