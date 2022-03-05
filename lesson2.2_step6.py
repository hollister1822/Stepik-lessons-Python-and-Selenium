from time import sleep
from math import log, sin
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(log(12*sin(int(x))))


link = 'http://suninjuly.github.io/execute_script.html'

try:
    driver = webdriver.Chrome()
    driver.get(link)
    x_element = driver.find_element(By.ID, value='input_value')
    x = x_element.text
    driver.execute_script("window.scrollBy(0, 140);")
    input_answer = driver.find_element(By.ID, value='answer')
    input_answer.send_keys(calc(x))
    checkBox = driver.find_element(By.ID, value='robotCheckbox')
    checkBox.click()
    robotsRule = driver.find_element(By.ID, value='robotsRule')
    robotsRule.click()
    button = driver.find_element(By.CSS_SELECTOR, value='button')
    button.click()


finally:
    sleep(30)
    driver.quit()
