import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, value='.form-control.first[required]')
    input1.send_keys('test1')
    input2 = browser.find_element(By.CSS_SELECTOR, value='.form-control.second[required]')
    input2.send_keys('test2')
    input3 = browser.find_element(By.CSS_SELECTOR, value='.form-control.third[required]')
    input3.send_keys('test3')

    button = browser.find_element(By.CSS_SELECTOR, value='button.btn')
    button.click()

    time.sleep(1)

    welcome_text = browser.find_element(By.TAG_NAME, value='h1')
    message = welcome_text.text
    assert "Congratulations! You have successfully registered!" == message

finally:
    time.sleep(5)
    browser.quit()
