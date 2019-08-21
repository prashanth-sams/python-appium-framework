import unittest
from time import sleep
from appium import webdriver


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
        app_name = self.driver.find_elements_by_link_text("Demo app for the appium-boilerplate")
        

# class Driver:

#     def __init__(self):

#         desired_caps = {
#             'platformName': 'android',
#             'deviceName': 'OnePlus 6',
#             'appPackage': 'com.oneplus.calculator',
#             'appActivity': 'com.oneplus.calculator.Calculator'
#         }

#         self.instance = webdriver.Remote("http://0.0.0.0:4723/wd/hub", desired_caps)