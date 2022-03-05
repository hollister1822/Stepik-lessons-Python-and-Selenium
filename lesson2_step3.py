from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(a, b):
    return str(int(a) + int(b))


link = 'http://suninjuly.github.io/selects1.html'

try:
    driver = webdriver.Chrome()
    driver.get(link)

    element_a = driver.find_element(By.ID, value='num1')
    a = element_a.text
    element_b = driver.find_element(By.ID, value='num2')
    b = element_b.text
    num = calc(a, b)

    elements = driver.find_elements(By.CSS_SELECTOR, value='option')
    for row in elements:
        if row.text == num:
            row.click()
            break

    button = driver.find_element(By.CSS_SELECTOR, value='button')
    button.click()




finally:
    sleep(30)
    driver.quit()
