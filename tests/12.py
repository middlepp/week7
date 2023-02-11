# import By
import pytest
from selenium import webdriver


# create a new Google Chrome browser session
driver = webdriver.Chrome()

# navigate to the application home page
driver.get("https://www.google.com")

# get the search textbox
search_field = driver.find_element(By.NAME, "r")

# enter search keyword and submit
search_field.send_keys("Selenium WebDriver")
search_field.submit()



# get the list of elements which are displayed after the search
# currently on result page using find_elements_by_class_name method
# lists = driver.find_elements_by_class_name("r")
lists = driver.find_element(By.NAME, "r")

# get the number of elements found
print("Found " + str(len(lists)) + " searches:")

# iterate through each element and print the text that is
# name of the search
for listitem in lists:
    print(listitem.get_attribute("innerHTML"))

# close the browser window
driver.quit()