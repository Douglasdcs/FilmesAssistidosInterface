from tkinter import *
from scr.Filme import *

# Classe do container principal
class Application:
    def __init__(self, master=None):
        # Dando título à aplicação
        master.title("Filmes Assistidos")

        # Containers - Como são 8 "Linhas" na interface, teremos 8 widgets
        # master é o container elementar da interface
        self.widget1 = Frame(master, pady=15, padx=20)
        # Informa-se que será usado a geometria pack() [Podendo ser: grid, pack, place]
        self.widget1.pack()

        self.widget2 = Frame(master, pady=7, padx=20)
        # Informa-se que será usado a geometria pack() [Podendo ser: grid, pack, place]
        self.widget2.pack()

        self.widget3 = Frame(master, pady=7, padx=20)
        # Informa-se que será usado a geometria pack() [Podendo ser: grid, pack, place]
        self.widget3.pack()

        self.widget4 = Frame(master, pady=7, padx=20)
        # Informa-se que será usado a geometria pack() [Podendo ser: grid, pack, place]
        self.widget4.pack()

        self.widget5 = Frame(master, pady=15, padx=20)
        # Informa-se que será usado a geometria pack() [Podendo ser: grid, pack, place]
        self.widget5.pack()

        self.widget6 = Frame(master, pady=15, padx=20)
        # Informa-se que será usado a geometria pack() [Podendo ser: grid, pack, place]
        self.widget6.pack()

        self.widget7 = Frame(master, pady=15, padx=20)
        # Informa-se que será usado a geometria pack() [Podendo ser: grid, pack, place]
        self.widget7.pack()

        self.widget8 = Frame(master, pady=15, padx=20)
        # Informa-se que será usado a geometria pack() [Podendo ser: grid, pack, place]
        self.widget8.pack()

        # *** Fim dos Widgets ***

        # Dentro desse container, imprime-se a mensagem abaixo
        self.msg = Label(self.widget1, text="Informe os dados do filme assistido:")
        self.msg["font"] = ("Calibri", "11", "bold")
        self.msg.pack()

        # Nome do filme - side=LEFT garante que os blocos estarão na mesma linha
        self.label1 = Label(self.widget2, text="Nome do Filme: ", width=15)
        self.label1.pack(side=LEFT)

        # Entrada do Nome do filme
        self.entrada_nome = Entry(self.widget2, width=40)
        self.entrada_nome.pack(side=LEFT)

        # Data em que o filme foi visto
        self.label2 = Label(self.widget3, text="Data (DD/MM/AA): ", width=15)
        self.label2.pack(side=LEFT)

        # Entrada da data em que o filme foi visto
        self.entrada_data = Entry(self.widget3, width=40)
        self.entrada_data.pack(side=LEFT)

        # Plataforma em que o vídeo foi visto
        self.label3 = Label(self.widget4, text="Plataforma: ", width=15)
        self.label3.pack(side=LEFT)

        # Entrada da plataforma em que o vídeo foi visto
        self.entrada_fonte = Entry(self.widget4, width=40)
        self.entrada_fonte.pack(side=LEFT)

        # Botão para atualizar txt com os filmes
        self.atualizar = Button(self.widget5, command=lambda: self.atualiza(), text="Atualizar")
        self.atualizar["width"] = 7
        self.atualizar.pack()

        # Status da atualização
        self.status = Label(self.widget7, text="")
        self.status.pack()

        # Informamos que haverá um botão no container principal e que sua função será quitar
        self.fechar = Button(self.widget8, command=self.widget8.quit)
        # Informa-se o texto presente
        self.fechar["text"] = "Fechar"
        # Largura
        self.fechar["width"] = 5
        # Exibe
        self.fechar.pack()

    def atualiza(self):
        filme = Filme()
        # Pegando todos os valores presentes nos campos de entrada
        entrada_nome = self.entrada_nome.get()
        entrada_data = self.entrada_data.get()
        entrada_fonte = self.entrada_fonte.get()

        # Instanciando objeto pelos gets
        filme.set_nome(entrada_nome)
        filme.set_data(entrada_data)
        filme.set_fonte(entrada_fonte)

        # print(entrada_nome, entrada_data, entrada_fonte)


        if filme.verifica_data() and filme.verifica_dados():
            self.status["text"] = "Atualizando..."
        # Verificando se os dados estão preenchidos
        elif not filme.verifica_dados():
            self.status["text"] = "Dados incompletos!"
            # Verificando formatação da data
        else:
            self.status["text"] = "A data informada está incorreta!"







root = Tk()
# Definindo tamanho da janela
root.geometry("475x350")
Application(root)
root.mainloop()
