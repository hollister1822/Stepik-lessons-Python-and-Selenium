import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

expected_result = "Congratulations! You have successfully registered!"


def test_form(link):
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.XPATH, "//div[1]/input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.XPATH, "//div[2]/input")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.XPATH, "//div[3]/input")
    input3.send_keys("stella.superbright@gmail.com")

    button = browser.find_element(By.XPATH, '//form/button[contains(text(),"Submit")]')
    button.click()

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")

    welcome_text = welcome_text_elt.text
    return welcome_text


class TestLinks(unittest.TestCase):
    def test_link1(self):
        result = test_form('http://suninjuly.github.io/registration1.html')
        self.assertEqual(result, expected_result, 'Oshibka')

    def test_link2(self):
        result = test_form('http://suninjuly.github.io/registration2.html')
        self.assertEqual(result, expected_result, 'Oshibka')


if __name__ == "__main__":
    unittest.main()