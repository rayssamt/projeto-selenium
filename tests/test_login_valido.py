from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://leogcarvalho.github.io/test-automation-practice/")

driver.find_element(By.ID, "username").send_keys("admin")
driver.find_element(By.ID, "password").send_keys("1234")
driver.find_element(By.ID, "login-button").click()
assert driver.find_element(By.ID, "login-status").is_displayed()
#numa aplicção onde roda o comando várias vezes, add o refresh() no final para a mensagem do 'login-status'desaparecer

