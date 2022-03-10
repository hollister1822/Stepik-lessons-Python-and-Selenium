import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def br():
    print('\nstart browser...')
    br = webdriver.Chrome()
    yield br
    print('\nquit browser...')
    br.quit()
