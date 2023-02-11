from selenium import webdriver

from home_page import HomePage

class TestFirstUi:
    """

    """
    def test_open_browser(self):
        """

        :return:
        """

        driver = webdriver.Chrome()
        page = HomePage(driver)
        page.visit()
        assert page.has_page_name('Python')
        page.search_for_text('bla')
        assert page.has_no_results()
        driver.quit()

