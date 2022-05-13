
co0 = "#f0f3f5"  # Preta
co1 = "#f0f3f5"  # cizenta / grey
co2 = "#403d3d"  # letra
co3 = "#333333"  # azul escuro / fundo da tela / fundo dos label
co4 = "#666666"  # cinza claro / fundo do frame
co5 = "#759fe6"  # cor da borda - highlightbackground
co6 = "#A8A8A8"  # cinza
co7 = "#6aabb5"  # Botão Adicionar
co8 = "#ffff99"  # Botão Alterar
co9 = "#d54c4a"  # botão excluir
co10 = "white"

import os
from subprocess import call
from tkinter import *
from tkinter import messagebox
from tkinter import tix
import mysql.connector

import sys

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

# - - - Funções dos Botões - - - - -

def abre_cadpessoas():
    call(["python", "Cadastro de Pessoa.py"])

def abre_cadastro_de_usuarios():
    call(["python", "Cadastro_Usuario.py"])

def abre_cad_produto():
    call(["python", "Cadastro_Produto.py"])

def abre_orcar():
    call(["python", "Orçar.py"])

class Gerenciar_Assistencia:
    def __init__(self):
        janela_principal = tix.Tk()
        janela_principal.state("zoomed")
        janela_principal.title("Sistema de Gerenciamento")
        janela_principal.config(bg="#808080")

# - - - Frame - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        LeftFrame = Frame(janela_principal, width=270, height=715, bg=co4)
        LeftFrame.place(x=0, y=0)

# - - - Botões - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        b_cadastro_pessoas = Button(LeftFrame, text="Cadastro de Pessoas", command=abre_cadpessoas, width=40,
                                    font=("Courier", 13, "italic", "bold"), bg="#808000", activebackground="#66FF99",
                                    borderwidth=3)
        b_cadastro_pessoas.place(x=10, y=10, height=60, width=250)
        # balao_cadastro_pessoas = tix.BALLOON(LeftFrame) não está funcionado
        # balao_cadastro_pessoas.bind_widget(b_cadastro_pessoas, ballonmsg="Abre a Tela de Cadastro")

        b_cadastro_funcionarios = Button(LeftFrame, text="Cadastro de Funcionários", command=abre_cadastro_de_usuarios,
                                         width=40, font=("Courier", 13, "italic", "bold"), bg="#808000",
                                         activebackground="#66FF99", borderwidth=3)
        b_cadastro_funcionarios.place(x=10, y=80, height=60, width=250)

        b_cadastro_produtos = Button(LeftFrame, text="Cadastro de Produtos", command=abre_cad_produto, width=40,
                                     font=("Courier", 13, "italic", "bold"), bg="#808000", activebackground="#66FF99",
                                     borderwidth=3)
        b_cadastro_produtos.place(x=10, y=150, height=60, width=250)

        b_venda = Button(LeftFrame, text="Vender", command=abre_orcar, width=40, font=("Courier", 13, "italic", "bold"),
                         bg="#808000", activebackground="#66FF99", borderwidth=3)
        b_venda.place(x=10, y=220, height=60, width=250)

        b_sair = Button(LeftFrame, text="Sair", command=janela_principal.destroy, width=40,
                        font=("Courier", 13, "italic", "bold"), bg="#808000", activebackground="#66FF99", borderwidth=3)
        b_sair.place(x=10, y=290, height=60, width=250)


if __name__ == '__main__':
    GUUEST=Gerenciar_Assistencia()