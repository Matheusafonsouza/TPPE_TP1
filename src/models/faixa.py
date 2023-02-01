class Faixa:
    def __init__(
            self,
            total_rendimentos,
            total_deducoes,
            total_dependentes
        ):
        self.faixa_1 = 0
        self.faixa_2 = 0
        self.faixa_3 = 0
        self.faixa_4 = 0
        self.faixa_5 = 0
        self.total_rendimentos = total_rendimentos
        self.total_deducoes = total_deducoes
        self.total_dependentes = total_dependentes
        self.total_rendimentos = self.calcula_total_rendimentos()

    def calcula_faixas(self):
        self.calcula_faixas_pelo_total_rendimento()
        return {
            "1": self.faixa_1,
            "2": self.faixa_2,
            "3": self.faixa_3,
            "4": self.faixa_4,
            "5": self.faixa_5
        }

    def calcula_faixas_pelo_total_rendimento(self):
        if self.total_rendimentos <= 1903.98:
            self.faixa_1 = self.total_rendimentos
        elif self.total_rendimentos <= 2826.65:
            self.faixa_1 = 1903.98
            self.faixa_2 = round(self.total_rendimentos - 1903.98, 2)
        elif self.total_rendimentos <= 3751.05:
            self.faixa_1 = 1903.98
            self.faixa_2 = 922.67
            self.faixa_3 = round(self.total_rendimentos - 2826.65, 2)
        elif self.total_rendimentos <= 4664.68:
            self.faixa_1 = 1903.98
            self.faixa_2 = 922.67
            self.faixa_3 = 924.40
            self.faixa_4 = round(self.total_rendimentos - 3751.05, 2)
        else:
            self.faixa_1 = 1903.98
            self.faixa_2 = 922.67
            self.faixa_3 = 924.40
            self.faixa_4 = 913.63
            self.faixa_5 = round(self.total_rendimentos - 4664.68, 2)

    def calcula_total_rendimentos(self):
        return (
            self.total_rendimentos -
            self.total_deducoes -
            (189.59 * self.total_dependentes)
        )
