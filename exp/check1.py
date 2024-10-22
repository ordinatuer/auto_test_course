from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "https://suninjuly.github.io/registration2.html"
    browser = webdriver.Edge()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    # По `label` рядом
    input1 = browser.find_element(
        By.XPATH, "//label[text()='First name*']/following-sibling::input")
    input1.send_keys("Alex")
    # По атрибуту `placeholder`
    input2 = browser.find_element(
        By.XPATH, "//input[@placeholder='Input your last name']")
    input2.send_keys("Fix")
    # По структуре (внутри `div` с классом)
    input3 = browser.find_element(
        By.XPATH, "//div[@class='form-group third_class']/input")
    input3.send_keys("reg@gmail.com")
    # По частичному совпадению атрибута `class`
    input4 = browser.find_element(
        By.XPATH, "//input[contains(@placeholder, 'phone')]")
    input4.send_keys("796453746312")
    # По `label` рядом
    input5 = browser.find_element(
        By.XPATH, "//label[text()='Address:']/following-sibling::input")
    input5.send_keys("Irkutsk")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
