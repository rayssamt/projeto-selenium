from selenium.webdriver.common.by import By
import conftest
from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self):
        self.driver = conftest.driver #chamar as configuracoes de inicializacao do selenium e pytest
        self.username_locator = (By.ID, "username")
        self.password_locator = (By.ID, "password")
        self.login_button = (By.XPATH, "//span[@class='title']")
        #também posso ter variaveis que vão se repetir ao longo do código, como essas com os locators de id e xpath

    def fazer_login(self, usuario, senha):
        #as açoes de procurar o elemento, enviar o parâmetro, clicar e tudo mais, não é exclusivo do login, é genérico e podem ser feitas numa pagina base
        # o metodo de login deve enviar o nome do usuario e senha (send_keys) pra um elemento que vamos achar através do find_element
        self.escrever(self.username_locator, usuario) #parametro: locator e o nome do usuario
        self.escrever(self.password_locator, senha)  #parametro: locator e senha
        self.clicar(self.login_button)
        #posso usar o self.metodosDaBasePage porque passei a BasePage como parametro aqui na LoginPage

        # driver.find_element(By.ID, "user-name").send_keys("standard_user")
        # driver.find_element(By.ID, "password").send_keys("secret_sauce")
        # driver.find_element(By.ID, "login-button").click()