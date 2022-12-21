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
        valor=3000.0
    )
    simulador.cadastra_deducao(
        descricao="salario",
        valor=500.0
    )

    assert simulador.calcula_faixas() == {
        "1": 1903.98,
        "2": 596.02,
        "3": 0.0,
        "4": 0.0,
        "5": 0.0,
    }


def test_calcula_faixas_2():
    simulador = SimuladorIRPF()

    simulador.cadastra_rendimento(
        descricao="salario",
        valor=4000.0
    )
    simulador.cadastra_deducao(
        descricao="salario",
        valor=500.0
    )

    assert simulador.calcula_faixas() == {
        "1": 1903.98,
        "2": 922.67,
        "3": 673.35,
        "4": 0.0,
        "5": 0.0,
    }


def test_calcula_imposto_faixas():
    simulador = SimuladorIRPF()

    simulador.cadastra_rendimento(
        descricao="salario",
        valor=3000.0
    )
    simulador.cadastra_deducao(
        descricao="salario",
        valor=500.0
    )

    assert simulador.calcula_imposto_faixas() == {
        "1": 0.0,
        "2": 44.7015,
        "3": 0.0,
        "4": 0.0,
        "5": 0.0,
    }


def test_calcula_imposto_faixas_2():
    simulador = SimuladorIRPF()

    simulador.cadastra_rendimento(
        descricao="salario",
        valor=4000.0
    )
    simulador.cadastra_deducao(
        descricao="salario",
        valor=500.0
    )

    assert simulador.calcula_imposto_faixas() == {
        "1": 0.0,
        "2": 69.2003,
        "3": 101.0025,
        "4": 0.0,
        "5": 0.0,
    }


def test_calcula_total_faixas():
    simulador = SimuladorIRPF()

    simulador.cadastra_rendimento(
        descricao="salario",
        valor=3000.0
    )
    simulador.cadastra_deducao(
        descricao="salario",
        valor=500.0
    )

    assert simulador.calcula_total_faixas() == 2500.00


def test_calcula_total_faixas_2():
    simulador = SimuladorIRPF()

    simulador.cadastra_rendimento(
        descricao="salario",
        valor=4000.0
    )
    simulador.cadastra_deducao(
        descricao="salario",
        valor=500.0
    )

    assert simulador.calcula_total_faixas() == 3500.00


def test_calcula_total_imposto_faixas():
    simulador = SimuladorIRPF()

    simulador.cadastra_rendimento(
        descricao="salario",
        valor=3000.0
    )
    simulador.cadastra_deducao(
        descricao="salario",
        valor=500.0
    )

    assert simulador.calcula_total_imposto_faixas() == 44.7015


def test_calcula_total_imposto_faixas_2():
    simulador = SimuladorIRPF()

    simulador.cadastra_rendimento(
        descricao="salario",
        valor=4000.0
    )
    simulador.cadastra_deducao(
        descricao="salario",
        valor=500.0
    )

    assert simulador.calcula_total_imposto_faixas() == 1270.2028
