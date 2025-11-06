from tests.fixtures import restaurante_fixture


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