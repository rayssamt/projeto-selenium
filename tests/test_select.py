import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from conftest import driver

@pytest.mark.usefixtures("setup_teardown")
class TestSelect:
    def test_select_dropdown(self):
        dropdown = Select(driver.find_element(By.ID, "dropdown"))
        dropdown.select_by_index(1)
        assert driver.find_element(By.XPATH, "//option[@value='option2']").is_selected()
