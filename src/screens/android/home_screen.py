from appium.webdriver.common.mobileby import MobileBy


class HomeLocators(object):
    """
    home screen screens
    """
    loginMenu = (MobileBy.XPATH, "//android.view.ViewGroup[@content-desc='Login']/android.widget.TextView")
    formsMenu = (MobileBy.ACCESSIBILITY_ID, "Forms")
    homeMenu = (MobileBy.ACCESSIBILITY_ID, "Home")
    swipeMenu = (MobileBy.ACCESSIBILITY_ID, "Swipe")

    # swipeMenu = {'ANDROID': (MobileBy.ACCESSIBILITY_ID, "Swipe"),'IOS': (MobileBy.ACCESSIBILITY_ID, "Swipe")}