from selenium import webdriver

import pytest

@pytest.fixture(scope="class", params=['firefox', 'chrome'], autouse=True)
def driver(request):
    if request.params == 'firefox':
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()

    return driver