import time
from math import sin, log
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(log(abs(12*sin(int(x)))))


link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, value='#input_value')
    x = int(x_element.text)
    input1 = browser.find_element(By.CSS_SELECTOR, value='#answer')
    input1.send_keys(calc(x))
    checkBox = browser.find_element(By.CSS_SELECTOR, value='#robotCheckbox')
    checkBox.click()
    radioBox = browser.find_element(By.CSS_SELECTOR, value='#robotsRule')
    radioBox.click()
    button = browser.find_element(By.CSS_SELECTOR, value='button')
    button.click()

finally:
    time.sleep(10)
    browser.quit()

