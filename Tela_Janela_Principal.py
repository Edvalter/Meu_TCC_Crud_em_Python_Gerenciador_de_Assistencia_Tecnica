

import os
import pickle
import sys
from tkinter import *
from tkinter import messagebox
from subprocess import call
from tkinter import ttk
from view import *
import view
import mysql.connector
from tkcalendar import Calendar, DateEntry
import calendar


# Configuração das Cores

co0 = "#f0f3f5"  # white
co1 = "#f0f3f5"  # cizenta / grey
co2 = "#403d3d"  # letra
co3 = "#333333"  # azul escuro / fundo da tela / fundo dos label
co4 = "#666666"  # roxo claro / fundo do frame
co5 = "#759fe6"  # cor da borda - highlightbackground

co7 = "#6aabb5"  # Botão Adicionar
co8 = "#ffff99"  # Botão Alterar

co9 = "orange"  # em uso = laranja botão excluir
co6 = "#A8A8A8"  # em uso = cinza  fundo dos labels e do frame
co10 = "Black" # em uso = cor da fonte

try:
    from Tkinter import *
except ImportError:
    from tkinter import*

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

janela_principal = Tk()

logo = PhotoImage(file="C:/Users/Edinho/PycharmProjects/Meu_TCC/Logo/LogoEsc.png")

# - - - Funções dos Botões - - - - -


def abre_cad_pessoa():
    call(["python", "Cadastro_Pessoa.py"])

def abre_cad_usuario():
    call(["python", "Cadastro_Usuario.py"])

def abre_cad_produto():
    call(["python", "Cadastro_Produto.py"])

def abre_orcamento():
    call(["python", "Tela_Orcamento.py"])

def abre_venda():
   call(["python", "Tela_Venda.py"])

def abre_relatorio():
   call(["python", "Tela_Relatorio.py"])


class Janela_Principal():
    def __init__(self):
        self.janela_principal = janela_principal
        self.Tela_Principal()
        self.Frames()
        self.botoes()

        self.janela_principal.mainloop()

    def Tela_Principal(self):
        self.janela_principal.state("zoomed")
        self.janela_principal.title("Sistema Gerenciador de Assistência Técnica")
        self.janela_principal.config(bg=co6)
        self.janela_principal.iconbitmap("C:/Users/Edinho/PycharmProjects/Meu_TCC/Logo/segatIcone.ico")

    def Frames(self):
        self.LeftFrame = Frame(janela_principal, width=270, height=715, bg=co4)
        self.LeftFrame.place(x=0, y=0)

    def botoes(self):
        b_cadastro_pessoas = Button(self.LeftFrame, text="Cadastro de Pessoas", command=abre_cad_pessoa,
                                    font=("Courier", 13, "italic", "bold"), bg="#808000", activebackground="#66FF99",
                                    borderwidth=3)
        b_cadastro_pessoas.place(x=10, y=10, height=60, width=250)

        b_cadastro_funcionarios = Button(self.LeftFrame, text="Cadastro de Funcionários", command=abre_cad_usuario,
                                         font=("Courier", 13, "italic", "bold"), bg="#808000",
                                         activebackground="#66FF99", borderwidth=3)
        b_cadastro_funcionarios.place(x=10, y=80, height=60, width=250)

        b_cadastro_produtos = Button(self.LeftFrame, text="Cadastro de Produtos", command=abre_cad_produto,
                                     font=("Courier", 13, "italic", "bold"), bg="#808000", activebackground="#66FF99",
                                     borderwidth=3)
        b_cadastro_produtos.place(x=10, y=150, height=60, width=250)

        b_orcamento = Button(self.LeftFrame, text="Orçar", command=abre_orcamento, font=("Courier", 13, "italic", "bold"),
                         bg="#808000", activebackground="#66FF99", borderwidth=3)
        b_orcamento.place(x=10, y=220, height=60, width=250)

        b_venda = Button(self.LeftFrame, text="Vender", command=abre_venda, font=("Courier", 13, "italic", "bold"),
                         bg="#808000", activebackground="#66FF99", borderwidth=3)
        b_venda.place(x=10, y=290, height=60, width=250)

        b_relatorio = Button(self.LeftFrame, text="Relatório", command=abre_relatorio, font=("Courier", 13, "italic", "bold"),
                             bg="#808000", activebackground="#66FF99", borderwidth=3)
        b_relatorio.place(x=10, y=360, height=60, width=250)

        b_sair = Button(self.LeftFrame, text="Sair", command=janela_principal.destroy,
                        font=("Courier", 13, "italic", "bold"), bg="#808000", activebackground="#66FF99", borderwidth=3)
        b_sair.place(x=10, y=430, height=60, width=250)

        logoLabel = Label(janela_principal,  image=logo, bg=co6)
        logoLabel.place(x=630, y=240)


Janela_Principal()