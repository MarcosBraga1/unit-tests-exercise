from tests.fixtures import sobremesa_fixture
from components.cardapio.sobremesa import Sobremesa

def teste_criar_instancia_sobremesa():
    """Testa se é possível criar uma instância de Sobremesa corretamente"""
    sobremesa = Sobremesa(
        nome="Sorvete",
        preco=100,
        tipo="Gelados",
        tamanho="500ml"
    )
    
    assert sobremesa._nome == "Sorvete"
    assert sobremesa._preco == 100
    assert sobremesa.tipo == "Gelados"
    assert sobremesa.tamanho == "500ml"

def teste_aplicar_desconto_sobremesa(sobremesa_fixture):
    sobremesa = sobremesa_fixture
    sobremesa.aplicar_desconto()

    assert sobremesa._preco == 85