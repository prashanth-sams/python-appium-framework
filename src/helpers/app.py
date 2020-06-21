from src.helpers.appiumdriver import Driver


class App(Driver):

    def __init__(self, driver):
        super().__init__(driver)

    def element(self, locator):
        return self.driver.find_element(*locator)

    def elements(self, locator):
        return self.driver.find_elements(*locator)