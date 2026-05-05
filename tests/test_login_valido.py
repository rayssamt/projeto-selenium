import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown") #chamando a fixture do método setup_teardown do arquivo conftest
@pytest.mark.login
class TestLoginValido: #o nome da classe pode ser o nome do caso de teste
    def test_login_valido(self):
        # fazer login -> não faz parte do teste, o teste só verifica se o login feito é valido
        # a funcao de fazer o login deve ser feita na página de login e ser chamada aqui
        # verificar login -> verificar 

        login_page = LoginPage()
        # home_page = HomePage()
        #
        login_page.fazer_login("admin", "1234")
        #
        # home_page.verificar_login_com_sucesso()