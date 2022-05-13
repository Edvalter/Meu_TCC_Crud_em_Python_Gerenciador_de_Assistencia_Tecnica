
"""


"""
import os
import pickle
import sys
import view
import mysql.connector
from view import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import Calendar, DateEntry
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, a4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image




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

# - - Janela Relatórios - -

relatorios = Tk()

class Funcao():
    def limpa_tela(self):
        self.e_id_produto.delete(0, END)
        self.e_produto.delete(0, END)
        self.e_modelo.delete(0, END)
        self.e_marca.delete(0, END)
        self.e_cor.delete(0, END)
        self.e_produto.focus()

    def conecta_bd(self):
        self.conn = sqlite3.connect('gerenciador.db')
        self.cursor = self.conn.cursor()

    def desconecta_bd(self):
        self.conn.close()

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


class Aplicacao_relatorios(Funcao):
    def __init__(self):
        self.relatorios = relatorios
        self.tela_relatorios()
        self.frames_relatorios()
        self.abas()
        self.labels_entry()
        self.botoes()

        self.relatorios.mainloop()

    def tela_relatorios(self):
        self.relatorios.title("Relatórios")
        self.relatorios.config(bg=co3)
        self.relatorios.geometry("1095x680+263+0")

    def frames_relatorios(self):
        self.frame_superior = Frame(self.relatorios, bd=2, bg=co4, highlightbackground=co5, highlightthickness=6)
        self.frame_superior.place(x=10, y=10, height=670, width=1075)


    def abas(self):
        self.abas = ttk.Notebook(self.frame_superior)

        self.abaCliente = Frame(self.abas)
        self.abaCliente.config(bg=co3)
        self.abas.add(self.abaCliente, text="Clientes")

        self.abaProduto = Frame(self.abas)
        self.abaProduto.config(bg=co3)
        self.abas.add(self.abaProduto, text="Produtos")

        self.abaOrdemServico = Frame(self.abas)
        self.abaOrdemServico.config(bg=co3)
        self.abas.add(self.abaOrdemServico, text="Ordem de Serviço")

        self.abas.place(x=3, y=3, height=650, width=1055)

    def labels_entry(self):
        # - - - Aba Clientes - - -
        self.l_id_pessoas = Label(self.abaCliente, text="Código:", justify='right',
                                  font=("Courier", 13, "italic", "bold"), bg=co3, fg=co10)
        self.l_id_pessoas.place(x=50, y=10)
        self.e_id_pessoas = Entry(self.abaCliente, width=45, justify='left', relief='raised', bg=co2,
                                  fg=co10)
        self.e_id_pessoas.place(x=125, y=10)

        self.l_cpf = Label(self.abaCliente, text="Cpf:", font=("Courier", 13, "italic", "bold"), bg=co3,
                           fg=co10)
        self.l_cpf.place(x=555, y=10)
        self.e_cpf = Entry(self.abaCliente, width=45, justify='left', relief='raised', bg=co2, fg=co10)
        self.e_cpf.place(x=600, y=10)

        self.l_nome = Label(self.abaCliente, text="Nome:", font=("Courier", 13, "italic", "bold"), bg=co3,
                            fg=co10)
        self.l_nome.place(x=70, y=35)
        self.e_nome = Entry(self.abaCliente, width=45, justify='left', relief='raised', bg=co2, fg=co10)
        self.e_nome.place(x=125, y=35)

        self.l_telefone = Label(self.abaCliente, text="Telefone:", font=("Courier", 13, "italic", "bold"),
                                bg=co3, fg=co10)
        self.l_telefone.place(x=505, y=35)
        self.e_telefone = Entry(self.abaCliente, width=45, justify='left', relief='raised', bg=co2, fg=co10)
        self.e_telefone.place(x=600, y=35)

        self.l_whatsapp = Label(self.abaCliente, text="Whatsapp:", font=("Courier", 13, "italic", "bold"),
                                bg=co3, fg=co10)
        self.l_whatsapp.place(x=30, y=60)
        self.e_whatsapp = Entry(self.abaCliente, width=45, justify='left', relief='raised', bg=co2, fg=co10)
        self.e_whatsapp.place(x=125, y=60)

        self.l_email = Label(self.abaCliente, text="E-mail:", font=("Courier", 13, "italic", "bold"),
                             bg=co3, fg=co10)
        self.l_email.place(x=525, y=60)
        self.e_email = Entry(self.abaCliente, width=45, justify='left', relief='raised', bg=co2, fg=co10)
        self.e_email.place(x=600, y=60)

        self.l_cep = Label(self.abaCliente, text="Cep:", font=("Courier", 13, "italic", "bold"), bg=co3,
                           fg=co10)
        self.l_cep.place(x=85, y=85)
        self.e_cep = Entry(self.abaCliente, width=45, justify='left', relief='raised', bg=co2, fg=co10)
        self.e_cep.place(x=125, y=85)

        self.l_rua = Label(self.abaCliente, text="Rua:", font=("Courier", 13, "italic", "bold"), bg=co3,
                           fg=co10)
        self.l_rua.place(x=555, y=85)
        self.e_rua = Entry(self.abaCliente, width=45, justify='left', relief='raised', bg=co2, fg=co10)
        self.e_rua.place(x=600, y=85)

        self.l_numero = Label(self.abaCliente, text="Número:", font=("Courier", 13, "italic", "bold"),
                              bg=co3, fg=co10)
        self.l_numero.place(x=50, y=110)
        self.e_numero = Entry(self.abaCliente, width=45, justify='left', relief='raised', bg=co2, fg=co10)
        self.e_numero.place(x=125, y=110)

        self.l_bairro = Label(self.abaCliente, text="Bairro:", font=("Courier", 13, "italic", "bold"),
                              bg=co3, fg=co10)
        self.l_bairro.place(x=525, y=110)
        self.e_bairro = Entry(self.abaCliente, width=45, justify='left', relief='raised', bg=co2, fg=co10)
        self.e_bairro.place(x=600, y=110)

        self.l_cidade = Label(self.abaCliente, text="Cidade:", font=("Courier", 13, "italic", "bold"),
                              bg=co3, fg=co10)
        self.l_cidade.place(x=50, y=135)
        self.e_cidade = Entry(self.abaCliente, width=45, justify='left', relief='raised', bg=co2, fg=co10)
        self.e_cidade.place(x=125, y=135)

        self.l_estado = Label(self.abaCliente, text="Estado:", font=("Courier", 13, "italic", "bold"),
                              bg=co3, fg=co10)
        self.l_estado.place(x=525, y=135)
        self.e_estado = Entry(self.abaCliente, width=45, justify='left', relief='raised', bg=co2, fg=co10)
        self.e_estado.place(x=600, y=135)

        self.l_observacoes = Label(self.abaCliente, text="Observações:",
                                   font=("Courier", 13, "italic", "bold"), bg=co3, fg=co10)
        self.l_observacoes.place(x=0, y=160)
        self.e_observacoes = Entry(self.abaCliente, width=45, justify='left', relief='raised', bg=co2,
                                   fg=co10)
        self.e_observacoes.place(x=125, y=160)

        self.l_data = Label(self.abaCliente, text="Data de Cadastro:",
                            font=("Courier", 13, "italic", "bold"), bg=co3, fg=co10)
        self.l_data.place(x=425, y=160)
        self.e_data = Entry(self.abaCliente, width=45, justify='left', relief='raised', bg=co2, fg=co10)
        self.e_data.place(x=600, y=160)


        # - - - Aba Produto - - -
        self.l_id_produto = Label(self.abaProduto, text="Código:", font=("Courier", 13, "italic", "bold"), bg=co3, fg=co10)
        self.l_id_produto.place(x=15, y=10)
        self.e_id_produto = Entry(self.abaProduto, width=45, justify='left', relief='raised', bg=co2, fg=co10)
        self.e_id_produto.place(x=90, y=10)

        self.l_produto = Label(self.abaProduto, text="Produto:", font=("Courier", 13, "italic", "bold"), bg=co3, fg=co10)
        self.l_produto.place(x=5, y=35)
        self.e_produto = Entry(self.abaProduto, width=45, justify='left', relief='raised', bg=co2, fg=co10)
        self.e_produto.place(x=90, y=35)

        self.l_marca = Label(self.abaProduto, text="Marca:", font=("Courier", 13, "italic", "bold"), bg=co3, fg=co10)
        self.l_marca.place(x=25, y=60)
        self.e_marca = Entry(self.abaProduto, width=45, justify='left', relief='raised', bg=co2, fg=co10)
        self.e_marca.place(x=90, y=60)

        self.l_modelo = Label(self.abaProduto, text="Modelo:", font=("Courier", 13, "italic", "bold"), bg=co3, fg=co10)
        self.l_modelo.place(x=535, y=10)
        self.e_modelo = Entry(self.abaProduto, width=45, justify='left', relief='raised', bg=co2, fg=co10)
        self.e_modelo.place(x=610, y=10)

        self.l_cor = Label(self.abaProduto, text="Cor:", font=("Courier", 13, "italic", "bold"), bg=co3, fg=co10)
        self.l_cor.place(x=565, y=35)
        self.e_cor = Entry(self.abaProduto, width=45, justify='left', relief='raised', bg=co2, fg=co10)
        self.e_cor.place(x=610, y=35)

        self.l_estoque = Label(self.abaProduto, text="Estoque:", font=("Courier", 13, "italic", "bold"), bg=co3, fg=co10)
        self.l_estoque.place(x=525, y=60)
        self.e_estoque = Entry(self.abaProduto, width=45, justify='left', relief='raised', bg=co2, fg=co10)
        self.e_estoque.place(x=610, y=60)

    def botoes(self):
        # - - - Aba Clientes - - -
        self.b_limpar = Button(self.abaCliente, text="Limpar", command=self.limpa_tela, width=10, font=('Ivy 8 bold'),
                               bg=co6, fg=co2, relief=RAISED, overrelief=RIDGE)
        self.b_limpar.place(x=280, y=190, height=40, width=100)

        self.b_procurar = Button(self.abaCliente, text="Procurar", command=self.buscar_Produto, width=10,
                                 font=('Ivy 8 bold'), bg=co6, fg=co2, relief=RAISED, overrelief=RIDGE)
        self.b_procurar.place(x=390, y=190, height=40, width=100)

        self.b_imprimir = Button(self.abaCliente, text="Imprimir", width=10, font=('Ivy 8 bold'), bg=co7, fg=co2,
                                 relief=RAISED, overrelief=RIDGE)
        self.b_imprimir.place(x=500, y=190, height=40, width=100)


        # - - - Aba Produtos - - -
        self.b_limpar = Button(self.abaProduto, text="Limpar", command=self.limpa_tela, width=10, font=('Ivy 8 bold'), bg=co6, fg=co2, relief=RAISED, overrelief=RIDGE)
        self.b_limpar.place(x=280, y=130, height=40, width=100)

        self.b_procurar = Button(self.abaProduto, text="Procurar", command=self.buscar_Produto, width=10, font=('Ivy 8 bold'), bg=co6, fg=co2, relief=RAISED, overrelief=RIDGE)
        self.b_procurar.place(x=390, y=130, height=40, width=100)

        self.b_imprimir = Button(self.abaProduto, text="Imprimir",  width=10, font=('Ivy 8 bold'), bg=co7, fg=co2, relief=RAISED, overrelief=RIDGE)
        self.b_imprimir.place(x=500, y=130, height=40, width=100)



Aplicacao_relatorios()