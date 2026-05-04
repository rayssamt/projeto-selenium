import pytest
from selenium.webdriver.common.by import By
from conftest import driver

@pytest.mark.usefixtures("setup_teardown")
class TestLoginInvalido:
    def test_login_invalido(self):
        driver.find_element(By.ID, "username").send_keys("admi")
        driver.find_element(By.ID, "password").send_keys("123")
        driver.find_element(By.ID, "login-button").click()
        assert not driver.find_element(By.ID, "login-status").is_displayed()