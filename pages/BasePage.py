from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        super(BasePage, self).__init__()
        self.page_url = str()
        self.driver = driver

    def is_visible(self):
        condition = EC.visibility_of_element_located(self)
        return bool(condition)

    def click(self, locator):
        element = self.driver.find_element(locator[0], locator[1])
        element.click()

    def go_to_page(self):
        self.driver.get(self.page_url)
        return self

    def get_title(self):
        return self.driver.title

    def send_key(self, locator, value):
        element = self.driver.find_element(locator[0], locator[1])
        element.send_keys(value)

