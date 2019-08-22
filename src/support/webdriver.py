from appium import webdriver

class Driver:
    
    def __init__(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = ''
        desired_caps['deviceName'] = 'PF'
        desired_caps['appPackage'] = 'com.wdiodemoapp'
        desired_caps['appActivity'] = 'com.wdiodemoapp.MainActivity'
        
        self.driver = webdriver.Remote("http://0.0.0.0:4723/wd/hub", desired_caps)