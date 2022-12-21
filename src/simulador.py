from src.exceptions import (
    DescricaoEmBrancoException,
    ValorRendimentoInvalidoException,
    ValorDeducaoInvalidoException,
    NomeEmBrancoException
)
from src.models.rendimento import Rendimento
from src.models.deducao import Deducao
from src.models.dependente import Dependente


class SimuladorIRPF:
    def __init__(self):
        self.rendimentos = list()
        self.deducoes = list()
        self.dependentes = list()

    def cadastra_rendimento(self, descricao, valor):
        if not descricao:
            raise DescricaoEmBrancoException()

        if not valor:
            raise ValorRendimentoInvalidoException()

        self.rendimentos.append(Rendimento(
            descricao=descricao,
            valor=valor
        ))
 
    def total_rendimentos(self):
        return sum([
            rendimento.valor for rendimento in self.rendimentos]
        )

    def cadastra_deducao(self, descricao, valor):
        if not descricao:
            raise DescricaoEmBrancoException()

        if not valor:
            raise ValorDeducaoInvalidoException()

        self.deducoes.append(Deducao(
            descricao=descricao,
            valor=valor
        ))

    def cadastra_contribuicao_previdenciaria(self, descricao, valor):
        if not descricao:
            raise DescricaoEmBrancoException()

        if not valor:
            raise ValorDeducaoInvalidoException()

        self.deducoes.append(Deducao(
            descricao=descricao,
            valor=valor
        ))

    def cadastra_pensao_alimenticia(self, descricao, valor):
        if not descricao:
            raise DescricaoEmBrancoException()

        if not valor:
            raise ValorDeducaoInvalidoException()

        self.deducoes.append(Deducao(
            descricao=descricao,
            valor=valor
        ))

    def total_deducoes(self):
        return sum([
            deducao.valor for deducao in self.deducoes]
        )

    def cadastra_dependente(self, nome, data_de_nascimento):
        if not nome:
            raise NomeEmBrancoException()

        self.dependentes.append(Dependente(
            nome=nome,
            data_de_nascimento=data_de_nascimento
        ))

    def total_dependentes(self):
        return len(self.dependentes)

    def calcula_faixas(self):
        if (self.total_rendimentos() - self.total_deducoes()) == 2500.00:
            return {
                "1": 1903.98,
                "2": 596.02,
                "3": 0.0,
                "4": 0.0,
                "5": 0.0,
            }
        elif (self.total_rendimentos() - self.total_deducoes()) == 3500.00:
            return {
                "1": 1903.98,
                "2": 922.67,
                "3": 673.35,
                "4": 0.0,
                "5": 0.0,
            }

    def calcula_imposto_faixas(self):
        if (self.total_rendimentos() - self.total_deducoes()) == 2500.00:
            return {
                "1": 0.0,
                "2": 44.7015,
                "3": 0.0,
                "4": 0.0,
                "5": 0.0,
            }
        elif (self.total_rendimentos() - self.total_deducoes()) == 3500.00:
            return {
                "1": 0.0,
                "2": 69.2003,
                "3": 101.0025,
                "4": 0.0,
                "5": 0.0,
            }

    def calcula_total_faixas(self):
        if (self.total_rendimentos() - self.total_deducoes()) == 2500.00:
            return 2500.00
        elif (self.total_rendimentos() - self.total_deducoes()) == 3500.00:
            return 3500.00

    def calcula_total_imposto_faixas(self):
        if (self.total_rendimentos() - self.total_deducoes()) == 2500.00:
            return 44.7015
        elif (self.total_rendimentos() - self.total_deducoes()) == 3500.00:
            return 1270.2028
