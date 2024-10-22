from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/redirect_accept.html")

    browser.find_element(By.TAG_NAME, "button").click()
    browser.switch_to.window(browser.window_handles[1])

    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)

    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.TAG_NAME, "button").click()
finally:
    time.sleep(20)
    browser.quit()
