from selenium.webdriver.common.by import By
from Config.TestData import as TD
from Pages.BasePage import BasePage

class GoogleSearchPage(BasePage):

    TITLE = 'Google'
    LOGO = (By.XPATH, "/html/body/div[1]/div[2]/div/img")
    key_path = (By.XPATH, "html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
    text_search = "hello"
    search_btn = (By.XPATH, "html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]")

    def __init__(self, driver)
        super(GoogleSearchPage, self).__init(driver)
        self.page_url = TD.URL