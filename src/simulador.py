from src.exceptions import (
    DescricaoEmBrancoException,
    ValorRendimentoInvalidoException
)
from src.models.rendimento import Rendimento


class SimuladorIRPF:
    def __init__(self):
        self.rendimento = None

    def cadastra_rendimento(self, descricao, valor):
        if not descricao:
            raise DescricaoEmBrancoException()

        if not valor:
            raise ValorRendimentoInvalidoException()

        self.rendimento = Rendimento(
            descricao=descricao,
            valor=valor
        )

        
    def total_rendimentos(self):
        return self.rendimento.valor
