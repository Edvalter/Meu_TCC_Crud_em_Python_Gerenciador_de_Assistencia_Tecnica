
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
import win32




"""

"""


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

TelaDeLogin = Tk()

logo = PhotoImage(file="C:/Users/Edinho/PycharmProjects/Meu_TCC/Logo/Segat_Logo.png")

class Login():
# - - Limpar a Tela - - - - - - - - - - - - - - - -
    def limpaTela(self):
        self.e_login.delete(0, END)
        self.e_senha.delete(0, END)
        self.e_login.focus()

# - - Conectar ao Banco de Dados - - - - - - - - - - - - - - - -
    def conecta_bd(self):
        self.conn = mysql.connector.connect(host='localhost', database='gerenciador', user='root', password='admin')
        self.cursor = self.conn.cursor()

# - - Desconectar ao Banco de Dados  - - - - - - - - - - - - - - - -
    def desconecta_bd(self):
        self.conn.close()

# - - Função Entrar - - - - - - - - - - - - - - - -
    def entra(self):
        self.conecta_bd()
        self.login = self.e_login.get()
        self.senha = self.e_senha.get()

        self.valida_login = self.cursor.execute(f"""SELECT login from funcionario WHERE login = '{self.login}'""")
        self.valida_login = self.cursor.fetchone()
        if self.valida_login is None:
            self.valida_login = None
        else:
            self.valida_login = self.valida_login[0]
        self.valida_senha = self.cursor.execute(f"""SELECT senha FROM funcionario WHERE login = '{self.login}' and 
                                                senha = '{self.senha}';""")
        self.valida_senha = self.cursor.fetchone()
        if self.valida_senha is None:
            self.valida_senha = None
        else:
            self.valida_senha = self.valida_senha[0]

        if self.login == '':
            messagebox.showerror(title="Acesso Negado", message="Usuário não informado!")

        elif self.valida_login is not None:
            if self.valida_senha is not None:
                self.TelaDeLogin.destroy()
                call(["python", "Tela_Janela_Principal.py"])

            elif self.valida_senha is None:
                messagebox.showerror(title="Acesso Negado", message="Senha incorreta!")

        elif self.valida_login is None:
            messagebox.showerror(title="Acesso Negado", message="Dados informados incorretos!")

        self.desconecta_bd()

class Aplicacao_Login(Login):
    def __init__(self):

        self.TelaDeLogin = TelaDeLogin
        self.tela_login()
        self.labels_login()
        self.botao()

        self.TelaDeLogin.mainloop()

# - - Configurando as posições/medidas da tela de login - - - - - - - - -
    def tela_login(self):
        self.TelaDeLogin.title("")
        self.TelaDeLogin.config(bg=co6)
        self.TelaDeLogin.geometry("242x300+550+200")
        self.TelaDeLogin.resizable(width=False, height=False)
        self.TelaDeLogin.iconbitmap("C:/Users/Edinho/PycharmProjects/Meu_TCC/Logo/segatIcone.ico")

    # - - Posição dos Label's e Entry's - - - - - - - - - - - - - - - - - -
    def labels_login(self):
        self.l_login = Label(self.TelaDeLogin, text="Login", font=("Courier", 13, "italic", "bold"), bg=co6, fg=co10)
        self.l_login.place(x=90, y=140)
        self.e_login = Entry(self.TelaDeLogin, justify='center', relief='raised', bg=co0, fg=co10)
        self.e_login.place(x=70, y=125, width=100)

        self.l_senha = Label(self.TelaDeLogin, text="Senha", font=("Courier", 13, "italic", "bold"), bg=co6, fg=co10)
        self.l_senha.place(x=90, y=195)
        self.e_senha = Entry(self.TelaDeLogin, show="*", justify='center', relief='raised', bg=co0, fg=co10)
        self.e_senha.place(x=70, y=180, width=100)

        logoLabel = Label(self.TelaDeLogin, image=logo, bg=co6)
        logoLabel.place(x=15, y=0)

# - - Botão Entrar - - - - - - - - - - - - - - - - - - - - - - - - - -
    def botao(self):
        self.b_entrar = Button(self.TelaDeLogin, text="Entrar", command=self.entra, font=("Courier", 13, "italic", "bold"), bg=co1, fg=co10)
        self.b_entrar.place(x=70, y=250, width=100)

Aplicacao_Login()