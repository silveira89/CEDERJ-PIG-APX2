from tkinter import *
from questao_1 import sorter

def criar():
    s = sorter()
    k = int(entrada.get())
    lista = sorter.randomList(k)
    lista_ord = s.sort(lista)
    mensagem1["text"]= lista
    mensagem2["text"]= lista_ord

window = Tk()
window.geometry("500x150+100+100")
window.title("Lista")
entrada = Entry(window, font="arial 15")
entrada.pack()

mensagem1 = Label(window, text=" ", font="impact 15")
mensagem1.pack()

mensagem2 = Label(window, text=" ", font="impact 15")
mensagem2.pack()

botao = Button(window, text="Criar lista", command=criar)
botao.pack()

window.mainloop()
