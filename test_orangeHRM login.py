
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_orangeHRM_login():
    driver=webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    time.sleep(2)


test_orangeHRM_login()  # Call the test function to execute the login test