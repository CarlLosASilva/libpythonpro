import pytest

from libypythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None

@pytest.mark.parametrize(
    "destinatario",
    ["renzo@python.pro.br", "foo@bar.com.br"]
)
def test_remetente(destinatario):
    enviador = Enviador()
    resultado = enviador.enviar(
        "%s" % destinatario,
        "luciano@python.pro.br",
        "cursos python pro",
        "Primeira turma"
    )
    assert destinatario in resultado


@pytest.mark.parametrize(
    "remetente",
    ["", "renzo"]
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            "%s" % remetente,
            "luciano@python.pro.br",
            "cursos python pro",
            "Primeira turma"
    )
