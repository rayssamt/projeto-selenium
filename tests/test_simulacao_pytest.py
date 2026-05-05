# pytest nome_arquivo.py
# pytest -v nome_arquivo.py para teste mais detalhado
# pytest nome_arquivo.py::nome_teste para testar apenas um método
import pytest

# @pytest.mark.simulacao -> posso usar marcador a nível da classe também
# uma boa prática é ter apenas 1 método de teste por classe
class TestSumulacao():

    @pytest.mark.simulacao  # marcador para o nome do teste. executar usando: pytest nome_arquivo -m nome_marcador
    @pytest.mark.cadastro  # pytest test_simulacao_pytest -m cadastro
    def test_simulacao_1(self):
        assert 1==1

    @pytest.mark.skip # pular teste
    def test_simulacao_2(self):
        assert 1==1