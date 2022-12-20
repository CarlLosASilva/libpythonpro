from unittest.mock import Mock

import pytest

from libypythonpro.spam.enviador_de_email import Enviador
from libypythonpro.spam.modelos import Usuario
from libypythonpro.tests.spam.main import EnviadorDeSpam

@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome="renzo", email='renzo@python.pro.br'),
            Usuario(nome="luciano", email='luciano@python.pro.br')
        ],
        [
            Usuario(nome="renzo", email='renzo@python.pro.br')
        ]
    ]
)
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'renzo@python.pro.br',
        'Curso Python',
        'Confira os módulos'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Renzo', email='renzo@python.pro.br')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'luciano@python.pro.br',
        'Curso Python',
        'Confira os módulos'
    )
    enviador.enviar.assert_called_once_with(
        'luciano@python.pro.br',
        'renzo@python.pro.br',
        'Curso Python',
        'Confira os módulos'
    )