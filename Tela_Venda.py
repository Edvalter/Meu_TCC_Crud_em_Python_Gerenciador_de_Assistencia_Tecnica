from tkinter import *
from tkinter import ttk
from tkinter import ttk
from tkinter import ttk
from tkinter import ttk
from tkinter import messagebox
from tkinter import tix
from tkinter import font
import mysql.connector
from tkcalendar import Calendar, DateEntry

co0 = "#f0f3f5"  # Preta
co1 = "#f0f3f5"  # cizenta / grey
co2 = "#403d3d"  # letra
co3 = "#333333"  # azul escuro / fundo da tela / fundo dos label
co4 = "#666666"  # roxo claro / fundo do frame
co5 = "#759fe6"  # cor da borda - highlightbackground
co6 = "#A8A8A8"  # cinza
co7 = "#6aabb5"  # Botão Adicionar
co8 = "#ffff99"  # Botão Alterar
co9 = "#d54c4a"  # botão excluir
co10 = "white"

# - - janela Cadastro de Pessoas - -

venda = Tk()

logo = PhotoImage(file="C:/Users/Edinho/PycharmProjects/Meu_TCC/Logo/Obrigaado-removebg-preview.png")

class Aplicacao_Venda():
    def __init__(self):
        self.venda = venda
        self.tela_venda()
        self.frames_venda()

        self.venda.mainloop()

    def tela_venda(self):
        self.venda.title("Vendas")
        self.venda.config(bg=co3)
        self.venda.geometry("1095x700+263+0")

    def frames_venda(self):
        self.frame_superior = Frame(self.venda, bg=co3, highlightbackground=co5, highlightthickness=6)
        self.frame_superior.place(x=10, y=10, height=670, width=1075)

        logoLabel = Label(self.venda, image=logo, bg=co3)
        logoLabel.place(x=100, y=100)

Aplicacao_Venda()