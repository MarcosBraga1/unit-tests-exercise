import pytest
from components.cardapio.bebida import Bebida

def test_instanciacao_bebida():
  bebida = Bebida(nome="Suco de Laranja", preco=10.0, tamanho="300ml")

  assert bebida._nome == "Suco de Laranja"
  assert bebida._preco == 10.0
  assert bebida.tamanho == "300ml"

def test_aplicar_desconto_bebida():
  bebida = Bebida(nome="Refrigerante", preco=12.50, tamanho="350ml")
  bebida.aplicar_desconto()

  assert bebida._preco == pytest.approx(11.5)
