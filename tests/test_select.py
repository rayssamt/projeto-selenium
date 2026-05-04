from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://leogcarvalho.github.io/test-automation-practice/index.html")

dropdown = Select(driver.find_element(By.ID, "dropdown"))
dropdown.select_by_index(1)
assert driver.find_element(By.XPATH, "//option[@value='option2']").is_selected()
