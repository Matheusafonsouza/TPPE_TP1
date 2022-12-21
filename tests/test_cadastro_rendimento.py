import pytest

from src.simulador import SimuladorIRPF
from src.exceptions import (
    DescricaoEmBrancoException,
    ValorRendimentoInvalidoException
)

@pytest.mark.parametrize(
    "rendimentos, resultado", 
    [
        (
            [
                dict(descricao="salario", valor=500.0), 
                dict(descricao="pensao", valor=100.0)
            ], 
            600.0
        ), 
        (
            [
                dict(descricao="salario", valor=500.0), 
            ], 
            500.0
        ), 
        (
            [
                dict(descricao="salario", valor=500.0), 
                dict(descricao="pensao", valor=500.0), 
                dict(descricao="imposto", valor=100.0), 
            ], 
            1100.0
        ), 
    ]
)
def test_cadastra_rendimento(rendimentos, resultado):
    simulador = SimuladorIRPF()

    for rendimento in rendimentos:
        print(rendimento)
        simulador.cadastra_rendimento(
            descricao=rendimento.get("descricao"),
            valor=rendimento.get("valor")
        )

    assert simulador.total_rendimentos() == resultado


def test_cadastra_rendimento_sem_descricao():
    simulador = SimuladorIRPF()

    with pytest.raises(DescricaoEmBrancoException):
        simulador.cadastra_rendimento(descricao="", valor=1000.0)


def test_cadastra_rendimento_sem_valor():
    simulador = SimuladorIRPF()

    with pytest.raises(ValorRendimentoInvalidoException):
        simulador.cadastra_rendimento(descricao="salario", valor=None)
