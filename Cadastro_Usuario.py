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
co7 = "#6aabb5"  # Botão Adicionar
co8 = "#ffff99"  # Botão Alterar


co9 = "orange"  # em uso = laranja botão excluir
co6 = "#A8A8A8"  # em uso = cinza  fundo dos labels e do frame
co10 = "Black" # em uso = cor da fonte
co11 = "white" # em uso no fundo do grid

# - - janela Cadastro de Produtos - -

cad_funcionario = Tk()
class Funcao():
    def limpaTela(self):
        self.e_id_funcionario.delete(0, END)
        self.e_id_pessoa.delete(0, END)
        self.e_nome.delete(0, END)
        self.e_login.delete(0, END)
        self.e_senha.delete(0, END)
        self.e_confirmar_senha.delete(0, END)

    def conecta_bd(self):
        self.conn = mysql.connector.connect(host='localhost', database='gerenciador', user='root', password='admin')
        self.cursor = self.conn.cursor()

    def desconecta_bd(self):
        self.conn.close()

    def montaTabelaFuncionario(self):
        self.conecta_bd()
        self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS funcionario(
                    id_funcionario INT PRIMARY KEY AUTO_INCREMENT,
                    id_pessoa INT, 
                    nome VARCHAR(100),
                    login VARCHAR(100),
                    senha VARCHAR(100),
                    confirmar_senha VARCHAR(100)
                    );
                """)
        self.conn.commit()
        self.desconecta_bd()

    def funcionarioVariaveis(self):
        self.id_funcionario = self.e_id_funcionario.get()
        self.id_pessoa = self.e_id_pessoa.get()
        self.nome = self.e_nome.get()
        self.login = self.e_login.get()
        self.senha = self.e_senha.get()
        self.confirmar_senha = self.e_confirmar_senha.get()

    def adicionaFuncionario(self):
        self.funcionarioVariaveis()

        if self.e_id_pessoa.get() == "" or self.e_login.get() == "" or self.e_senha.get() == "" or self.e_confirmar_senha.get() == "":
            messagebox.showerror(title="Cadastro de Funcionários", message="Todos os Campos Devem Ser Preenchidos")
            pass

        elif self.e_senha.get() != self.e_confirmar_senha.get():
            messagebox.showerror(title="Cadastro de Funcionários", message="Campo SENHA é diferente do CONFIRMAR SENHA")
            pass

        else:
            self.conecta_bd()
            self.cursor.execute("""
                INSERT INTO 
                    funcionario(
                        id_pessoa, 
                        nome, 
                        login, 
                        senha, 
                        confirmar_senha)
                VALUES
                    (%s, %s, %s, %s, %s)""",
                        (self.id_pessoa,
                         self.nome,
                         self.login,
                         self.senha,
                         self.confirmar_senha))

            messagebox.showinfo(title="Cadastro de Funcionários", message="Usuário Cadastrado com Sucesso")

        self.conn.commit()
        self.desconecta_bd()
        self.selecionaFuncionario()


    def selecionaPessoa(self):
        self.listaPessoas.delete(*self.listaPessoas.get_children())
        self.conecta_bd()
        listaPe = self.cursor.execute("""
            SELECT id_pessoa, nome FROM pessoas WHERE status_pessoa <> 'Cliente' ORDER BY id_pessoa ASC; """)

        listaPe = self.cursor.fetchall()

        for i in listaPe:
            self.listaPessoas.insert("", END, values=i)

        self.desconecta_bd()

    def selecionaFuncionario(self):
        self.listaFuncionario.delete(*self.listaFuncionario.get_children())
        self.conecta_bd()
        listaFun = self.cursor.execute(""" SELECT * FROM funcionario; """)
        listaFun = self.cursor.fetchall()

        for i in listaFun:
            self.listaFuncionario.insert("", END, values=i)

        self.desconecta_bd()

    def duploCliquePessoa(self, event):
        self.limpaTela()
        self.listaPessoas.selection()

        for n in self.listaPessoas.selection():
            col0, col1 = self.listaPessoas.item(n, 'values')

            self.e_id_pessoa.insert(END, col0)
            self.e_nome.insert(END, col1)


    def duploCliqueFuncionario(self, event):
        self.limpaTela()
        self.listaFuncionario.selection()

        for n in self.listaFuncionario.selection():
            col0, col1, col2, col3, col4, col5 = self.listaFuncionario.item(n, 'values')

            self.e_id_funcionario.insert(END, col0)
            self.e_id_pessoa.insert(END, col1)
            self.e_nome.insert(END, col2)
            self.e_login.insert(END, col3)
            self.e_senha.insert(END, col4)
            self.e_confirmar_senha.insert(END, col5)


    def deletaFuncionario(self):
        self.funcionarioVariaveis()
        self.conecta_bd()
        self.cursor.execute(f"""
               DELETE FROM funcionario WHERE id_funcionario= '%{self.id_funcionario}%'; """)
        messagebox.showinfo(title="Cadastro de Funcionários", message="Usuário excluído com Sucesso")

        self.conn.commit()
        self.desconecta_bd()
        self.limpaTela()
        self.selecionaFuncionario()

    def alteraFuncionario(self):
        self.funcionarioVariaveis()
        if self.e_id_pessoa.get() == "" or self.e_login.get() == ""or self.e_senha.get() == ""or self.e_confirmar_senha.get() == "":
            messagebox.showerror(title="Cadastro de Funcionários", message="Todos os Campos Devem Ser Preenchidos")
            pass

        elif self.e_senha.get() != self.e_confirmar_senha.get():
            messagebox.showerror(title="Cadastro de Funcionários", message="Campo SENHA é diferente do CONFIRMAR SENHA")
            pass
        else:
            self.conecta_bd()
            self.cursor.execute("""
                UPDATE 
                    funcionario 
                SET 
                    id_pessoa = %s, 
                    nome = %s, 
                    login = %s, 
                    senha = %s,
                    confirmar_senha = %s
                WHERE
                    id_funcionario = %s""", (
                    self.id_pessoa,
                    self.nome,
                    self.login,
                    self.senha,
                    self.confirmar_senha,
                    self.id_funcionario))

            messagebox.showinfo(title="Cadastrado de Funcionário", message="Login do Funcionário Alterado com Sucesso")

        self.conn.commit()
        self.desconecta_bd()
        self.selecionaFuncionario()
        self.limpaTela()

    def buscarPessoa(self):
        self.conecta_bd()
        self.listaPessoas.delete(*self.listaPessoas.get_children())

        id_pessoa = self.e_id_pessoa.get()
        nome = self.e_nome.get()

        if len(id_pessoa) > 0:
            self.e_id_pessoa.insert(END, "")
            id_pessoa = self.e_id_pessoa.get()
            self.cursor.execute(f"""
                SELECT id_pessoa, nome 
                FROM 
                    pessoas 
                WHERE 
                    id_pessoa 
                LIKE '%{id_pessoa}' ORDER BY id_pessoa ASC; """)

            buscaIdPessoa = self.cursor.fetchall()

            for i in buscaIdPessoa:
                self.listaPessoas.insert("", END, values=i)

        elif len(nome) > 0:
            self.e_nome.insert(END, "")
            nome = self.e_nome.get()
            self.cursor.execute(f"""
                SELECT 
                    id_pessoa, nome  
                FROM 
                    pessoas 
                WHERE 
                    nome 
                LIKE '%{nome}' ORDER BY nome ASC; """)

            buscaNome = self.cursor.fetchall()

            for i in buscaNome:
                self.listaPessoas.insert("", END, values=i)

    def buscarFuncionario(self):
        self.conecta_bd()
        self.listaFuncionario.delete(*self.listaFuncionario.get_children())

        id_funcionario = self.e_id_funcionario.get()
        id_pessoa = self.e_id_pessoa.get()
        nome = self.e_nome.get()

        if len(id_funcionario) > 0:
            self.e_id_funcionario.insert(END, "")
            id_pessoa = self.e_id_funcionario.get()
            self.cursor.execute(f"""
                SELECT * FROM 
                    funcionario 
                WHERE 
                    id_funcionario 
                LIKE '%{id_funcionario}' ORDER BY id_funcionario ASC; """)

            buscaIdFuncionario = self.cursor.fetchall()

            for i in buscaIdFuncionario:
                self.listaFuncionario.insert("", END, values=i)


        elif len(id_pessoa) > 0:
            self.e_id_pessoa.insert(END, "")
            id_pessoa = self.e_id_pessoa.get()
            self.cursor.execute(f"""
                SELECT * FROM 
                    funcionario 
                WHERE 
                    id_pessoa
                LIKE '%{id_pessoa}%' ORDER BY nome ASC; """)

            buscaIdPessoa = self.cursor.fetchall()

            for i in buscaIdPessoa:
                self.listaFuncionario.insert("", END, values=i)

        elif len(nome) > 0:
            self.e_nome.insert(END, "")
            nome = self.e_nome.get()
            self.cursor.execute(f"""
                SELECT * FROM 
                    funcionario 
                WHERE 
                    nome 
                LIKE '%{nome}%' ORDER BY nome ASC; """)

            buscaNome = self.cursor.fetchall()

            for i in buscaNome:
                self.listaFuncionario.insert("", END, values=i)



class AplicacaoUsuarios(Funcao):
    def __init__(self):
        self.cad_funcionario = cad_funcionario
        self.tela_cad_funcionario()
        self.frame_Cad_Funcionarios()
        self.labelsFuncionario()
        self.botoesFuncionario()
        self.gridPessoas()
        self.gridFuncionario()
        self.selecionaPessoa()
        self.selecionaFuncionario()

        self.cad_funcionario.mainloop()

    def tela_cad_funcionario(self):
        self.cad_funcionario.title("Cadastro de Funcionários")
        self.cad_funcionario.config(bg=co3)
        self.cad_funcionario.geometry("1095x700+263+0")
        self.cad_funcionario.iconbitmap("C:/Users/Edinho/PycharmProjects/Meu_TCC/Logo/segatIcone.ico")

    def frame_Cad_Funcionarios(self):
        self.frameSuperior = Frame(self.cad_funcionario, height=280, width=1365, bd=4, bg=co6, highlightbackground=co5, highlightthickness=6)
        self.frameSuperior.place(x=10, y=10, height=250, width=1075)

        self.frameInferior = Frame(self.cad_funcionario, height=280, width=1365, bd=4, bg=co6, highlightbackground=co5, highlightthickness=6)
        self.frameInferior.place(x=10, y=280, height=400, width=1075)

        self.framePessoa = Frame(self.frameInferior, bg=co10, highlightbackground=co5, highlightthickness=6)
        self.framePessoa.place(x=10, y=10, height=350, width=400)

        self.frameFuncionario = Frame(self.frameInferior, bg=co10, highlightbackground=co5, highlightthickness=6)
        self.frameFuncionario.place(x=430, y=10, height=350, width=610)

    def labelsFuncionario(self):
        self.l_id_funcionario = Label(self.frameSuperior, text="Código Usuário:", font=("Courier", 13, "italic", "bold"), bg=co6, fg=co10)
        self.l_id_funcionario.place(x=35, y=10)
        self.e_id_funcionario = Entry(self.frameSuperior, width=45, justify='left', relief='raised', bg=co0, fg=co10)
        self.e_id_funcionario.place(x=190, y=10)

        self.l_id_pessoa = Label(self.frameSuperior, text="Código Pessoa:", font=("Courier", 13, "italic", "bold"), bg=co6, fg=co10)
        self.l_id_pessoa.place(x=45, y=35)
        self.e_id_pessoa = Entry(self.frameSuperior, width=45, justify='left', relief='raised', bg=co0, fg=co10)
        self.e_id_pessoa.place(x=190, y=35)

        self.l_nome = Label(self.frameSuperior, text="Nome:", font=("Courier", 13, "italic", "bold"), bg=co6, fg=co10)
        self.l_nome.place(x=135, y=60)
        self.e_nome = Entry(self.frameSuperior, width=45, justify='left', relief='raised', bg=co0, fg=co10)
        self.e_nome.place(x=190, y=60)

        self.l_login = Label(self.frameSuperior, text="Login:", font=("Courier", 13, "italic", "bold"), bg=co6, fg=co10)
        self.l_login.place(x=125, y=85)
        self.e_login = Entry(self.frameSuperior, width=45, justify='left', relief='raised', bg=co0, fg=co10)
        self.e_login.place(x=190, y=85)

        self.l_senha = Label(self.frameSuperior, text="Senha:",font=("Courier", 13, "italic", "bold"), bg=co6, fg=co10)
        self.l_senha.place(x=125, y=110)
        self.e_senha = Entry(self.frameSuperior, width=45, show="*", justify='left', relief='raised', bg=co0, fg=co10)
        self.e_senha.place(x=190, y=110)

        self.l_confirmar_senha = Label(self.frameSuperior, text="Confirme a Senha:", font=("Courier", 13, "italic", "bold"), bg=co6, fg=co10)
        self.l_confirmar_senha.place(x=15, y=135)
        self.e_confirmar_senha = Entry(self.frameSuperior, width=45, show="*", justify='left', relief='raised', bg=co0, fg=co10)
        self.e_confirmar_senha.place(x=190, y=135)

    def botoesFuncionario(self):
        self.b_limpar = Button(self.frameSuperior, text="Limpar", command=self.limpaTela, width=10, font=("Courier", 13, "italic", "bold"), bg=co1, fg=co2, relief=RAISED, overrelief=RIDGE)
        self.b_limpar.place(x=380, y=185, height=40, width=100)

        self.b_procurarPessoa = Button(self.frameSuperior, text="Procurar\nPessoa", command=self.buscarPessoa, font=("Courier", 13, "italic", "bold"), bg=co1, fg=co2, relief=RAISED, overrelief=RIDGE)
        self.b_procurarPessoa.place(x=470, y=10, height=45, width=100)

        self.b_procurarFuncionario = Button(self.frameSuperior, text="Procurar",  command=self.buscarFuncionario, font=("Courier", 13, "italic", "bold"), bg=co1, fg=co2, relief=RAISED, overrelief=RIDGE)
        self.b_procurarFuncionario.place(x=490, y=185, height=40, width=100)

        self.b_adicionar = Button(self.frameSuperior, text="Adicionar", command=self.adicionaFuncionario, width=10, font=("Courier", 13, "italic", "bold"), bg=co7, fg=co2, relief=RAISED, overrelief=RIDGE)
        self.b_adicionar.place(x=600, y=185, height=40, width=100)

        self.b_alterar = Button(self.frameSuperior, text="Alterar", command=self.alteraFuncionario, font=("Courier", 13, "italic", "bold"), bg=co8, fg=co2, relief=RAISED, overrelief=RIDGE)
        self.b_alterar.place(x=710, y=185, height=40, width=100)

        self.b_excluir = Button(self.frameSuperior, text="Excluir", command=self.deletaFuncionario, font=("Courier", 13, "italic", "bold"), bg=co9, fg=co2, relief=RAISED, overrelief=RIDGE)
        self.b_excluir.place(x=820, y=185, height=40, width=100)

    def gridPessoas(self):
        self.listaPessoas = ttk.Treeview(self.framePessoa, columns=("col0", "col1"))
        self.listaPessoas.heading("#0", text="")
        self.listaPessoas.heading("#1", text="Código Pessoa")
        self.listaPessoas.heading("#2", text="Nome")

        self.listaPessoas.column("#0", anchor='center', width=2)
        self.listaPessoas.column("#1", anchor='center', width=100)
        self.listaPessoas.column("#2", anchor='center', width=270)

        self.listaPessoas.place(x=0, y=0, height=338, width=388)

    def gridFuncionario(self):
        self.listaFuncionario = ttk.Treeview(self.frameFuncionario, columns=("col0", "col1", "col2", "col3"))
        self.listaFuncionario.heading("#0", text="")
        self.listaFuncionario.heading("#1", text="Funcionário")
        self.listaFuncionario.heading("#2", text="Pessoa")
        self.listaFuncionario.heading("#3", text="Nome")
        self.listaFuncionario.heading("#4", text="Login")

        self.listaFuncionario.column("#0", anchor='center', width=2)
        self.listaFuncionario.column("#1", anchor='center', width=85)
        self.listaFuncionario.column("#2", anchor='center', width=70)
        self.listaFuncionario.column("#3", anchor='center', width=98)
        self.listaFuncionario.column("#4", anchor='center', width=98)

        self.listaFuncionario.place(x=0, y=0, height=338, width=598)

        self.barraVertical = ttk.Scrollbar(self.framePessoa, orient='vertical', command=self.listaFuncionario.yview)
        self.barraVertical.place(x=1048, y=0, height=369, width=15)

        self.barraHorizontal = ttk.Scrollbar(self.frameFuncionario, orient='horizontal', command=self.listaFuncionario.xview)
        self.barraHorizontal.place(x=0, y=354, height=15, width=1050)

        self.listaFuncionario.configure(yscrollcommand=self.barraVertical.set, xscrollcommand=self.barraHorizontal.set)

        self.listaPessoas.bind("<Double-1>", self.duploCliquePessoa)
        self.listaFuncionario.bind("<Double-1>", self.duploCliqueFuncionario)

AplicacaoUsuarios()

