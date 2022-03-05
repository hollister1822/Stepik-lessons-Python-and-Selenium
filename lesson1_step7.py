import time
from math import log, sin
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
  return str(log(abs(12*sin(int(x)))))


link = 'http://suninjuly.github.io/get_attribute.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.ID, value='treasure')
    x = x_element.get_attribute('valuex')
    input_answer = browser.find_element(By.CSS_SELECTOR, value='#answer')
    input_answer.send_keys(calc(x))
    checkBox = browser.find_element(By.ID, value='robotCheckbox')
    checkBox.click()
    radio = browser.find_element(By.ID, value='robotsRule')
    radio.click()
    button = browser.find_element(By.CSS_SELECTOR, value='button')
    button.click()

finally:
    time.sleep(10)
    browser.quit()
