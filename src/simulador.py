from src.exceptions import (
    DescricaoEmBrancoException,
    ValorRendimentoInvalidoException,
    ValorDeducaoInvalidoException,
    NomeEmBrancoException
)
from src.models.rendimento import Rendimento
from src.models.deducao import Deducao
from src.models.dependente import Dependente
from src.models.faixa import Faixa


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
        return Faixa(
            total_rendimentos=self.total_rendimentos(),
            total_dependentes=self.total_dependentes(),
            total_deducoes=self.total_deducoes()
        ).calcula_faixas()

    def calcula_imposto_faixas(self):
        faixas = self.calcula_faixas()

        return {
            "1": 0.00,
            "2": round(faixas.get("2") * 0.075, 2),
            "3": round(faixas.get("3") * 0.15, 2),
            "4": round(faixas.get("4") * 0.225, 2),
            "5": round(faixas.get("5") * 0.275, 2)
        }

    def calcula_total_faixas(self):
        faixas = self.calcula_faixas()
        return round(sum([faixas.get(el) for el in faixas]), 2)

    def calcula_total_imposto_faixas(self):
        impostos = self.calcula_imposto_faixas()
        return round(sum([impostos.get(el) for el in impostos]), 2)

    def calcula_aliquota_efetiva(self):
        return round((self.calcula_total_imposto_faixas() / self.total_rendimentos()) * 100, 2)
    