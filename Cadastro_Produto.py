
"""
https://www.youtube.com/watch?v=Epz87iYfXtw

verificar a possibilidade de colocar um visualizador instantaneo de como fica preenchido os campos

fazer um IF para que se for procurado um protudo e não encontrar, informar na tela PRODUTO NÃO ENCONTRADO

    ver para fazer o confirmação ou cancelamento na hora de alterar/cadastrar um cliente
    messagebox.askquestion("ADICIONADO", " Os Dados Foram Acicionados")
    askyesno()

    class tkinter.messagebox.Message(master=None, **options)
    Cria uma caixa de mensagem padrão de informações.

    Caixa de mensagem de informação

    tkinter.messagebox.showinfo(title=None, message=None, **options)
    Caixas de mensagem de atenção

    tkinter.messagebox.showwarning(title=None, message=None, **options)
    tkinter.messagebox.showerror(title=None, message=None, **options)
    Caixas de mensagem de dúvida

    tkinter.messagebox.askquestion(title=None, message=None, **options)
    tkinter.messagebox.askokcancel(title=None, message=None, **options)
    tkinter.messagebox.askretrycancel(title=None, message=None, **options)
    tkinter.messagebox.askyesno(title=None, message=None, **options)
    tkinter.messagebox.askyesnocancel(title=None, message=None, **options)


"""
import os
import pickle
import sys
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from view import *
import view
import sqlite3

# Configuração das Cores

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

# - - janela Cadastro de Produtos - -

cad_produto = Tk()

class Funcao():
    def limpa_tela(self):
        self.e_id_produto.delete(0, END)
        self.e_produto.delete(0, END)
        self.e_modelo.delete(0, END)
        self.e_marca.delete(0, END)
        self.e_cor.delete(0, END)
        self.e_valor_compra.delete(0, END)
        self.e_valor_venda.delete(0, END)
        self.e_estoque.delete(0, END)
        self.e_produto.focus()

    def conecta_bd(self):
        self.conn = sqlite3.connect('gerenciador.db')
        self.cursor = self.conn.cursor()

    def desconecta_bd(self):
        self.conn.close()

    def montatabelas(self):
        self.conecta_bd()
        self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS cad_produto(
                id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
                produto VARCHAR(100) NOT NULL,
                marca VARCHAR(100) NOT NULL,
                modelo VARCHAR(100) NOT NULL,
                cor VARCHAR(100),
                valor_compra FLOAT,
                valor_venda FLOAT,
                estoque INTEGER
            );
        """)

        self.conn.commit();
        self.desconecta_bd()

    def produtos_Variaveis(self):
        self.id_produto = self.e_id_produto.get()
        self.produto = self.e_produto.get()
        self.marca = self.e_marca.get()
        self.modelo = self.e_modelo.get()
        self.cor = self.e_cor.get()
        self.valor_compra = self.e_valor_compra.get()
        self.valor_venda = self.e_valor_venda.get()
        self.estoque = self.e_estoque.get()

    def adiciona_Produto(self):
        self.produtos_Variaveis()
        if self.e_produto.get() == "":
            messagebox.showerror(title="Cadastro de Produto", message="Campos Vazios")
        else:
            self.conecta_bd()
            self.cursor.execute(
                """ INSERT INTO 
                    cad_produto (produto, marca, modelo, cor, valor_compra, valor_venda, estoque)
                VALUES 
                    (?, ?, ?, ?, ?, ?, ?);""", (
                     self.produto,
                     self.marca,
                     self.modelo,
                     self.cor,
                     self.valor_compra,
                     self.valor_venda,
                     self.estoque))

            messagebox.showinfo(title="Cadastrado de Produto", message="Produto Cadastro com Sucesso")
        self.conn.commit()
        self.desconecta_bd()
        self.select_Produto()
        self.limpa_tela()

    def select_Produto(self):
        self.listaproduto.delete(*self.listaproduto.get_children())
        self.conecta_bd()
        lista = self.cursor.execute("""
            SELECT * FROM 
                cad_produto 
            ORDER BY 
                marca 
            ASC; """)
        for i in lista:
            self.listaproduto.insert("", END, values=i)
        self.desconecta_bd()

    def duplo_Clique(self, event):
        self.limpa_tela()
        self.listaproduto.selection()

        for n in self.listaproduto.selection():
            col0, col1, col2, col3, col4, col5, col6, col7 = self.listaproduto.item(n, 'values')
            self.e_id_produto.insert(END, col0)
            self.e_produto.insert(END, col1)
            self.e_marca.insert(END, col2)
            self.e_modelo.insert(END, col3)
            self.e_cor.insert(END, col4)
            self.e_valor_compra.insert(END, col5)
            self.e_valor_venda.insert(END, col6)
            self.e_estoque.insert(END, col7)

    def deleta_Produto(self):
        self.produtos_Variaveis()
        self.conecta_bd()
        self.cursor.execute("""
            DELETE FROM 
                cad_produto 
            WHERE
                id_produto = ? """, (
                self.id_produto,))

        self.conn.commit()
        self.desconecta_bd()
        self.limpa_tela()
        self.select_Produto()

    def altera_Produto(self):
        self.produtos_Variaveis()
        self.conecta_bd()
        self.cursor.execute("""
            UPDATE 
                cad_produto
            SET 
                produto = ?, marca = ?, modelo = ?, cor = ?, valor_compra = ?, valor_venda = ?, estoque = ? 
            WHERE 
                id_produto = ?""", (
                self.produto,
                self.marca,
                self.modelo,
                self.cor,
                self.valor_compra,
                self.valor_venda,
                self.estoque,
                self.id_produto))

        self.conn.commit()
        self.desconecta_bd()
        self.select_Produto()
        self.limpa_tela()

    def buscar_Produto(self):
        self.conecta_bd()
        self.listaproduto.delete(*self.listaproduto.get_children())

        produto = self.e_produto.get()
        marca = self.e_marca.get()
        modelo = self.e_modelo.get()
        cor = self.e_cor.get()

        if len(produto) > 0:

            self.e_produto.insert(END, "%")
            produto = self.e_produto.get()
            self.cursor.execute("""
                SELECT * FROM 
                    cad_produto
                WHERE 
                    produto 
                LIKE '%s' ORDER BY produto ASC""" % produto, )

            buscaproduto = self.cursor.fetchall()

            for i in buscaproduto:
                self.listaproduto.insert("", END, values=i)

        elif len(marca) > 0:
            self.e_marca.insert(END, "%")
            marca = self.e_marca.get()
            self.cursor.execute("""
                SELECT * FROM 
                    cad_produto 
                WHERE 
                    marca 
                LIKE '%s' ORDER BY marca ASC""" % marca, )
            buscamarca = self.cursor.fetchall()

            for i in buscamarca:
                self.listaproduto.insert("", END, values=i)

        elif len(modelo) > 0:
            self.e_modelo.insert(END, "%")
            modelo = self.e_modelo.get()
            self.cursor.execute("""
                SELECT * FROM 
                    cad_produto 
                WHERE 
                    modelo 
                LIKE '%s' ORDER BY marca ASC""" % modelo, )
            buscamodelo = self.cursor.fetchall()

            for i in buscamodelo:
                self.listaproduto.insert("", END, values=i)

            self.limpa_tela()
            self.desconecta_bd()

        elif len(cor) > 0:
            self.e_cor.insert(END, "%")
            cor = self.e_cor.get()
            self.cursor.execute("""
                SELECT * FROM 
                    cad_produto 
                WHERE 
                    cor 
                LIKE '%s' ORDER BY cor ASC""" % cor, )
            buscacor = self.cursor.fetchall()

            for i in buscacor:
                self.listaproduto.insert("", END, values=i)

        self.limpa_tela()
        self.desconecta_bd()

class Aplicacao_Produto(Funcao):
    def __init__(self):
        self.cad_produto = cad_produto
        self.tela_cadastro_produto()
        self.frames_cad_produto()
        self.labels_entry()
        self.botoes()
        self.grid_produto()
        self.montatabelas()
        self.select_Produto()
        self.cad_produto.mainloop()

    def tela_cadastro_produto(self):
        self.cad_produto.title("Cadastro de Produto")
        self.cad_produto.config(bg=co3)
        self.cad_produto.geometry("1095x680+263+0")

    def frames_cad_produto(self):
        self.frame_superior = Frame(self.cad_produto, bd=4, bg=co4, highlightbackground=co5, highlightthickness=6)
        self.frame_superior.place(x=10, y=10, height=250, width=1075)

        self.frame_grid = Frame(self.cad_produto, height=418, width=1075, bg=co10, highlightbackground=co5, highlightthickness=6)
        self.frame_grid.place(x=10, y=280, height=380, width=1075)

    def labels_entry(self):
        self.l_id_produto = Label(self.frame_superior, text="Código:", font=("Courier", 13, "italic", "bold"), bg=co4, fg=co10)
        self.l_id_produto.place(x=15, y=10)
        self.e_id_produto = Entry(self.frame_superior, width=45, justify='left', relief='raised', bg=co2, fg=co10)
        self.e_id_produto.place(x=90, y=10)

        self.l_produto = Label(self.frame_superior, text="Produto:", font=("Courier", 13, "italic", "bold"), bg=co4, fg=co10)
        self.l_produto.place(x=5, y=35)
        self.e_produto = Entry(self.frame_superior, width=45, justify='left', relief='raised', bg=co2, fg=co10)
        self.e_produto.place(x=90, y=35)

        self.l_marca = Label(self.frame_superior, text="Marca:", font=("Courier", 13, "italic", "bold"), bg=co4, fg=co10)
        self.l_marca.place(x=25, y=60)
        self.e_marca = Entry(self.frame_superior, width=45, justify='left', relief='raised', bg=co2, fg=co10)
        self.e_marca.place(x=90, y=60)

        self.l_modelo = Label(self.frame_superior, text="Modelo:", font=("Courier", 13, "italic", "bold"), bg=co4, fg=co10)
        self.l_modelo.place(x=15, y=85)
        self.e_modelo = Entry(self.frame_superior, width=45, justify='left', relief='raised', bg=co2, fg=co10)
        self.e_modelo.place(x=90, y=85)

        self.l_valor_compra = Label(self.frame_superior, text="Valor de Compra:", font=("Courier", 13, "italic", "bold"), bg=co4, fg=co10)
        self.l_valor_compra.place(x=440, y=10)
        self.e_valor_compra = Entry(self.frame_superior, width=45, justify='left', relief='raised', bg=co2, fg=co10)
        self.e_valor_compra.place(x=610, y=10)

        self.l_valor_venda = Label(self.frame_superior, text="Valor de Venda:", font=("Courier", 13, "italic", "bold"), bg=co4, fg=co10)
        self.l_valor_venda.place(x=450, y=35)
        self.e_valor_venda = Entry(self.frame_superior, width=45, justify='left', relief='raised', bg=co2, fg=co10)
        self.e_valor_venda.place(x=610, y=35)

        self.l_cor = Label(self.frame_superior, text="Cor:", font=("Courier", 13, "italic", "bold"), bg=co4, fg=co10)
        self.l_cor.place(x=560, y=60)
        self.e_cor = Entry(self.frame_superior, width=45, justify='left', relief='raised', bg=co2, fg=co10)
        self.e_cor.place(x=610, y=60)

        self.l_estoque = Label(self.frame_superior, text="Estoque:", font=("Courier", 13, "italic", "bold"), bg=co4, fg=co10)
        self.l_estoque.place(x=520, y=85)
        self.e_estoque = Entry(self.frame_superior, width=45, justify='left', relief='raised', bg=co2, fg=co10)
        self.e_estoque.place(x=610, y=85)

    def botoes(self):
        self.b_limpar = Button(self.frame_superior, text="Limpar", command=self.limpa_tela, width=10, font=('Ivy 8 bold'), bg=co6, fg=co2, relief=RAISED, overrelief=RIDGE)
        self.b_limpar.place(x=280, y=130, height=40, width=100)

        self.b_procurar = Button(self.frame_superior, text="Procurar:", command=self.buscar_Produto, width=10, font=('Ivy 8 bold'), bg=co6, fg=co2, relief=RAISED, overrelief=RIDGE)
        self.b_procurar.place(x=390, y=130, height=40, width=100)

        self.b_adicionar = Button(self.frame_superior, text="Adicionar:", command=self.adiciona_Produto, width=10, font=('Ivy 8 bold'), bg=co7, fg=co2, relief=RAISED, overrelief=RIDGE)
        self.b_adicionar.place(x=500, y=130, height=40, width=100)

        self.b_alterar = Button(self.frame_superior, text="Alterar:", command=self.altera_Produto, width=10, font=('Ivy 8 bold'), bg=co8, fg=co2, relief=RAISED, overrelief=RIDGE)
        self.b_alterar.place(x=610, y=130, height=40, width=100)

        self.b_excluir = Button(self.frame_superior, text="Excluir:", command=self.deleta_Produto, width=10, font=('Ivy 8 bold'), bg=co9, fg=co2, relief=RAISED, overrelief=RIDGE)
        self.b_excluir.place(x=720, y=130, height=40, width=100)

    def grid_produto(self):
        self.listaproduto = ttk.Treeview(self.frame_grid, columns=("col0", "col1", "col2", "col3", "col4", "col5", "col6", "col7"))
        self.listaproduto.heading("#0", text="")
        self.listaproduto.heading("#1", text="Código")
        self.listaproduto.heading("#2", text="Produto")
        self.listaproduto.heading("#3", text="Marca")
        self.listaproduto.heading("#4", text="Modelo")
        self.listaproduto.heading("#5", text="Cor")
        self.listaproduto.heading("#6", text="Valor de Compra")
        self.listaproduto.heading("#7", text="Valor de Venda")
        self.listaproduto.heading("#8", text="Estoque")

        self.listaproduto.column("#0", anchor='center', width=5)
        self.listaproduto.column("#1", anchor='center', width=120)
        self.listaproduto.column("#2", anchor='center', width=174)
        self.listaproduto.column("#3", anchor='center', width=120)
        self.listaproduto.column("#4", anchor='center', width=120)
        self.listaproduto.column("#5", anchor='center', width=120)
        self.listaproduto.column("#6", anchor='center', width=120)
        self.listaproduto.column("#7", anchor='center', width=120)
        self.listaproduto.column("#8", anchor='center', width=120)

        self.listaproduto.place(x=10, y=10, height=340, width=1035)

        self.barra_vertical = ttk.Scrollbar(self.frame_grid, orient='vertical', command=self.listaproduto.yview)
        self.barra_vertical.place(x=1048, y=0, height=369, width=15)

        self.barra_horizontal = ttk.Scrollbar(self.frame_grid, orient='horizontal', command=self.listaproduto.xview)
        self.barra_horizontal.place(x=0, y=354, height=15, width=1050)

        self.listaproduto.configure(yscrollcommand=self.barra_vertical.set, xscrollcommand=self.barra_horizontal.set)

        self.listaproduto.bind("<Double-1>", self.duplo_Clique)

Aplicacao_Produto()