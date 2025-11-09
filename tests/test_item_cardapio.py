import pytest
from components.cardapio.item_cardapio import ItemCardapio

class ItemConcreto(ItemCardapio):
  def aplicar_desconto(self):
    self._preco -= 1

def test_item_cardapio_instanciacao():
  item = ItemConcreto(nome="Teste", preco=10)
  assert item._nome == "Teste"
  assert item._preco == 10

def test_item_cardapio_str():
  item = ItemConcreto(nome="Pizza", preco=20)
  assert str(item) == "Pizza"

def test_aplicar_desconto_metodo_concreto():
  item = ItemConcreto(nome="Teste", preco=10)
  item.aplicar_desconto()
  assert item._preco == 9
