import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def br():
    print('\nstart browser for test...')
    br = webdriver.Chrome()
    yield br
    print('\nquit browser for test...')
    br.quit()
