import pytest
from selenium.webdriver.common.by import By
import conftest

@pytest.mark.usefixtures("setup_teardown")
class TestLogin:
    def test_login_valido(self):
        driver = conftest.driver
        driver.find_element(By.ID, "username").send_keys("admin")
        driver.find_element(By.ID, "password").send_keys("1234")
        driver.find_element(By.ID, "login-button").click()
        assert driver.find_element(By.ID, "login-status").is_displayed()
