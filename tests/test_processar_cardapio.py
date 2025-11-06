from tests.fixtures import restaurante_fixture
from components.cardapio.prato import Prato
from components.cardapio.bebida import Bebida
from components.cardapio.sobremesa import Sobremesa


def teste_processar_cardapio(restaurante_fixture):
    """Testa se o método processar_cardapio processa corretamente os itens do cardápio"""
    restaurante = restaurante_fixture
   
    cardapio_data = [
        {
            "Item": "Prato Teste",
            "Price": 25.50,
            "Description": "Um prato de teste"
        },
        {
            "Item": "Bebida Teste",
            "Price": 8.00,
            "Size": "500ml",
            "tipo": "Bebida"
        },
        {
            "Item": "Sobremesa Teste",
            "Price": 12.00,
            "Size": "300g",
            "Type": "Gelados",
            "tipo": "Sobremesa"
        }
    ]
   
    cardapio_processado = restaurante.processar_cardapio(cardapio_data)
   
    assert cardapio_processado is not None
    assert isinstance(cardapio_processado, list)
   
    assert isinstance(cardapio_processado[0], Prato)
    assert cardapio_processado[0]._nome == "Prato Teste"
    assert cardapio_processado[0]._preco == 25.50
    assert cardapio_processado[0].descricao == "Um prato de teste"
   
    assert len(cardapio_processado) >= 0
