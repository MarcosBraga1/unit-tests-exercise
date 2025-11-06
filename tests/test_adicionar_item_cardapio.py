from tests.fixtures import restaurante_fixture
from components.cardapio.prato import Prato
from components.cardapio.bebida import Bebida
from components.cardapio.sobremesa import Sobremesa


def teste_adicionar_item_cardapio(restaurante_fixture):
    """Testa se o método adicionar_no_cardapio adiciona corretamente itens ao cardápio"""
    restaurante = restaurante_fixture
   
    tamanho_inicial = len(restaurante._cardapio)
   
    novo_prato = Prato(
        nome="Novo Prato",
        preco=30.00,
        descricao="Um prato novo para teste"
    )
   
    restaurante.adicionar_no_cardapio(novo_prato)
   
    assert len(restaurante._cardapio) == tamanho_inicial + 1
   
    assert restaurante._cardapio[-1] == novo_prato
    assert restaurante._cardapio[-1]._nome == "Novo Prato"
    assert restaurante._cardapio[-1]._preco == 30.00
   
    nova_bebida = Bebida(
        nome="Nova Bebida",
        preco=5.50,
        tamanho="350ml"
    )
   
    tamanho_antes_bebida = len(restaurante._cardapio)
    restaurante.adicionar_no_cardapio(nova_bebida)
   
    assert len(restaurante._cardapio) == tamanho_antes_bebida + 1
    assert restaurante._cardapio[-1] == nova_bebida