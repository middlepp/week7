
import time

# import webbrowser
#
# # Replace "jenkins_url" with the URL of your Jenkins instance
# jenkins_url = "http://localhost:8080/"
#
# # Open the Jenkins URL in the default web browser
# webbrowser.open(jenkins_url)



from selenium import webdriver

# Replace "jenkins_url" with the URL of your Jenkins instance
jenkins_url = "http://localhost:8080/"

# Create a new instance of the Firefox browser
browser = webdriver.Chrome()

# Navigate to the Jenkins URL
browser.get('http://localhost:8080/')
time.sleep(5)