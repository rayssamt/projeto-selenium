import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
class TestLogin:
    def test_login_valido(self):
        login_page = LoginPage()
        home_page = HomePage()

        login_page.fazer_login("admin", "1234")

        home_page.verificar_login_com_sucesso()

