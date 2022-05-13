
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

co0 = "#f0f3f5"  # Preta
co1 = "#f0f3f5"  # cizenta / grey
co2 = "#403d3d"  # letra
co3 = "#333333"  # azul escuro / fundo da tela / fundo dos label
co4 = "#666666"  # roxo claro / fundo do frame
co5 = "#759fe6"  # cor da borda - highlightbackground
co6 = "#A8A8A8"  # cinza
co7 = "#6aabb5"  # Botão Adicionar
co8 =  "#ffff99"  # Botão Alterar
co9 =  "#d54c4a"  # botão excluir
co10 = "white"


login = Tk()

class Aplicacao_Login():
    def __init__(self):
        self.login = login
        self.tela_login()
        self.labels_login()
        self.botao()


        self.login.mainloop()

    def tela_login(self):
        self.login.title("Segat")
        self.login.config(bg=co3)
        self.login.geometry("300x250+550+250")
        self.login.resizable(width=False, height=False)

    def labels_login(self):
        self.l_login = Label(self.login, text="Login", font=("Courier", 15, "italic", "bold"), bg=co3, fg=co10)
        self.l_login.place(x=110, y=15)
        self.e_login = Entry(self.login, justify='center', relief='raised', bg=co2, fg=co10)
        self.e_login.place(x=100, y=40, width=100)

        self.l_senha = Label(self.login, text="Senha", font=("Courier", 15, "italic", "bold"), bg=co3, fg=co10)
        self.l_senha.place(x=110, y=65)
        self.e_senha = Entry(self.login, justify='center', show="*", relief='raised', bg=co2, fg=co10)
        self.e_senha.place(x=100, y=90, width=100)

    def botao(self):
        self.b_entrar = Button(self.login, text="Entrar", command=self.entra, font=("Courier", 15, "italic", "bold"), bg=co3, fg=co10)
        self.b_entrar.place(x=100, y=150, width=100)

    def entra(self):
        login = self.e_login.get()
        senha = self.e_senha.get()

        if login == "edi" and senha == "edi":
            print("Logou")
            self.login.destroy()
            call(["python", "Tela_Janela_Principal.py"])

        else:
            messagebox.showerror(title="Acesso Negado", message="Verifique Login e Senha")

Aplicacao_Login()
