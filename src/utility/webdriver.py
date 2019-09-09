from appium import webdriver
import unittest

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
        self.driver.quit()
    
if __name__ == '__main__':
    unittest.main()