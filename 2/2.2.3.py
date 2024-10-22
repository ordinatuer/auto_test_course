from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

try:
	browser = webdriver.Chrome()
	browser.get("https://suninjuly.github.io/selects1.html")

	num1 = int(browser.find_element(By.ID, "num1").text)
	num2 = int(browser.find_element(By.ID, "num2").text)

	select = Select(browser.find_element(By.ID, "dropdown"))
	select.select_by_visible_text(str(num1 + num2))

	browser.find_element(By.TAG_NAME, "button").click()

finally:
	time.sleep(20)
	browser.quit()