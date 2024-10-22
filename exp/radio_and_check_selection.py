from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
	browser = webdriver.Chrome()
	browser.get("https://suninjuly.github.io/math.html")

	checkbox_input = browser.find_element(By.ID, "robotCheckbox").get_attribute("checked")
	people_radio_input = browser.find_element(By.ID, "peopleRule").get_attribute("checked")
	robots_radio_input = browser.find_element(By.ID, "robotsRule").get_attribute("checked")

	print(f'{checkbox_input} | {people_radio_input} | {robots_radio_input}')

finally:
	time.sleep(5)
	browser.quit()