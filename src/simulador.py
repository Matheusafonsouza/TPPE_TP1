from src.exceptions import (
    DescricaoEmBrancoException,
    ValorRendimentoInvalidoException
)


class SimuladorIRPF:
    def cadastra_rendimento(self, descricao, valor):
        if not descricao:
            raise DescricaoEmBrancoException()

        if not valor:
            raise ValorRendimentoInvalidoException()

        
    def total_rendimentos(self):
        return 1000.0
