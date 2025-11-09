import pytest
from unittest.mock import patch, mock_open, MagicMock
from components.sabor_express import SaborExpress
from tests.fixtures import avaliacao_restaurante_fixture, restaurante_fixture, sabor_express_object_fixture, sobremesa_fixture

def test_escolher_restaurante(sabor_express_object_fixture):
  sabor_express = sabor_express_object_fixture
  restaurante_escolhido = sabor_express.escolher_restaurante(1)

  assert restaurante_escolhido._nome == "Restaurante 1"

def test_escolher_pedido(sabor_express_object_fixture):
  sabor_express = sabor_express_object_fixture
  restaurante_escolhido = sabor_express.escolher_restaurante(1)

  pedido_escolhido = sabor_express.escolher_pedido(restaurante_escolhido, 1)

  assert pedido_escolhido._nome == "Item 1"

@patch("builtins.open", new_callable=mock_open, read_data='[{"nome": "Rest A"}]')
@patch("components.sabor_express.Restaurantes")
def test_obter_restaurantes(mock_restaurantes, mock_file):
  s = SaborExpress()
  mock_restaurantes.return_value = "obj_restaurantes"

  s.obter_restaurantes()

  mock_file.assert_called_once_with("data/restaurants_db.json")
  mock_restaurantes.assert_called_once()
  assert s._restaurantes == "obj_restaurantes"

@patch("builtins.print")
def test_calcular_preco_com_desconto(mock_print, sobremesa_fixture):
  pedido = sobremesa_fixture
  pedido.aplicar_desconto = MagicMock()
  s = SaborExpress()

  s.calcular_preco(pedido, "S")

  pedido.aplicar_desconto.assert_called_once()
  mock_print.assert_called_once()

@patch("builtins.print")
def test_calcular_preco_sem_desconto(mock_print, sobremesa_fixture):
  pedido = sobremesa_fixture
  pedido.aplicar_desconto = MagicMock()
  s = SaborExpress()

  s.calcular_preco(pedido, "N")

  pedido.aplicar_desconto.assert_not_called()
  mock_print.assert_called_once_with(f"O pedido ficou por {pedido._preco:.2f}")

@patch("builtins.input", side_effect=["5", "Excelente!"])
@patch("builtins.open", new_callable=mock_open)
@patch("json.dump")
def test_avaliar_pedido(mock_dump, mock_file, mock_input, sabor_express_object_fixture):
  s = sabor_express_object_fixture

  restaurante = s._restaurantes._lista_de_restaurantes[0]
  restaurante._avaliacoes.media = 5
  restaurante._avaliacoes.avaliacoes_individuais = []

  s.avaliar_pedido(0)

  mock_input.assert_any_call("Nota (1 a 5):")
  mock_input.assert_any_call("Comentário:")
  mock_file.assert_called_once_with("nova_avaliacao.json", "w", encoding="utf-8")
  mock_dump.assert_called_once()

@patch("builtins.input", side_effect=["1", "2", "N", "N"])
@patch("builtins.print")
def test_iniciar_interface_de_pedidos(mock_print, mock_input, sabor_express_object_fixture):
  s = sabor_express_object_fixture

  s.calcular_preco = MagicMock()
  s.avaliar_pedido = MagicMock()

  s.iniciar_interface_de_pedidos()

  s.calcular_preco.assert_called_once()
  s.avaliar_pedido.assert_not_called()
  mock_print.assert_any_call("Digite o número do restaurante no qual deseja fazer o pedido.")
  mock_print.assert_any_call("\nPedido finalizado.")