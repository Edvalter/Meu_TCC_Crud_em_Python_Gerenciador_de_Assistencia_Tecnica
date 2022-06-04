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
class Funcao():
    def limpaTela(self):
        self.e_id_pessoa.delete(0, END)
        self.e_nome.delete(0, END)
        self.e_login.delete(0, END)
        self.e_senha.delete(0, END)
        self.e_confirmarSenha.delete(0, END)

    def conecta_bd(self):
        self.conn = mysql.connector.connect(host='localhost', database='gerenciador', user='root', password='admin')
        self.cursor = self.conn.cursor()

    def desconecta_bd(self):
        self.conn.close()

    def montaTabelaFuncionario(self):
        self.conecta_bd()
        self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS funcionario(
                id_pessoa INT PRIMARY KEY,
                nome VARCHAR(100),
                login VARCHAR(100),
                senha VARCHAR(100),
                confirmarSenha VARCHAR(100),
            );
        """)
        self.conn.commit()
        self.desconecta_bd()

    def funcionarioVariaveis(self):
        self.id_pessoa = self.e_id_pessoa.get()
        self.nome = self.e_nome.get()
        self.login = self.e_login.get()
        self.senha = self.e_senha.get()
        self.confirmarSenha = self.e_confirmarSenha.get()

    def adicionaFuncionario(self):
        self.funcionarioVariaveis()

        if self.e_id_pessoa.get() == "" or self.e_login.get() == ""or self.e_senha.get() == ""or self.e_confirmarSenha.get() == "":
            messagebox.showerror(title="Cadastro de Funcionários", message="Todos os Campos Devem Ser Preenchidos")
        else:
            self.conecta_bd()
            self.cursor.execute("""
                INSERT INTO 
                    funcionario(login, senha, confirmarSenha)
                VALUES
                    (%s, %s, %s)""",
                (self.login, self.senha, self.confirmarSenha))

            messagebox.showerror(title="Cadastro de Funcionários", message="Cadastradi")

        self.conn.commit()
        self.desconecta_bd()

    def selectFuncionario(self):
        self.listaFuncionario.delete(*self.listaFuncionario.get_children())
        self.conecta_bd()
        listaFun = self.cursor.execute("""
            SELECT * FROM funcionario; """)

        listaFun = self.cursor.fetchall()

        for i in listaFun:
            self.listaFuncionario.insert("", END, values=i)

        self.desconecta_bd()

    def duploCliqueFuncionario(self, event):
        self.limpaTela()
        self.listaFuncionario.selection()

        for n in self.listaFuncionario.selection():
            col1 = self.listaFuncionario.item(n,'values')

            self.e_nome.insert(END, col1)


    def deletaFuncionario(self):
        self.funcionarioVariaveis()
        self.conecta_bd()
        self.cursor.execute("""
               DELETE FROM funcionario WHERE id_pessoa = %s """, (self.id_pessoa,))

        self.conn.commit()
        self.desconecta_bd()
        self.limpaTela()
        self.selectFuncionario()

    def alteraFuncionario(self):
        self.funcionarioVariaveis()
        self.conecta_bd()
        self.cursor.execute("""
                UPDATE funcionario SET 
                    id_pessoa = %s, 
                    login = %s, 
                    senha = %s, 
                    cofirmarSenha = %s, 
                WHERE
                    id_pessoa = %s""",
                    (self.id_pessoa,
                     self.login,
                     self.senha,
                     self.confirmarSenha))

        self.conn.commit()
        self.desconecta_bd()
        self.selectFuncionario()
        self.limpaTela()

    def buscarPessoa(self):
        self.conecta_bd()
        self.listaFuncionario.delete(*self.listaFuncionario.get_children())

        id_pessoa = self.e_id_pessoa.get()
        nome = self.e_nome.get()


        if len(id_pessoa) > 0:
            self.e_id_pessoa.insert(END, "%")
            id_pessoa = self.e_id_pessoa.get()
            self.cursor.execute("""
                SELECT id_pessoa, nome FROM cad_pessoas WHERE id_pessoa LIKE '%s' ORDER BY id_pessoa ASC""" % id_pessoa, )

            buscaIdFuncionario = self.cursor.fetchall()

            for i in buscaIdFuncionario:
                self.listaFuncionario.insert("", END, values=i)


        elif len(nome) > 0:
            self.e_nome.insert(END, "%")
            nome = self.e_nome.get()
            self.cursor.execute("""
                SELECT * FROM cad_pessoas WHERE nome LIKE '%s' ORDER BY nome ASC""" % nome, )

            buscaNome = self.cursor.fetchall()

            for i in buscaNome:
                self.listaFuncionario.insert("", END, values=i)

class AplicacaoUsuarios(Funcao):
    def __init__(self):
        self.cad_funcionario = cad_funcionario
        self.tela_cad_funcionario()
        self.frame_Cad_Funcionarios()
        self.labelsFuncionario()
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

    def labelsFuncionario(self):
        self.l_id_pessoa = Label(self.frame_superior_funcionarios, text="Código:", font=("Courier", 13, "italic", "bold"), bg=co4, fg=co10)
        self.l_id_pessoa.place(x=110, y=10)
        self.e_id_pessoa = Entry(self.frame_superior_funcionarios, width=45, justify='left', relief='raised', bg=co2, fg=co10)
        self.e_id_pessoa.place(x=190, y=10)

        self.l_nome = Label(self.frame_superior_funcionarios, text="Funcionario:", font=("Courier", 13, "italic", "bold"), bg=co4, fg=co10)
        self.l_nome.place(x=60, y=35)
        self.e_nome = Entry(self.frame_superior_funcionarios, width=45, justify='left', relief='raised', bg=co2, fg=co10)
        self.e_nome.place(x=190, y=35)

        self.l_login = Label(self.frame_superior_funcionarios, text="Login:", font=("Courier", 13, "italic", "bold"), bg=co4, fg=co10)
        self.l_login.place(x=120, y=60)
        self.e_login = Entry(self.frame_superior_funcionarios, width=45, justify='left', relief='raised', bg=co2, fg=co10)
        self.e_login.place(x=190, y=60)

        self.l_senha = Label(self.frame_superior_funcionarios, text="Senha:", font=("Courier", 13, "italic", "bold"), bg=co4, fg=co10)
        self.l_senha.place(x=120, y=85)
        self.e_senha = Entry(self.frame_superior_funcionarios, width=45, justify='left', relief='raised', bg=co2, fg=co10)
        self.e_senha.place(x=190, y=85)

        self.l_confirmarSenha = Label(self.frame_superior_funcionarios, text="Confirme a Senha:", font=("Courier", 13, "italic", "bold"), bg=co4, fg=co10)
        self.l_confirmarSenha.place(x=10, y=110)
        self.e_confirmarSenha = Entry(self.frame_superior_funcionarios, width=45, justify='left', relief='raised', bg=co2, fg=co10)
        self.e_confirmarSenha.place(x=190, y=110)

    def botoes_tela_cad_funcionario(self):
        self.b_limpar = Button(self.frame_superior_funcionarios, text="Limpar", command=self.limpaTela, width=10,
                               font=("Courier", 13, "italic", "bold"), bg=co6, fg=co2, relief=RAISED, overrelief=RIDGE)
        self.b_limpar.place(x=280, y=185, height=40, width=100)

        self.b_procurarPessoa = Button(self.frame_superior_funcionarios, text="Procurar", command=self.buscarPessoa, width=10, font=("Courier", 13, "italic", "bold"), bg=co6, fg=co2, relief=RAISED, overrelief=RIDGE)
        self.b_procurarPessoa.place(x=470, y=10, height=45, width=100)

        self.b_procurarFuncionario = Button(self.frame_superior_funcionarios, text="Procurar",
                                       width=10, font=("Courier", 13, "italic", "bold"), bg=co6, fg=co2, relief=RAISED, overrelief=RIDGE)
        self.b_procurarFuncionario.place(x=390, y=185, height=40, width=100)

        self.b_adicionar = Button(self.frame_superior_funcionarios, text="Adicionar", command=self.adicionaFuncionario, width=10, font=("Courier", 13, "italic", "bold"),  bg=co7, fg=co2, relief=RAISED, overrelief=RIDGE)
        self.b_adicionar.place(x=500, y=185, height=40, width=100)

        self.b_alterar = Button(self.frame_superior_funcionarios, text="Alterar", width=10, font=("Courier", 13, "italic", "bold"), bg=co8, fg=co2, relief=RAISED, overrelief=RIDGE)
        self.b_alterar.place(x=610, y=185, height=40, width=100)

        self.b_excluir = Button(self.frame_superior_funcionarios, text="Excluir", width=10, font=("Courier", 13, "italic", "bold"), bg=co9, fg=co2, relief=RAISED, overrelief=RIDGE)
        self.b_excluir.place(x=720, y=185, height=40, width=100)

    def grid_cad_funcionario(self):
        self.listaFuncionario = ttk.Treeview(self.frame_grid_funcionarios, columns=("col0", "col1", "col2", "col3"))
        self.listaFuncionario.heading("#0", text="")
        self.listaFuncionario.heading("#1", text="Código")
        self.listaFuncionario.heading("#2", text="Login")
        self.listaFuncionario.heading("#3", text="Senha")
        self.listaFuncionario.heading("#4", text="Confirmar Senha")

        self.listaFuncionario.column("#0", width=2)
        self.listaFuncionario.column("#1", width=125)
        self.listaFuncionario.column("#2", width=125)
        self.listaFuncionario.column("#3", width=125)
        self.listaFuncionario.column("#4", width=125)

        self.listaFuncionario.place(x=10, y=10, height=340, width=1035)

        self.barra_vertical = ttk.Scrollbar(self.frame_grid_funcionarios, orient='vertical', command=self.listaFuncionario.yview)
        self.barra_vertical.place(x=1048, y=0, height=369, width=15)

        self.barra_horizontal = ttk.Scrollbar(self.frame_grid_funcionarios, orient='horizontal', command=self.listaFuncionario.xview)
        self.barra_horizontal.place(x=0, y=354, height=15, width=1050)

        self.listaFuncionario.configure(yscrollcommand=self.barra_vertical.set, xscrollcommand=self.barra_horizontal.set)

        self.listaFuncionario.bind("<Double-1>", self.duploCliqueFuncionario)

AplicacaoUsuarios()

