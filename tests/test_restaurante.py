from tests.fixtures import restaurante_fixture
from components.cardapio.prato import Prato
from components.cardapio.bebida import Bebida
from components.cardapio.sobremesa import Sobremesa
from io import StringIO
import sys


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


def teste_alterar_estado(restaurante_fixture):
    """Testa se o método alternar_estado altera corretamente o estado do restaurante"""
    restaurante = restaurante_fixture
   
    estado_inicial = restaurante._ativo
   
    restaurante.alternar_estado()
   
    assert restaurante._ativo != estado_inicial
   
    restaurante.alternar_estado()

    assert restaurante._ativo == estado_inicial
   
    if restaurante._ativo:
        assert restaurante.ativo == '✅'
    else:
        assert restaurante.ativo == '❌'


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


def teste_calcular_media_avaliacoes(restaurante_fixture):
    """Testa se o método calcular_media_avaliacoes calcula corretamente a média"""
    restaurante = restaurante_fixture
   
    media_original = restaurante._avaliacoes.media
   
    restaurante.calcular_media_avaliacoes()
 
    soma_avaliacoes = sum(avaliacao["rating"] for avaliacao in restaurante._avaliacoes.avaliacoes_individuais)
    media_esperada = soma_avaliacoes / len(restaurante._avaliacoes.avaliacoes_individuais)
   
    assert restaurante._avaliacoes.media == media_esperada
   
    assert isinstance(restaurante._avaliacoes.media, (int, float))
    assert restaurante._avaliacoes.media >= 0

