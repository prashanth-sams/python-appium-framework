from appium.webdriver.common.mobileby import MobileBy


class LoginLocators(object):
    """
    login screen locators
    """
    inputField = (MobileBy.XPATH, '//android.widget.EditText[@content-desc="input-email"]')
    passwordField = (MobileBy.ACCESSIBILITY_ID, 'input-password')
    loginButton = (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="button-LOGIN"]/android.view.ViewGroup')