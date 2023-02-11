from selenium import webdriver
from selenium.webdriver.common.by import By
import time

edge_path = 'edgedriver_win64/msedgedriver.exe'
driver = webdriver.Edge(executable_path=edge_path)
driver.get('https://the-internet.herokuapp.com/login')

element = driver.find_element(By.CSS_SELECTOR, 'input#username')
element.send_keys('tomsmith')
element = driver.find_element(By.CSS_SELECTOR, 'input#password')
element.send_keys('SuperSecretPassword!')
element = driver.find_element(By.CSS_SELECTOR, '.fa.fa-2x.fa-sign-in').click()

# assert_message = driver.find_element(By.CSS_SELECTOR, 'h2').text
# print(assert_message)

time.sleep(10)
driver.close()
driver.quit()