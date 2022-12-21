from src.exceptions import (
    DescricaoEmBrancoException,
    ValorRendimentoInvalidoException
)
from src.models.rendimento import Rendimento


class SimuladorIRPF:
    def __init__(self):
        self.rendimentos = list()

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
