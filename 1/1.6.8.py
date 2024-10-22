from selenium import webdriver
from selenium.webdriver.common.by import By
import time


try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/huge_form.html")

    elements = browser.find_elements(By.CSS_SELECTOR, "input")
    for el in elements:
        el.send_keys("We kiss the Stars")

    submit_button = browser.find_element(By.CSS_SELECTOR, ".btn-default")
    submit_button.click()

finally:
    time.sleep(30)

    webdriver.close()
    time.sleep(3)
    browser.quit()
