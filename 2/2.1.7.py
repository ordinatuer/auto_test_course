from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/get_attribute.html")

    x = browser.find_element(By.ID, "treasure").get_attribute("valuex")
    y = calc(x)

    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()

    browser.find_element(By.TAG_NAME, "button").click()
finally:
    time.sleep(10)
    browser.close()
