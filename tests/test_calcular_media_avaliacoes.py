from tests.fixtures import restaurante_fixture


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