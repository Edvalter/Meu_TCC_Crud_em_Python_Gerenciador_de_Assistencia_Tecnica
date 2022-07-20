


import os
import pickle
import sys
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from view import *
import view
import mysql.connector
from mysql.connector import Error


# Configuração das Cores

co0 = "#f0f3f5"  # Preta
co1 = "#f0f3f5"  # cizenta / grey
co2 = "#403d3d"  # letra
co3 = "#333333"  # azul escuro / fundo da tela / fundo dos label
co4 = "#666666"  # roxo claro / fundo do frame
co5 = "#759fe6"  # cor da borda - highlightbackground
co6 = "#A8A8A8"  # em uso = cinza  fundo dos labels e do frame
co7 = "#6aabb5"  # Botão Adicionar
co8 = "#ffff99"  # Botão Alterar
co9 = "orange"  # em uso = laranja botão excluir
co10 = "Black" # em uso = cor da fonte
co11 = "white" # em uso no fundo do grid

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
        self.conn = mysql.connector.connect(host='localhost', database='gerenciador', user='root', password='admin')
        self.cursor = self.conn.cursor()

    def desconecta_bd(self):
        self.conn.close()

    def montatabelas(self):
        self.conecta_bd()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS produto(
                id_produto INTEGER AUTO_INCREMENT,
                produto VARCHAR(100) NOT NULL,
                marca VARCHAR(100) NOT NULL,
                modelo VARCHAR(100) NOT NULL,
                cor VARCHAR(100),
                valor_compra FLOAT,
                valor_venda FLOAT,
                estoque INTEGER,
            PRIMARY KEY (id_produto)
            );
        """)

        self.conn.commit()
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
            self.cursor.execute("""
                INSERT INTO
                    produto (
                        produto, 
                        marca, 
                        modelo, 
                        cor, 
                        valor_compra, 
                        valor_venda, 
                        estoque) 
                VALUES 
                        (%s, %s, %s, %s, %s, %s, %s);""", (
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
        lista = self.cursor.execute(""" SELECT * FROM produto ORDER BY id_produto ASC; """)
        lista = self.cursor.fetchall()

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
        self.cursor.execute(f"""
            DELETE FROM 
                produto 
            WHERE
                id_produto = %s """, (self.id_produto,))

        messagebox.showinfo(title="Cadastrado de Produto", message="Produto Excluído")

        self.conn.commit()
        self.desconecta_bd()
        self.limpa_tela()
        self.select_Produto()

    def altera_Produto(self):
        self.produtos_Variaveis()
        self.conecta_bd()
        self.cursor.execute("""
            UPDATE 
                produto
            SET 
                produto = %s, 
                marca = %s, 
                modelo = %s, 
                cor = %s, 
                valor_compra = %s, 
                valor_venda = %s, 
                estoque = %s 
            WHERE 
                id_produto = %s""", (
                self.produto,
                self.marca,
                self.modelo,
                self.cor,
                self.valor_compra,
                self.valor_venda,
                self.estoque,
                self.id_produto))

        messagebox.showinfo(title="Cadastrado de Produto", message="Produto Alterado")

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
        estoque = self.e_estoque.get()

        if len(produto) > 0 or len(marca) > 0 or len(modelo) > 0 or len(cor) > 0 or len(estoque) > 0:
            self.e_produto.insert(END, "")
            self.cursor.execute(f"""
                SELECT * FROM 
                    produto
                WHERE 
                    produto LIKE '%{produto}%' 
                AND marca LIKE '%{marca}%'
                AND modelo LIKE '%{modelo}%'
                AND cor LIKE '%{cor}%'
                AND estoque LIKE '{estoque}%'
                ORDER BY id_produto;""")

            buscaproduto = self.cursor.fetchall()

            for i in buscaproduto:
                self.listaproduto.insert("", END, values=i)

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
        self.cad_produto.geometry("1095x700+263+0")
        self.cad_produto.iconbitmap("C:/Users/Edinho/PycharmProjects/Meu_TCC/Logo/segatIcone.ico")

    def frames_cad_produto(self):
        self.frame_superior = Frame(self.cad_produto, bd=4, bg=co6, highlightbackground=co5, highlightthickness=6)
        self.frame_superior.place(x=10, y=10, height=250, width=1075)

        self.frame_grid = Frame(self.cad_produto, height=418, width=1075, bg=co11, highlightbackground=co5, highlightthickness=6)
        self.frame_grid.place(x=10, y=280, height=400, width=1075)

    def labels_entry(self):
        self.l_id_produto = Label(self.frame_superior, text="Código:", font=("Courier", 13, "italic", "bold"), bg=co6, fg=co10)
        self.l_id_produto.place(x=65, y=10)
        self.e_id_produto = Entry(self.frame_superior, width=45, justify='left', relief='raised', bg=co0, fg=co10)
        self.e_id_produto.place(x=140, y=10)

        self.l_produto = Label(self.frame_superior, text="Produto:", font=("Courier", 13, "italic", "bold"), bg=co6, fg=co10)
        self.l_produto.place(x=55, y=35)
        self.e_produto = Entry(self.frame_superior, width=45, justify='left', relief='raised', bg=co0, fg=co10)
        self.e_produto.place(x=140, y=35)

        self.l_marca = Label(self.frame_superior, text="Marca:", font=("Courier", 13, "italic", "bold"), bg=co6, fg=co10)
        self.l_marca.place(x=75, y=60)
        self.e_marca = Entry(self.frame_superior, width=45, justify='left', relief='raised', bg=co0, fg=co10)
        self.e_marca.place(x=140, y=60)

        self.l_modelo = Label(self.frame_superior, text="Modelo:", font=("Courier", 13, "italic", "bold"), bg=co6, fg=co10)
        self.l_modelo.place(x=65, y=85)
        self.e_modelo = Entry(self.frame_superior, width=45, justify='left', relief='raised', bg=co0, fg=co10)
        self.e_modelo.place(x=140, y=85)

        self.l_valor_compra = Label(self.frame_superior, text="Valor de Compra:", font=("Courier", 13, "italic", "bold"), bg=co6, fg=co10)
        self.l_valor_compra.place(x=485, y=10)
        self.e_valor_compra = Entry(self.frame_superior, width=45, justify='left', relief='raised', bg=co0, fg=co10)
        self.e_valor_compra.place(x=650, y=10)

        self.l_valor_venda = Label(self.frame_superior, text="Valor de Venda:", font=("Courier", 13, "italic", "bold"), bg=co6, fg=co10)
        self.l_valor_venda.place(x=495, y=35)
        self.e_valor_venda = Entry(self.frame_superior, width=45, justify='left', relief='raised', bg=co0, fg=co10)
        self.e_valor_venda.place(x=650, y=35)

        self.l_cor = Label(self.frame_superior, text="Cor:", font=("Courier", 13, "italic", "bold"), bg=co6, fg=co10)
        self.l_cor.place(x=605, y=60)
        self.e_cor = Entry(self.frame_superior, width=45, justify='left', relief='raised', bg=co0, fg=co10)
        self.e_cor.place(x=650, y=60)

        self.l_estoque = Label(self.frame_superior, text="Estoque:", font=("Courier", 13, "italic", "bold"), bg=co6, fg=co10)
        self.l_estoque.place(x=565, y=85)
        self.e_estoque = Entry(self.frame_superior, width=45, justify='left', relief='raised', bg=co0, fg=co10)
        self.e_estoque.place(x=650, y=85)

    def botoes(self):
        self.b_limpar = Button(self.frame_superior, text="Limpar", command=self.limpa_tela, font=("Courier", 13, "italic", "bold"), bg=co1, fg=co2, relief=RAISED, overrelief=RIDGE)
        self.b_limpar.place(x=380, y=150, height=40, width=100)

        self.b_procurar = Button(self.frame_superior, text="Procurar", command=self.buscar_Produto, font=("Courier", 13, "italic", "bold"), bg=co1, fg=co2, relief=RAISED, overrelief=RIDGE)
        self.b_procurar.place(x=490, y=150, height=40, width=100)

        self.b_adicionar = Button(self.frame_superior, text="Adicionar", command=self.adiciona_Produto, font=("Courier", 13, "italic", "bold"), bg=co7, fg=co2, relief=RAISED, overrelief=RIDGE)
        self.b_adicionar.place(x=600, y=150, height=40, width=100)

        self.b_alterar = Button(self.frame_superior, text="Alterar", command=self.altera_Produto, font=("Courier", 13, "italic", "bold"), bg=co8, fg=co2, relief=RAISED, overrelief=RIDGE)
        self.b_alterar.place(x=710, y=150, height=40, width=100)

        self.b_excluir = Button(self.frame_superior, text="Excluir", command=self.deleta_Produto, width=10, font=("Courier", 13, "italic", "bold"), bg=co9, fg=co2, relief=RAISED, overrelief=RIDGE)
        self.b_excluir.place(x=820, y=150, height=40, width=100)

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

        self.listaproduto.place(x=0, y=0, height=375, width=1055)

        self.barra_vertical = ttk.Scrollbar(self.frame_grid, orient='vertical', command=self.listaproduto.yview)
        self.barra_vertical.place(x=1050, y=0, height=388, width=15)

        self.barra_horizontal = ttk.Scrollbar(self.frame_grid, orient='horizontal', command=self.listaproduto.xview)
        self.barra_horizontal.place(x=0, y=373, height=15, width=1050)

        self.listaproduto.configure(yscrollcommand=self.barra_vertical.set, xscrollcommand=self.barra_horizontal.set)

        self.listaproduto.bind("<Double-1>", self.duplo_Clique)

Aplicacao_Produto()