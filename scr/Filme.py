from datetime import date


class Filme:

    def __init__(self):
        self.nome = None
        self.data = None
        self.fonte = None

    def set_nome(self, nome):
        self.nome = nome

    def set_data(self, data):
        self.data = data

    def set_fonte(self, fonte):
        self.fonte = fonte

    # Retorna 1 se a data estiver no formado certo
    def verifica_data(self):
        # A data deve estar no formato: DD/MM/AA
        a = self.data.split("/")
        if len(a) == 3:
            for i in range(0, len(a)):
                if len(a[i]) != 2:
                    return 0
        else:
            return 0
        if not self.verifica_partes_data():
            return 0

        return 1

    # Retorna 1 se estiver tudo certo
    def verifica_partes_data(self):
        a = self.data.split("/")
        # Se for letras tipo xx/ff/ll pega o erro
        try:
            dia = int(a[0])
            mes = int(a[1])
            ano = int(a[2])
            if dia > 31 or dia <= 0 or mes > 12 or mes <= 0 or ano > (date.today().year - 2000) or ano < 11:
                return 0
            return 1
        except ValueError:
            return 0

    # Retorna 1 se estiver certo
    def verifica_dados(self):
        if self.nome is None or self.data is None or self.fonte is None:
            return 0
        if self.nome == "" or self.data == "" or self.fonte == "":
            return 0
        return 1

    def to_string(self, num):
        return num + "- " + self.nome + " - " + self.data + " (" + self.fonte + ")"
