import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://suninjuly.github.io/huge_form.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    elements = browser.find_elements(By.CSS_SELECTOR, value='[type="text"]')
    for element in elements:
        element.send_keys('Бла')

    button = browser.find_element(By.CSS_SELECTOR, value='button.btn')
    button.click()

finally:
    time.sleep(30)
    browser.quit()
