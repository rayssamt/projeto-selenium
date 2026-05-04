import pytest
from selenium.webdriver.common.by import By
import conftest
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
class TestLogin:
    def test_login_valido(self):
        driver = conftest.driver
        login_page = LoginPage()
        login_page.fazer_login("admin", "1234")
        assert driver.find_element(By.ID, "login-status").is_displayed()
