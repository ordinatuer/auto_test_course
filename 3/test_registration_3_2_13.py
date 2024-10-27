from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time

class TestRegistration(unittest.TestCase):
    name = "John"
    lastname = "Doe"
    email = "johndoe@epost.em"
    registrtion_ok_text = "Congratulations! You have successfully registered!"

    reg1 = "https://suninjuly.github.io/registration1.html"
    reg2 = "https://suninjuly.github.io/registration2.html"

    def test_form1(self):
        text = self.registrtion_test(self.reg1)

        self.assertEqual(self.registrtion_ok_text, text, "Регистрация на первой форме провалена (╯°□°）╯︵ ┻━┻")

    def test_form2(self):
        text = self.registrtion_test(self.reg2)

        self.assertEqual(self.registrtion_ok_text, text, "Регистрация на второй форме провалена (╯°□°）╯︵ ┻━┻")

    def registrtion_test(self, url):
        self.browser.get(url)

        self.browser.find_element(By.CSS_SELECTOR, ".first_block .first").send_keys(self.name)
        self.browser.find_element(By.CSS_SELECTOR, ".first_block .second").send_keys(self.lastname)
        self.browser.find_element(By.CSS_SELECTOR, ".first_block .third").send_keys(self.email)

        self.browser.find_element(By.CSS_SELECTOR, "button.btn").click()

        time.sleep(2)

        return self.browser.find_element(By.TAG_NAME, "h1").text

    def setUp(self):
        self.browser = webdriver.Chrome()

if __name__ == "__main__":
    unittest.main()
