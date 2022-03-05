from time import sleep
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://suninjuly.github.io/file_input.html'

try:
    driver = webdriver.Chrome()
    driver.get(link)
    input1 = driver.find_element(By.NAME, value='firstname')
    input1.send_keys('Ivan')
    input2 = driver.find_element(By.NAME, value='lastname')
    input2.send_keys('Ivanov')
    input3 = driver.find_element(By.NAME, value='email')
    input3.send_keys('ivanov@gmail.com')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'short bio.txt')
    file = driver.find_element(By.ID, value='file')
    file.send_keys(file_path)

    button = driver.find_element(By.CSS_SELECTOR, value='button')
    button.click()


finally:
    sleep(30)
    driver.quit()
