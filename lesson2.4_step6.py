from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://suninjuly.github.io/cats.html'

try:
    driver = webdriver.Chrome()
    driver.get(link)
    driver.find_element(By.ID, value='button')

finally:
    driver.quit()
