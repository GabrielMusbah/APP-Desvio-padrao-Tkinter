from tkinter import *
import numpy #biblioteca usada para fazer a media dos valores presentes na lista
import math #biblioteca de funcoes matematicas, usado para fazer a raiz

class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer["background"] = "white"
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer["background"] = "white"
        self.segundoContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer["background"] = "white"
        self.quartoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="Desvio Padrão")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo["background"] = "white"
        self.titulo.pack()

        self.nomeLabel = Label(self.segundoContainer,text="Lista Numeros", font=self.fontePadrao)
        self.nomeLabel["background"] = "white"
        self.nomeLabel.pack(side=LEFT)

        self.nome = Entry(self.segundoContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome["borderwidth"] = 3
        self.nome["relief"] = "ridge"
        self.nome.pack(side=LEFT)

        self.autenticar = Button(self.quartoContainer)
        self.autenticar["text"] = "Calcular"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["foreground"] = "white"
        self.autenticar["background"] = "grey"
        self.autenticar["command"] = self.calcular
        self.autenticar.pack()

        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem["background"] = "white"
        self.mensagem.pack()


    def calcular(self):
        usuario = self.nome.get()
        lista = usuario.split()
        listaNum = list(map(float, lista))
        mediaLista = numpy.mean(listaNum)
        quantidadeNumero = len(listaNum)
        quantidadeNumero2 = len(listaNum)

        listaComMedia = []
        while quantidadeNumero > 0:
            listaComMedia.append(mediaLista)
            quantidadeNumero = quantidadeNumero - 1


        listaNumeroMenosMedia = [(a - b) for a, b in zip(listaNum, listaComMedia)]

        listaNumeroMenosMediaAoQuadrado = [(a * b) for a, b in zip(listaNumeroMenosMedia, listaNumeroMenosMedia)]

        somaLista = sum(listaNumeroMenosMediaAoQuadrado)

        dividirSomaPorQuantidadeNumero = somaLista / (quantidadeNumero2 - 1)

        if (dividirSomaPorQuantidadeNumero < 0):
            dividirSomaPorQuantidadeNumeroPronto = dividirSomaPorQuantidadeNumero * -1
        else:
            dividirSomaPorQuantidadeNumeroPronto = dividirSomaPorQuantidadeNumero

        desvioPadrao = math.sqrt(dividirSomaPorQuantidadeNumeroPronto)

        desvioPadraoArend = round(desvioPadrao, 5)

        desvioPadraoStr = str(desvioPadraoArend)

        self.mensagem["text"] = "O desvio padrão: "+desvioPadraoStr


root = Tk()
root.title("Calculadora de desvio padrão")
Application(root)
root.configure(bg= "white")
root.mainloop()
