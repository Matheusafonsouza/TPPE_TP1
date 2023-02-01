FAIXA_1_LIMITE = 1903.98
FAIXA_2_LIMITE = 2826.65
FAIXA_2_LIMITE_VALOR = 922.67
FAIXA_3_LIMITE = 3751.05
FAIXA_3_LIMITE_VALOR = 924.40
FAIXA_4_LIMITE = 4664.68
FAIXA_4_LIMITE_VALOR = 913.63
FAIXA_5_LIMITE = 2826.65
VALOR_POR_DEPENDENTE = 189.59


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
        if self.total_rendimentos <= FAIXA_1_LIMITE:
            self.faixa_1 = self.total_rendimentos
        elif self.total_rendimentos <= FAIXA_2_LIMITE:
            self.faixa_1 = FAIXA_1_LIMITE
            self.faixa_2 = round(self.total_rendimentos - FAIXA_1_LIMITE, 2)
        elif self.total_rendimentos <= FAIXA_3_LIMITE:
            self.faixa_1 = FAIXA_1_LIMITE
            self.faixa_2 = FAIXA_2_LIMITE_VALOR
            self.faixa_3 = round(self.total_rendimentos - FAIXA_2_LIMITE, 2)
        elif self.total_rendimentos <= FAIXA_4_LIMITE:
            self.faixa_1 = FAIXA_1_LIMITE
            self.faixa_2 = FAIXA_2_LIMITE_VALOR
            self.faixa_3 = FAIXA_3_LIMITE_VALOR
            self.faixa_4 = round(self.total_rendimentos - FAIXA_3_LIMITE, 2)
        else:
            self.faixa_1 = FAIXA_1_LIMITE
            self.faixa_2 = FAIXA_2_LIMITE_VALOR
            self.faixa_3 = FAIXA_3_LIMITE_VALOR
            self.faixa_4 = FAIXA_4_LIMITE_VALOR
            self.faixa_5 = round(self.total_rendimentos - FAIXA_4_LIMITE, 2)

    def calcula_total_rendimentos(self):
        return (
            self.total_rendimentos -
            self.total_deducoes -
            (VALOR_POR_DEPENDENTE * self.total_dependentes)
        )
