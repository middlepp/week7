from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://the-internet.herokuapp.com/login")
browser.maximize_window()

el = browser.find_element(By.CSS_SELECTOR, "input#username").send_keys('tomsmith')
# # browser.find_element_by_css_selector('input#username').send_keys('tomsmith')
# # browser.find_element(By.CSS_SELECTOR, 'input#username').send_keys('tomsmith')
# # browser.find_element_by_xpath("/html//input[@id='password']")
# # browser.find_element_by_css_selector('.fa.fa-2x.fa-sign-in').click
# # browser.find_e


# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
#
# options = Options()
# # options.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(
#     service=Service(ChromeDriverManager().install()),
#      options=options
#      )
#
# driver.get("https://www.python.org/")
# driver.maximize_window()
#
# input = driver.find_element(By.CSS_SELECTOR,".documentation-widget p")
#
# print(input)
#
# driver.close()
# driver.quit()