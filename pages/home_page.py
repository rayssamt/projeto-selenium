from selenium.webdriver.common.by import By

import conftest
from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.id_aviso_sucessful = (By.ID, "login-status")

    def verificar_login_com_sucesso(self):
        self.verificar_se_elemento_existe(self.id_aviso_sucessful)