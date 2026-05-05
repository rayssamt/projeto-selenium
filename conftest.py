import pytest
from selenium import webdriver

driver: webdriver.Remote #tornar a variável remota em outros arquivos


@pytest.fixture #essa fixture vai ser usada nas classes em que eu chamá-la
def setup_teardown():
    # setup
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("https://leogcarvalho.github.io/test-automation-practice/")

    # run test
    yield

    # teardown
    driver.quit()