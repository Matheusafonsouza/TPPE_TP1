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
            1.49
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
            3.54
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
            7.56
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

    assert simulador.calcula_aliquota_efetiva() == resultado
