from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.edge.service import Service

edge_path = 'edgedriver_win64/msedgedriver.exe'
service = Service(executable_path=edge_path)
driver = webdriver.Edge(service = service)
driver.get('https://the-internet.herokuapp.com/login')

element = driver.find_element(By.CSS_SELECTOR, 'input#username')
element.send_keys('tomsmith')
element = driver.find_element(By.CSS_SELECTOR, 'input#password')
element.send_keys('SuperSecretPassword!')
element = driver.find_element(By.CSS_SELECTOR, '.fa.fa-2x.fa-sign-in').click()


time.sleep(10)
driver.close()
driver.quit()