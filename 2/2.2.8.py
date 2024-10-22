from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/file_input.html")

    browser.find_element(By.NAME, "firstname").send_keys("Jane")
    browser.find_element(By.NAME, "lastname").send_keys("Doe")
    browser.find_element(By.NAME, "email").send_keys("empty_email@jd.com")

    file = os.path.join(os.path.abspath(os.path.dirname(__file__)), "upload_file.txt")
    upload_el = browser.find_element(By.NAME, "file").send_keys(file)

    browser.find_element(By.TAG_NAME, "button").click()
finally:
    time.sleep(20)
    browser.quit()

# print("-----------------------")
# print(os.path.abspath(__file__))

# dir_name = os.path.abspath(os.path.dirname(__file__))
# print(dir_name)
# print("-----------------------")

# new_file_name = os.path.join(dir_name, "new_file.csv")

# print(new_file_name)
# print("-----------------------")
