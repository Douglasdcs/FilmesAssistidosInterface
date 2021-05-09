from tkinter import *
from tkinter import messagebox
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

        # Botão para atualizar frase para verificação
        self.atualizar = Button(self.widget5, command=lambda: self.atualiza(), text="Montar")
        self.atualizar["width"] = 7
        self.atualizar.pack()

        # Status da atualização estático
        self.status_statico = Label(self.widget6, text="Status: ")
        self.status_statico["font"] = ("Calibri", "11", "bold")
        self.status_statico.pack(side=LEFT)

        # Status da atualização
        self.status = Label(self.widget6, text="")
        self.status["font"] = ("Calibri", "11", "bold")
        self.status.pack(side=LEFT)

        # # Botão para salvar no Banco de dados o filme ***
        # self.salva_bd = Button(self.widget7, command=lambda: self.atualiza(), text="Salvar BD")
        # self.salva_bd["width"] = 8
        # self.salva_bd.pack(side=LEFT)

        # Botão para limpas os campos das entradas
        self.limpa = Button(self.widget7, command=lambda: self.limpa_campos(), text="Limpar")
        self.limpa["width"] = 8
        self.limpa.pack(side=LEFT)

        # Botão para salvar no txt com os filmes
        self.salva_texto = Button(self.widget7, command=lambda: self.salva_txt(), text="Salvar TXT")
        self.salva_texto["width"] = 8
        self.salva_texto.pack(side=LEFT)

        # Informamos que haverá um botão no container principal e que sua função será quitar
        self.fechar = Button(self.widget8, command=self.widget8.quit)
        # Informa-se o texto presente
        self.fechar["text"] = "Fechar"
        # Largura
        self.fechar["width"] = 8
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
            # Monta o texto no formato de salvamento
            self.monta_texto(filme)
        # Verificando se os dados estão preenchidos
        elif not filme.verifica_dados():
            self.status["text"] = "Dados incompletos!"
            # Verificando formatação da data
        else:
            self.status["text"] = "A data informada está incorreta!"

    def monta_texto(self, filme):
        # Abre arquivo
        file = open(adress, "r", encoding='utf-8')
        lines = file.readlines()
        last = lines[len(lines)-1]
        file.close()
        last = last.split("-")[0]
        new_last = str(int(last) + 1)
        # Chama método para concatenar a string que será salva
        texto = filme.to_string(new_last)
        self.status["text"] = texto

    def salva_txt(self):
        # Pegando os dados do Label e colocando um \n no início
        texto = "\n" + self.status.cget("text")
        if len(texto.split("-")) == 3:
            # Abre arquivo e modifica
            file = open(adress, "a", encoding='utf-8')
            file.writelines(texto)
            # Fecha arquivo
            file.close()
            # Indica que foi salvo com sucesso
            messagebox.showinfo("Arquivo Salvo", "Arquivo salvo com sucesso!")
            # Limpa as entradas
            self.limpa_campos()
            # Seta o label
            self.status["text"] = "Concluído!"
        else:
            # Indica que não foi passado o filme
            messagebox.showinfo("Erro", "Preencha os campos antes de prosseguir!")

    def limpa_campos(self):
        # Limpando campos
        self.entrada_nome.delete(0, END)
        self.entrada_data.delete(0, END)
        self.entrada_fonte.delete(0, END)
        self.status["text"] = ""


# Endereço do arquivo filmes
# adress = "files/filmes.txt"
adress = "C:\Users\dougl\Desktop\#Filmes 2021.txt"
root = Tk()
# Definindo tamanho da janela
root.geometry("475x400")
Application(root)
root.mainloop()
