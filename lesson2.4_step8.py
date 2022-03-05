from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from time import sleep
from math import log, sin


def calc(x):
    return str(log(12*sin(int(x))))

link = 'http://suninjuly.github.io/explicit_wait2.html'

try:
    driver = webdriver.Chrome()
    driver.get(link)
    WebDriverWait(driver, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '100'))
    button = driver.find_element(By.ID, value='book')
    button.click()
    driver.execute_script("window.scrollBy(0, 250);")

    x_element = driver.find_element(By.ID, value='input_value')
    x = x_element.text
    answer = driver.find_element(By.ID, value='answer')
    answer.send_keys(calc(x))

    button = driver.find_element(By.ID, value='solve')
    button.click()

finally:
    sleep(20)
    driver.quit()

