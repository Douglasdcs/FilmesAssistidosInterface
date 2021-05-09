from tkinter import *


# Classe do container principal
class Application:
    def __init__(self, master=None):
        # master é o container elementar da interface
        self.widget1 = Frame(master)
        # Informa-se que será usado a geometria pack() [Podendo ser: grid, pack, place]
        self.widget1.pack()
        # Dentro desse container, imprime-se a mensagem abaixo
        self.msg = Label(self.widget1, text="Primeiro widget")
        self.msg.pack()


root = Tk()
Application(root)
root.mainloop()
