import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import chrome

from selenium import webdriver
driver = webdriver.Chrome()

class TestJenkinsIsUp:

    def test_jenkins_is_up(self):
        driver.get("http://localhost:8080/")
        print("****************************************")

        try:
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'j_username')))
            print("PASS")

        except:
            print("Not Found")
            print(driver.title, "!!!!!!")
time.sleep(5)