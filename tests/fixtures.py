from components.cardapio.sobremesa import Sobremesa
from components.restaurantes import Restaurantes
from components.sabor_express import SaborExpress
from components.avaliacao_restaurante import AvaliacaoRestaurante
from components import restaurante as restaurante_module
import pytest

@pytest.fixture
def sabor_express_object_fixture():
  sabor_express_mock = SaborExpress()
  sabor_express_mock._restaurantes = Restaurantes({
    "restaurants": [
      {
        "name": "restaurante 1",
        "category": "tradicional",
        "menu": [
          {
            "Item": "Item 1",
            "Price": 5,
            "Description": "An item 1"
          },
          {
            "Item": "Item 2",
            "Price": 10,
            "Description": "An item 2"
          },
          {
            "Item": "Item 1",
            "Price": 6,
            "Description": "An item 3"
          }
        ],
        "ratings": {
          "average": 3,
          "individual_ratings": [
            {
              "rating": 3,
              "description": "Don't like it that much"
            }
          ]
        }
      },
      {
        "name": "restaurante 2",
        "category": "tradicional",
        "menu": [
          {
            "Item": "Item 1",
            "Price": 5,
            "Description": "An item 1"
          },
          {
            "Item": "Item 2",
            "Price": 10,
            "Description": "An item 2"
          },
          {
            "Item": "Item 1",
            "Price": 6,
            "Description": "An item 3"
          }
        ],
        "ratings": {
          "average": 3,
          "individual_ratings": [
            {
              "rating": 3,
              "description": "Don't like it that much"
            }
          ]
        }
      }
    ]
  })
    
  return sabor_express_mock

@pytest.fixture
def sobremesa_fixture():
  return Sobremesa(
    nome="Sorvete",
    preco=100,
    tipo="Gelados",
    tamanho="500ml"
  )

@pytest.fixture
def restaurante_fixture():
  """Fixture para criar uma instância de Restaurantes para testes"""
  restaurantes_data = {
    "restaurants": [
      {
        "name": "Restaurante Teste",
        "category": "Tradicional",
        "menu": [
          {
            "Item": "Prato Principal",
            "Price": 25.50,
            "Description": "Um prato delicioso"
          },
          {
            "Item": "Bebida Refrescante",
            "Price": 8.00,
            "Size": "500ml",
            "tipo": "Bebida"
          }
        ],
        "ratings": {
          "average": 4.5,
          "individual_ratings": [
            {"rating": 5, "description": "Excelente restaurante"},
            {"rating": 4, "description": "Muito bom"}
          ]
        }
      }
    ]
  }

  return Restaurantes(restaurantes_data)

@pytest.fixture
def avaliacao_restaurante_fixture():
  """Fixture para criar uma instância de AvaliacaoRestaurante para testes"""
  return AvaliacaoRestaurante(
    media=4.5,
    avaliacoes_individuais=[
      {
        "rating": 5,
        "description": "Excelente restaurante"
      },
      {
        "rating": 4,
        "description": "Muito bom"
      }
    ]
  )

@pytest.fixture(autouse=True)
def mock_dependencias(monkeypatch):
  class FakeAvaliacaoRestaurante:
    def __init__(self, media, avaliacoes_individuais):
      self.media = media
      self.avaliacoes_individuais = avaliacoes_individuais

  class FakeItemCardapio:
    def __init__(self, nome, preco):
      self._nome = nome
      self._preco = preco
  
  monkeypatch.setattr(restaurante_module, "AvaliacaoRestaurante", FakeAvaliacaoRestaurante)
  monkeypatch.setattr(restaurante_module, "Prato", FakeItemCardapio)
  monkeypatch.setattr(restaurante_module, "Bebida", FakeItemCardapio)
  monkeypatch.setattr(restaurante_module, "Sobremesa", FakeItemCardapio)

@pytest.fixture
def restaurantes_data():
  return {
    "restaurants": [
      {
        "name": "Pizzaria Napoli",
        "category": "Italiana",
        "menu": [
          {"Item": "Pizza Margherita", "Price": 30.0, "Description": "Clássica italiana"},
          {"Item": "Lasanha", "Price": 25.0, "Description": "Tradicional de forno"}
        ],
        "ratings": {
          "average": 4.8,
          "individual_ratings": [
            {"cliente": "Ana", "rating": 5.0},
            {"cliente": "Bruno", "rating": 4.6},
          ]
        }
      },
      {
        "name": "Sushi Express",
        "category": "Japonesa",
        "menu": [
          {"Item": "Sushi", "Price": 15.0, "Description": "Combo de sushi"},
        ],
        "ratings": {
          "average": 4.9,
          "individual_ratings": [
            {"cliente": "Carlos", "rating": 4.9}
          ]
        }
      }
    ]
  }