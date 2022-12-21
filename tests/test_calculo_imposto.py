import pytest

from src.simulador import SimuladorIRPF
from src.exceptions import (
    DescricaoEmBrancoException,
    ValorRendimentoInvalidoException
)


@pytest.mark.parametrize(
    "rendimentos, deducoes, dependentes, resultado", 
    [
        (
            [
                dict(descricao="salario", valor=3000.0), 
            ],
            [
                dict(descricao="pensao", valor=500.0)
            ],
            [],
            {
                "1": 1903.98,
                "2": 596.02,
                "3": 0.0,
                "4": 0.0,
                "5": 0.0,
            }
        ),
        (
            [
                dict(descricao="salario", valor=4000.0), 
            ],
            [
                dict(descricao="pensao", valor=500.0)
            ],
            [
                dict(nome="maia", data_de_nascimento="28/12/1999")
            ],
            {
                "1": 1903.98,
                "2": 922.67,
                "3": 483.76,
                "4": 0.0,
                "5": 0.0,
            }
        ), 
        (
            [
                dict(descricao="clt", valor=4000.0), 
                dict(descricao="pj", valor=2000.0), 
            ],
            [
                dict(descricao="pensao", valor=1000.0)
            ],
            [
                dict(nome="monteiro", data_de_nascimento="3/8/1997")
            ],
            {
                "1": 1903.98,
                "2": 922.67,
                "3": 924.4,
                "4": 913.63,
                "5": 145.73,
            }
        ), 
    ]
)
def test_calcula_faixas(rendimentos, deducoes, dependentes, resultado):
    simulador = SimuladorIRPF()

    for rendimento in rendimentos:
        simulador.cadastra_rendimento(
            descricao=rendimento.get("descricao"),
            valor=rendimento.get("valor")
        )
    for deducao in deducoes:
        simulador.cadastra_deducao(
            descricao=deducao.get("descricao"),
            valor=deducao.get("valor")
        )
    for dependente in dependentes:
        simulador.cadastra_dependente(
            nome=dependente.get("nome"),
            data_de_nascimento=dependente.get("data_de_nascimento")
        )

    assert simulador.calcula_faixas() == resultado


@pytest.mark.parametrize(
    "rendimentos, deducoes, dependentes, resultado", 
    [
        (
            [
                dict(descricao="salario", valor=3000.0), 
            ],
            [
                dict(descricao="pensao", valor=500.0)
            ],
            [],
            {
                "1": 0.0,
                "2": 44.7,
                "3": 0.0,
                "4": 0.0,
                "5": 0.0,
            }
        ),
        (
            [
                dict(descricao="salario", valor=4000.0), 
            ],
            [
                dict(descricao="pensao", valor=500.0)
            ],
            [
                dict(nome="maia", data_de_nascimento="28/12/1999")
            ],
            {
                "1": 0.0,
                "2": 69.2,
                "3": 72.56,
                "4": 0.0,
                "5": 0.0,
            }
        ), 
        (
            [
                dict(descricao="clt", valor=4000.0), 
                dict(descricao="pj", valor=2000.0), 
            ],
            [
                dict(descricao="pensao", valor=1000.0)
            ],
            [
                dict(nome="monteiro", data_de_nascimento="3/8/1997")
            ],
            {
                "1": 0.0,
                "2": 69.2,
                "3": 138.66,
                "4": 205.57,
                "5": 40.08,
            }
        ), 
    ]
)
def test_calcula_imposto_faixas(rendimentos, deducoes, dependentes, resultado):
    simulador = SimuladorIRPF()

    for rendimento in rendimentos:
        simulador.cadastra_rendimento(
            descricao=rendimento.get("descricao"),
            valor=rendimento.get("valor")
        )
    for deducao in deducoes:
        simulador.cadastra_deducao(
            descricao=deducao.get("descricao"),
            valor=deducao.get("valor")
        )
    for dependente in dependentes:
        simulador.cadastra_dependente(
            nome=dependente.get("nome"),
            data_de_nascimento=dependente.get("data_de_nascimento")
        )

    assert simulador.calcula_imposto_faixas() == resultado


@pytest.mark.parametrize(
    "rendimentos, deducoes, dependentes, resultado", 
    [
        (
            [
                dict(descricao="salario", valor=3000.0), 
            ],
            [
                dict(descricao="pensao", valor=500.0)
            ],
            [],
            2500.00
        ),
        (
            [
                dict(descricao="salario", valor=4000.0), 
            ],
            [
                dict(descricao="pensao", valor=500.0)
            ],
            [
                dict(nome="maia", data_de_nascimento="28/12/1999")
            ],
            3310.41
        ), 
        (
            [
                dict(descricao="clt", valor=4000.0), 
                dict(descricao="pj", valor=2000.0), 
            ],
            [
                dict(descricao="pensao", valor=1000.0)
            ],
            [
                dict(nome="monteiro", data_de_nascimento="3/8/1997")
            ],
            4810.41
        ), 
    ]
)
def test_calcula_total_faixas(rendimentos, deducoes, dependentes, resultado):
    simulador = SimuladorIRPF()

    for rendimento in rendimentos:
        simulador.cadastra_rendimento(
            descricao=rendimento.get("descricao"),
            valor=rendimento.get("valor")
        )
    for deducao in deducoes:
        simulador.cadastra_deducao(
            descricao=deducao.get("descricao"),
            valor=deducao.get("valor")
        )
    for dependente in dependentes:
        simulador.cadastra_dependente(
            nome=dependente.get("nome"),
            data_de_nascimento=dependente.get("data_de_nascimento")
        )

    assert simulador.calcula_total_faixas() == resultado


@pytest.mark.parametrize(
    "rendimentos, deducoes, dependentes, resultado", 
    [
        (
            [
                dict(descricao="salario", valor=3000.0), 
            ],
            [
                dict(descricao="pensao", valor=500.0)
            ],
            [],
            44.7
        ),
        (
            [
                dict(descricao="salario", valor=4000.0), 
            ],
            [
                dict(descricao="pensao", valor=500.0)
            ],
            [
                dict(nome="maia", data_de_nascimento="28/12/1999")
            ],
            141.76
        ), 
        (
            [
                dict(descricao="clt", valor=4000.0), 
                dict(descricao="pj", valor=2000.0), 
            ],
            [
                dict(descricao="pensao", valor=1000.0)
            ],
            [
                dict(nome="monteiro", data_de_nascimento="3/8/1997")
            ],
            453.51
        ), 
    ]
)
def test_calcula_total_imposto_faixas(rendimentos, deducoes, dependentes, resultado):
    simulador = SimuladorIRPF()

    for rendimento in rendimentos:
        simulador.cadastra_rendimento(
            descricao=rendimento.get("descricao"),
            valor=rendimento.get("valor")
        )
    for deducao in deducoes:
        simulador.cadastra_deducao(
            descricao=deducao.get("descricao"),
            valor=deducao.get("valor")
        )
    for dependente in dependentes:
        simulador.cadastra_dependente(
            nome=dependente.get("nome"),
            data_de_nascimento=dependente.get("data_de_nascimento")
        )

    assert simulador.calcula_total_imposto_faixas() == resultado
