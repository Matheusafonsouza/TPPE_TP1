import pytest

from src.simulador import SimuladorIRPF
from src.exceptions import (
    DescricaoEmBrancoException,
    ValorDeducaoInvalidoException,
    NomeEmBrancoException
)


def test_cadastra_deducao():
    simulador = SimuladorIRPF()

    simulador.cadastra_deducao(
        descricao="saude",
        valor=1000.0
    )

    assert simulador.total_deducaos() == 1000.0


def test_cadastra_deducao_sem_descricao():
    simulador = SimuladorIRPF()

    with pytest.raises(DescricaoEmBrancoException):
        simulador.cadastra_deducao(descricao="", valor=1000.0)


def test_cadastra_deducao_sem_valor():
    simulador = SimuladorIRPF()

    with pytest.raises(ValorDeducaoInvalidoException):
        simulador.cadastra_deducao(descricao="saude", valor=None)


def test_cadastra_contribuicao_previdenciaria():
    simulador = SimuladorIRPF()

    simulador.cadastra_contribuicao_previdenciaria(
        descricao="previdencia privada",
        valor=1000.0
    )

    assert simulador.total_deducaos() == 1000.0


def test_cadastra_contribuicao_previdenciaria_sem_descricao():
    simulador = SimuladorIRPF()

    with pytest.raises(DescricaoEmBrancoException):
        simulador.cadastra_contribuicao_previdenciaria(descricao="", valor=1000.0)


def test_cadastra_contribuicao_previdenciaria_sem_valor():
    simulador = SimuladorIRPF()

    with pytest.raises(ValorDeducaoInvalidoException):
        simulador.cadastra_contribuicao_previdenciaria(descricao="previdencia privada", valor=None)


def test_cadastra_pensao_alimenticia():
    simulador = SimuladorIRPF()

    simulador.cadastra_pensao_alimenticia(
        descricao="pensao",
        valor=1000.0
    )

    assert simulador.total_deducaos() == 1000.0


def test_cadastra_pensao_alimenticia_sem_descricao():
    simulador = SimuladorIRPF()

    with pytest.raises(DescricaoEmBrancoException):
        simulador.cadastra_pensao_alimenticia(descricao="", valor=1000.0)


def test_cadastra_pensao_alimenticia_sem_valor():
    simulador = SimuladorIRPF()

    with pytest.raises(ValorDeducaoInvalidoException):
        simulador.cadastra_pensao_alimenticia(descricao="pensao", valor=None)


def test_cadastra_dependente():
    simulador = SimuladorIRPF()

    simulador.cadastra_dependente(
        nome="matheus",
        data_de_nascimento="23/07/2000"
    )

    assert simulador.total_dependentes() == 1


def test_cadastra_dependente_sem_nome():
    simulador = SimuladorIRPF()

    with pytest.raises(NomeEmBrancoException):
        simulador.cadastra_dependente(nome="", data_de_nascimento="23/07/2000")
