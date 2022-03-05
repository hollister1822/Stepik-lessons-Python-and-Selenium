import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By


link = 'http://suninjuly.github.io/find_link_text'


try:
    browser = webdriver.Chrome()
    browser.get(link)
    link = browser.find_element(By.LINK_TEXT, value=str(math.ceil(math.pow(math.pi, math.e)*10000)))
    link.click()

    input1 = browser.find_element(By.TAG_NAME, value='[name="first_name"]')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, value='last_name')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, value="form-control.city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, value="country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, value="button.btn")
    button.click()


finally:
    time.sleep(30)
    browser.quit()
