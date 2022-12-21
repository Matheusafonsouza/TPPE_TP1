import pytest

from src.simulador import SimuladorIRPF
from src.exceptions import (
    DescricaoEmBrancoException,
    ValorDeducaoInvalidoException,
    NomeEmBrancoException
)


@pytest.mark.parametrize(
    "deducoes, resultado", 
    [
        (
            [
                dict(descricao="saude", valor=500.0), 
                dict(descricao="comida", valor=100.0)
            ], 
            600.0
        ), 
        (
            [
                dict(descricao="saude", valor=500.0), 
            ], 
            500.0
        ), 
        (
            [
                dict(descricao="saude", valor=500.0), 
                dict(descricao="comida", valor=500.0), 
                dict(descricao="escola", valor=100.0), 
            ], 
            1100.0
        ), 
    ]
)
def test_cadastra_deducao(deducoes, resultado):
    simulador = SimuladorIRPF()

    for deducao in deducoes:
        simulador.cadastra_deducao(
            descricao=deducao.get("descricao"),
            valor=deducao.get("valor")
        )

    assert simulador.total_deducoes() == resultado


def test_cadastra_deducao_sem_descricao():
    simulador = SimuladorIRPF()

    with pytest.raises(DescricaoEmBrancoException):
        simulador.cadastra_deducao(descricao="", valor=1000.0)


def test_cadastra_deducao_sem_valor():
    simulador = SimuladorIRPF()

    with pytest.raises(ValorDeducaoInvalidoException):
        simulador.cadastra_deducao(descricao="saude", valor=None)


@pytest.mark.parametrize(
    "deducoes, resultado", 
    [
        (
            [
                dict(descricao="privada", valor=500.0), 
                dict(descricao="publica", valor=100.0)
            ], 
            600.0
        ), 
        (
            [
                dict(descricao="privada", valor=500.0), 
            ], 
            500.0
        ), 
        (
            [
                dict(descricao="privada", valor=500.0), 
                dict(descricao="publica", valor=500.0), 
                dict(descricao="bradesco", valor=100.0), 
            ], 
            1100.0
        ), 
    ]
)
def test_cadastra_contribuicao_previdenciaria(deducoes, resultado):
    simulador = SimuladorIRPF()

    for deducao in deducoes:
        simulador.cadastra_contribuicao_previdenciaria(
            descricao=deducao.get("descricao"),
            valor=deducao.get("valor")
        )

    assert simulador.total_deducoes() == resultado


def test_cadastra_contribuicao_previdenciaria_sem_descricao():
    simulador = SimuladorIRPF()

    with pytest.raises(DescricaoEmBrancoException):
        simulador.cadastra_contribuicao_previdenciaria(descricao="", valor=1000.0)


def test_cadastra_contribuicao_previdenciaria_sem_valor():
    simulador = SimuladorIRPF()

    with pytest.raises(ValorDeducaoInvalidoException):
        simulador.cadastra_contribuicao_previdenciaria(descricao="previdencia privada", valor=None)


@pytest.mark.parametrize(
    "deducoes, resultado", 
    [
        (
            [
                dict(descricao="pensao1", valor=500.0), 
                dict(descricao="pensao2", valor=100.0)
            ], 
            600.0
        ), 
        (
            [
                dict(descricao="pensao1", valor=500.0), 
            ], 
            500.0
        ), 
        (
            [
                dict(descricao="pensao1", valor=500.0), 
                dict(descricao="pensao2", valor=500.0), 
                dict(descricao="pensao3", valor=100.0), 
            ], 
            1100.0
        ), 
    ]
)
def test_cadastra_pensao_alimenticia(deducoes, resultado):
    simulador = SimuladorIRPF()

    for deducao in deducoes:
        simulador.cadastra_pensao_alimenticia(
            descricao=deducao.get("descricao"),
            valor=deducao.get("valor")
        )

    assert simulador.total_deducoes() == resultado


def test_cadastra_pensao_alimenticia_sem_descricao():
    simulador = SimuladorIRPF()

    with pytest.raises(DescricaoEmBrancoException):
        simulador.cadastra_pensao_alimenticia(descricao="", valor=1000.0)


def test_cadastra_pensao_alimenticia_sem_valor():
    simulador = SimuladorIRPF()

    with pytest.raises(ValorDeducaoInvalidoException):
        simulador.cadastra_pensao_alimenticia(descricao="pensao", valor=None)


@pytest.mark.parametrize(
    "dependentes, resultado", 
    [
        (
            [
                dict(nome="matheus", data_de_nascimento="23/07/2001"), 
                dict(nome="maia", data_de_nascimento="23/07/2000")
            ], 
            2
        ), 
        (
            [
                dict(nome="matheus", data_de_nascimento="23/07/2001"), 
            ], 
            1
        ), 
        (
            [
                dict(nome="matheus", data_de_nascimento="23/07/2000"), 
                dict(nome="maia", data_de_nascimento="12/07/2000"), 
                dict(nome="daniel", data_de_nascimento="15/07/2000"), 
            ], 
            3
        ), 
    ]
)
def test_cadastra_dependente(dependentes, resultado):
    simulador = SimuladorIRPF()

    for dependente in dependentes:
        simulador.cadastra_dependente(
            nome=dependente.get("nome"),
            data_de_nascimento=dependente.get("data_de_nascimento")
        )

    assert simulador.total_dependentes() == resultado


def test_cadastra_dependente_sem_nome():
    simulador = SimuladorIRPF()

    with pytest.raises(NomeEmBrancoException):
        simulador.cadastra_dependente(nome="", data_de_nascimento="23/07/2000")
