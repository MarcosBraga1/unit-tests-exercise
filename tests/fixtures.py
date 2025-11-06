from components.cardapio.sobremesa import Sobremesa
from components.restaurantes import Restaurantes
from components.sabor_express import SaborExpress
from components.restaurante import Restaurante
from components.avaliacao_restaurante import AvaliacaoRestaurante
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
    """Fixture para criar uma instância de Restaurante para testes"""
    cardapio_data = [
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
    ]
   
    avaliacoes = {
        "average": 4.5,
        "individual_ratings": [
            {
                "rating": 5,
                "description": "Excelente restaurante"
            },
            {
                "rating": 4,
                "description": "Muito bom"
            }
        ]
    }
   
    return Restaurante(
        nome="Restaurante Teste",
        categoria="Tradicional",
        cardapio=cardapio_data,
        avaliacoes=avaliacoes
    )
    
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
