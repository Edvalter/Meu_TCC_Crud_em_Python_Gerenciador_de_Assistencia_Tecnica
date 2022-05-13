import os
import pickle
import sys
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from view import *
import view
import mysql.connector

# Configuração das Cores

co0 = "#f0f3f5"  # Preta
co1 = "#f0f3f5"  # cizenta / grey
co2 = "#403d3d"  # letra
co3 = "#333333"  # azul escuro / fundo da tela / fundo dos label
co4 = "#666666"  # roxo claro / fundo do frame
co5 = "#759fe6"  # cor da borda - highlightbackground
co6 = "#A8A8A8"  # cinza
co7 ="#6aabb5" # Botão Adicionar
co8 =  "#ffff99" # Botão Alterar
co9 ="#d54c4a" # botão excluir
co10 = "white"

# - - janela Cadastro de Produtos - -

cad_funcionario = Tk()

class Aplicacao_Cad_Funcionarios():
    def __init__(self):
        self.cad_funcionario = cad_funcionario
        self.tela_cad_funcionario()
        self.frame_Cad_Funcionarios()
        self.labels_entry_funcionario()
        self.botoes_tela_cad_funcionario()
        self.grid_cad_funcionario()

        self.cad_funcionario.mainloop()

    def tela_cad_funcionario(self):
        self.cad_funcionario.title("Cadastro de Funcionários")
        self.cad_funcionario.config(bg=co3)
        self.cad_funcionario.geometry("1095x680+263+0")

    def frame_Cad_Funcionarios(self):
        self.frame_superior_funcionarios = Frame(self.cad_funcionario, height=280, width=1365, bd=4, bg=co4, highlightbackground=co5, highlightthickness=6)
        self.frame_superior_funcionarios.place(x=10, y=10, height=250, width=1075)

        self.frame_grid_funcionarios = Frame(self.cad_funcionario, height=418, width=1365, bg=co10, highlightbackground=co5, highlightthickness=6)
        self.frame_grid_funcionarios.place(x=10, y=280, height=380, width=1075)

    def labels_entry_funcionario(self):
        self.l_cpf = Label(self.frame_superior_funcionarios, text="Cpf:",
                           font=("Courier", 13, "italic", "bold"), bg=co4, fg=co10)
        self.l_cpf.place(x=70, y=10)
        self.e_cpf = Entry(self.frame_superior_funcionarios, width=45, justify='left', relief='raised', bg=co2, fg=co10)
        self.e_cpf.place(x=120, y=10)

        self.l_codigo = Label(self.frame_superior_funcionarios, text="Código:",
                              font=("Courier", 13, "italic", "bold"), bg=co4, fg=co10)
        self.l_codigo.place(x=40, y=35)
        self.e_codigo = Entry(self.frame_superior_funcionarios, width=45, justify='left', relief='raised', bg=co2, fg=co10)
        self.e_codigo.place(x=120, y=35)

        self.l_nome = Label(self.frame_superior_funcionarios, text="Nome:",
                            font=("Courier", 13, "italic", "bold"), bg=co4, fg=co10)
        self.l_nome.place(x=60, y=60)
        self.e_nome = Entry(self.frame_superior_funcionarios, width=45, justify='left', relief='raised', bg=co2, fg=co10)
        self.e_nome.place(x=120, y=60)

        self.l_telefone = Label(self.frame_superior_funcionarios, text="Telefone:",
                                font=("Courier", 13, "italic", "bold"), bg=co4, fg=co10)
        self.l_telefone.place(x=20, y=85)
        self.e_telefone = Entry(self.frame_superior_funcionarios, width=45, justify='left', relief='raised', bg=co2, fg=co10)
        self.e_telefone.place(x=120, y=85)

        self.l_whatsapp = Label(self.frame_superior_funcionarios, text="Whatsapp:",
                                font=("Courier", 13, "italic", "bold"), bg=co4, fg=co10)
        self.l_whatsapp.place(x=20, y=110)
        self.e_whatsapp = Entry(self.frame_superior_funcionarios, width=45, justify='left', relief='raised', bg=co2, fg=co10)
        self.e_whatsapp.place(x=120, y=110)

        self.l_email = Label(self.frame_superior_funcionarios, text="E-mail:",
                             font=("Courier", 13, "italic", "bold"), bg=co4, fg=co10)
        self.l_email.place(x=520, y=10)
        self.e_email = Entry(self.frame_superior_funcionarios, width=45, justify='left', relief='raised', bg=co2, fg=co10)
        self.e_email.place(x=600, y=10)

        self.l_login = Label(self.frame_superior_funcionarios, text="Login:",
                             font=("Courier", 13, "italic", "bold"), bg=co4, fg=co10)
        self.l_login.place(x=530, y=35)
        self.e_login = Entry(self.frame_superior_funcionarios, width=45, justify='left', relief='raised', bg=co2, fg=co10)
        self.e_login.place(x=600, y=35)

        self.l_senha = Label(self.frame_superior_funcionarios, text="Senha:",
                             font=("Courier", 13, "italic", "bold"), bg=co4, fg=co10)
        self.l_senha.place(x=530, y=60)
        self.e_senha = Entry(self.frame_superior_funcionarios, width=45, justify='left', relief='raised', bg=co2, fg=co10)
        self.e_senha.place(x=600, y=60)

        self.l_confirmarsenha = Label(self.frame_superior_funcionarios, text="Confirme a Senha:",
                                      font=("Courier", 13, "italic", "bold"), bg=co4, fg=co10)
        self.l_confirmarsenha.place(x=420, y=85)
        self.e_confirmarsenha = Entry(self.frame_superior_funcionarios, width=45, justify='left', relief='raised', bg=co2, fg=co10)
        self.e_confirmarsenha.place(x=600, y=85)

    def botoes_tela_cad_funcionario(self):
        self.b_limpar = Button(self.frame_superior_funcionarios, text="Limpar", width=10,
                               font=('Ivy 8 bold'), bg=co6, fg=co2, relief=RAISED, overrelief=RIDGE)
        self.b_limpar.place(x=280, y=185, height=40, width=100)

        self.b_procurar = Button(self.frame_superior_funcionarios, text="Procurar:", width=10, font=('Ivy 8 bold'), bg=co6, fg=co2, relief=RAISED, overrelief=RIDGE)
        self.b_procurar.place(x=390, y=185, height=40, width=100)

        self.b_adicionar = Button(self.frame_superior_funcionarios, text="Adicionar:", width=10, font=('Ivy 8 bold'),  bg=co7, fg=co2, relief=RAISED, overrelief=RIDGE)
        self.b_adicionar.place(x=500, y=185, height=40, width=100)

        self.b_alterar = Button(self.frame_superior_funcionarios, text="Alterar:", width=10, font=('Ivy 8 bold'), bg=co8, fg=co2, relief=RAISED, overrelief=RIDGE)
        self.b_alterar.place(x=610, y=185, height=40, width=100)

        self.b_excluir = Button(self.frame_superior_funcionarios, text="Excluir:", width=10, font=('Ivy 8 bold'), bg=co9, fg=co2, relief=RAISED, overrelief=RIDGE)
        self.b_excluir.place(x=720, y=185, height=40, width=100)

    def grid_cad_funcionario(self):
        self.listafuncionaro = ttk.Treeview(self.frame_grid_funcionarios, columns=("col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8"))
        self.listafuncionaro.heading("#0", text="Código")
        self.listafuncionaro.heading("#1", text="CPF")
        self.listafuncionaro.heading("#2", text="Nome")
        self.listafuncionaro.heading("#3", text="Telefone")
        self.listafuncionaro.heading("#4", text="WhatsApp")
        self.listafuncionaro.heading("#5", text="E-mail")
        self.listafuncionaro.heading("#6", text="Login")
        self.listafuncionaro.heading("#7", text="Senha")
        self.listafuncionaro.heading("#8", text="Confirmar Senha")

        self.listafuncionaro.column("#0", width=50)
        self.listafuncionaro.column("#1", width=125)
        self.listafuncionaro.column("#2", width=125)
        self.listafuncionaro.column("#3", width=125)
        self.listafuncionaro.column("#4", width=125)
        self.listafuncionaro.column("#5", width=125)
        self.listafuncionaro.column("#6", width=125)
        self.listafuncionaro.column("#7", width=125)
        self.listafuncionaro.column("#8", width=125)

        self.listafuncionaro.place(x=10, y=10, height=340, width=1035)

        self.barra_vertical = ttk.Scrollbar(self.frame_grid_funcionarios, orient='vertical', command=self.listafuncionaro.yview)
        self.barra_vertical.place(x=1048, y=0, height=369, width=15)

        self.barra_horizontal = ttk.Scrollbar(self.frame_grid_funcionarios, orient='horizontal', command=self.listafuncionaro.xview)
        self.barra_horizontal.place(x=0, y=354, height=15, width=1050)

        self.listafuncionaro.configure(yscrollcommand=self.barra_vertical.set, xscrollcommand=self.barra_horizontal.set)

Aplicacao_Cad_Funcionarios()

