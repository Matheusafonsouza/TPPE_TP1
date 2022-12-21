import pytest

from src.simulador import SimuladorIRPF
from src.exceptions import (
    DescricaoEmBrancoException,
    ValorRendimentoInvalidoException
)


def test_cadastra_rendimento():
    simulador = SimuladorIRPF()
    simulador.cadastra_rendimento(descricao="salario", valor=1000.00)

    assert simulador.total_rendimentos() == 1000.0


def test_cadastra_rendimento_sem_descricao():
    simulador = SimuladorIRPF()

    with pytest.raises(DescricaoEmBrancoException):
        simulador.cadastra_rendimento(descricao="", valor=1000.0)


def test_cadastra_rendimento_sem_valor():
    simulador = SimuladorIRPF()

    with pytest.raises(ValorRendimentoInvalidoException):
        simulador.cadastra_rendimento(descricao="salario", valor=None)
