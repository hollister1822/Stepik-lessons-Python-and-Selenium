from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from math import log, sin


def calc(x):
    return str(log(12*sin(int(x))))

link = 'http://suninjuly.github.io/alert_accept.html'

try:
    driver = webdriver.Chrome()
    driver.get(link)

    button = driver.find_element(By.CSS_SELECTOR, value='button')
    button.click()

    confirm = driver.switch_to.alert
    confirm.accept()

    x_element = driver.find_element(By.ID, value='input_value')
    x = x_element.text
    answer = driver.find_element(By.ID, value='answer')
    answer.send_keys(calc(x))
    button = driver.find_element(By.TAG_NAME, value='button')
    button.click()



finally:
    sleep(30)
    driver.quit()
