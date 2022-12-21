import pytest

from src.simulador import SimuladorIRPF
from src.exceptions import (
    DescricaoEmBrancoException,
    ValorRendimentoInvalidoException
)


def test_calcula_faixas():
    simulador = SimuladorIRPF()

    simulador.cadastra_rendimento(
        descricao="salario",
        valor=4000.0
    )
    simulador.cadastra_deducao(
        descricao="pensao",
        valor=500.0
    )
    simulador.cadastra_dependente(
        nome="maia",
        data_de_nascimento="28/12/1999"
    )

    assert simulador.calcula_aliquota_efetiva() == 3.54


def test_calcula_faixas_2():
    simulador = SimuladorIRPF()

    simulador.cadastra_rendimento(
        descricao="salario",
        valor=3000.0
    )
    simulador.cadastra_deducao(
        descricao="pensao",
        valor=100.0
    )
    simulador.cadastra_dependente(
        nome="maia",
        data_de_nascimento="28/12/1999"
    )

    assert simulador.calcula_aliquota_efetiva() == 2.01
