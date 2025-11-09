import pytest
from components.cardapio.prato import Prato

def test_instanciacao_prato():
  prato = Prato(nome="Feijoada", preco=50.0, descricao="Típico prato brasileiro")

  assert prato._nome == "Feijoada"
  assert prato._preco == 50.0
  assert prato.descricao == "Típico prato brasileiro"


def test_aplicar_desconto_prato():
  prato = Prato(nome="Lasanha", preco=40.0, descricao="Com muito queijo")
  prato.aplicar_desconto()

  assert prato._preco == pytest.approx(38.0)
