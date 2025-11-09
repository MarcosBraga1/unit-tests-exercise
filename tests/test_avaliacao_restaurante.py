from tests.fixtures import avaliacao_restaurante_fixture

def test_criar_instancia(avaliacao_restaurante_fixture):
  avaliacao = avaliacao_restaurante_fixture
  
  assert avaliacao.media == 4.5
  assert len(avaliacao.avaliacoes_individuais) == 2
  assert avaliacao.avaliacoes_individuais[0]["rating"] == 5
  assert avaliacao.avaliacoes_individuais[0]["description"] == "Excelente restaurante"
  assert avaliacao.avaliacoes_individuais[1]["rating"] == 4
  assert avaliacao.avaliacoes_individuais[1]["description"] == "Muito bom"
