from tests.fixtures import restaurante_fixture
from io import StringIO
import sys


def teste_exibir_cardapio(restaurante_fixture):
    """Testa se o método exibir_cardapio exibe corretamente o cardápio do restaurante"""
    restaurante = restaurante_fixture
   
    captured_output = StringIO()
    sys.stdout = captured_output
   
    restaurante.exibir_cardapio
       # Restaura a saída padrão
    sys.stdout = sys.__stdout__

    output = captured_output.getvalue()
   
    assert restaurante._nome in output
   
    assert len(output.strip()) > 0

    assert "R$" in output