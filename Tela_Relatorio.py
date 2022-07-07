


import os
import pickle
import sys
import mysql.connector
from tkinter import *
from tkinter import ttk

from datetime import datetime as dt
from tkcalendar import Calendar, DateEntry

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image
import webbrowser

import pandas as pd


database = "gerenciador.db"

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

# - - Janela Relatórios - -

relatorios = Tk()

class Relatorio():

    def imprimir(self):
        webbrowser.open("Lista de Clientes.pdf")# abre o arquivo pdf na pagina da internet

    def geraRelatorioClientes(self):
        self.conecta_bd()
        self.listaPessoas = self.cursor.execute(""" 
            SELECT 
                id_pessoa, nome, 
            DATE_FORMAT(data_cadastro, '%d/%m/%Y') 
                as data_cadastro  FROM pessoas; """) # converte a data  padrão americana para a padrão brasileira

        self.listaPessoas = self.cursor.fetchall()

        self.meuRelatorio = canvas.Canvas("Lista de Clientes.pdf") # imprime o cabeçalho
        self.meuRelatorio.setFont("Times-Bold", 18)
        self.meuRelatorio.drawString(50, 750, "Código")
        self.meuRelatorio.drawString(270, 750, "Nome")
        self.meuRelatorio.drawString(480, 750, "Data")

        self.meuRelatorio.setFont("Times-Bold", 13) # aqui imprimi as informações do dataframe
        y = 0
        for i in range(0, len(self.listaPessoas)):
            y = y + 15 # distância entre as linhas
            self.meuRelatorio.drawString(75, 750 - y, str(self.listaPessoas[i][0])) # 75, 270, 500 distância vertical
            self.meuRelatorio.drawString(270, 750 - y, str(self.listaPessoas[i][1])) # 750 distância horizontal
            self.meuRelatorio.drawString(470, 750 - y, str(self.listaPessoas[i][2]))

        self.meuRelatorio.save()
        self.imprimir()
        self.desconecta_bd()

class Funcao(Relatorio):
    def limpaTelaClientes(self):
        self.e_id_pessoa.delete(0, END)
        self.e_cpf.delete(0, END)
        self.e_nome.delete(0, END)
        self.e_telefone.delete(0, END)
        self.e_whatsapp.delete(0, END)
        self.e_email.delete(0, END)
        self.e_dataInicio.delete(0, END)
        self.e_dataFim.delete(0, END)

    def conecta_bd(self):
        self.conn = mysql.connector.connect(host='localhost', database='gerenciador', user='root', password='admin')
        self.cursor = self.conn.cursor()

    def desconecta_bd(self):
        self.conn.close()

    def entradaVariaveis(self):
        self.id_pessoa = self.e_id_pessoa.get()
        self.cpf= self.e_cpf.get()
        self.nome= self.e_nome.get()
        self.telefone= self.e_telefone.get()
        self.whatsapp= self.e_whatsapp.get()
        self.email= self.e_email.get()
        self.dataInicio= self.e_dataInicio.get()
        self.dataConvertidaInicial = self.converteDataInicial()
        self.dataFim= self.e_dataFim.get()
        self.dataConvertidaFinal = self.converteDataFinal()


    def converteDataInicial(self):
        if self.dataInicio != '':
            dataConvertidaInicial = dt.strptime(self.dataInicio, '%d/%m/%Y')
            return dataConvertidaInicial
        else:
            pass

    def converteDataFinal(self):
        if self.dataInicio != '':
            dataConvertidaFinal = dt.strptime(self.dataFim, '%d/%m/%Y')
            return dataConvertidaFinal
        else:
            pass


    def selecionaCliente(self):
        self.listapessoas.delete(*self.listapessoas.get_children())
        self.conecta_bd()
        listaPe = self.cursor.execute("""
             SELECT * FROM pessoas ORDER BY id_pessoa ASC; """)

        listaPe = self.cursor.fetchall()

        for i in listaPe:
            posicaoDaData = i[0:14] + (i[14].strftime('%d/%m/%Y'),)
            self.listapessoas.insert("", END, values=posicaoDaData)

        self.desconecta_bd()

    def procuraCliente(self):
        self.conecta_bd()
        self.listapessoas.delete(*self.listapessoas.get_children())

        id_pessoa = self.e_id_pessoa.get()
        cpf = self.e_cpf.get()
        nome = self.e_nome.get()
        telefone = self.e_telefone.get()
        whatsapp = self.e_whatsapp.get()
        email = self.e_email.get()
        dataInicio = self.e_dataInicio.get()
        dataFim = self.e_dataFim.get()

        if len(cpf) > 0:
            self.e_cpf.insert(END, "%")
            cpf = self.e_cpf.get()
            self.cursor.execute("""
                         SELECT * FROM  
                             pessoas 
                         WHERE 
                             cpf 
                         LIKE '%s' ORDER BY cpf ASC""" % cpf, )

            buscacpf = self.cursor.fetchall()

            for i in buscacpf:
                posicaoDaData = i[0:14] + (i[14].strftime('%d/%m/%Y'),)
                self.listapessoas.insert("", END, values=posicaoDaData)

        elif len(nome) > 0:
            self.e_nome.insert(END, "%")
            nome = self.e_nome.get()
            self.cursor.execute("""
                         SELECT * FROM 
                             pessoas
                         WHERE 
                             nome 
                         LIKE '%s' ORDER BY nome ASC""" % nome,)

            buscanome = self.cursor.fetchall()

            for i in buscanome:
                posicaoDaData = i[0:14] + (i[14].strftime('%d/%m/%Y'),)
                self.listapessoas.insert("", END, values=posicaoDaData)

        elif len(id_pessoa) > 0:
            self.e_id_pessoa.insert(END, "%")
            id_pessoa = self.e_id_pessoa.get()
            self.cursor.execute("""
                         SELECT * FROM 
                             pessoas 
                         WHERE 
                             id_pessoa 
                         LIKE '%s' ORDER BY id_pessoa ASC""" % id_pessoa,)

            buscaid_pessoas = self.cursor.fetchall()

            for i in buscaid_pessoas:
                posicaoDaData = i[0:14] + (i[14].strftime('%d/%m/%Y'),)
                self.listapessoas.insert("", END, values=i)

        elif len(telefone) > 0:
            self.e_telefone.insert(END, "%")
            telefone = self.e_telefone.get()
            self.cursor.execute("""
                         SELECT * FROM 
                             pessoas 
                         WHERE 
                             telefone 
                         LIKE '%s' ORDER BY telefone ASC""" % telefone,)

            buscatelefone = self.cursor.fetchall()

            for i in buscatelefone:
                posicaoDaData = i[0:14] + (i[14].strftime('%d/%m/%Y'),)
                self.listapessoas.insert("", END, values=posicaoDaData)

        elif len(whatsapp) > 0:
            self.e_whatsapp.insert(END, "%")
            whatsapp = self.e_whatsapp.get()
            self.cursor.execute("""
                         SELECT * FROM 
                             pessoas 
                         WHERE 
                             whatsapp 
                         LIKE '%s' ORDER BY whatsapp ASC""" % whatsapp,)

            buscawhatsapp = self.cursor.fetchall()

            for i in buscawhatsapp:
                posicaoDaData = i[0:14] + (i[14].strftime('%d/%m/%Y'),)
                self.listapessoas.insert("", END, values=posicaoDaData)

        elif len(email) > 0:
            self.e_email.insert(END, "%")
            email = self.e_email.get()
            self.cursor.execute("""
                         SELECT * FROM 
                             pessoas 
                         WHERE 
                             email 
                         LIKE '%s' ORDER BY email ASC""" % email,)
            buscaemail = self.cursor.fetchall()

            for i in buscaemail:
                posicaoDaData = i[0:14] + (i[14].strftime('%d/%m/%Y'),)
                self.listapessoas.insert("", END, values=posicaoDaData)

        elif len(dataInicio) > 0 or len(dataFim) > 0:
            self.e_dataInicio.insert(END, "")
            self.e_dataFim.insert(END, "")
            dataFim = self.e_dataFim.get()
            dataInicio = self.e_dataInicio.get()

            if dataFim == '':
                dataFim = '01/01/4001'
                dataFim = dt.strptime(dataFim, "%d/%m/%Y")
                dataFim = dt.strftime(dataFim, "%Y-%m-%d")
            else:
                dataFim = dt.strptime(dataFim, "%d/%m/%Y")
                dataFim = dt.strftime(dataFim, "%Y-%m-%d")

            if dataInicio == '':
                dataInicio = '01/01/1001'
                dataInicio = dt.strptime(dataInicio, "%d/%m/%Y")
                dataInicio = dt.strftime(dataInicio, "%Y-%m-%d")
            else:
                dataInicio = dt.strptime(dataInicio, "%d/%m/%Y")
                dataInicio = dt.strftime(dataInicio, "%Y-%m-%d")

            self.cursor.execute(f"""
                SELECT * FROM pessoas 
                WHERE data_cadastro BETWEEN 
                '{dataInicio}' AND '{dataFim}' ORDER BY data_cadastro ASC""")
            filtraDatas = self.cursor.fetchall()

            for i in filtraDatas:
                posicaoDaData = i[0:14] + (i[14].strftime('%d/%m/%Y'),)
                self.listapessoas.insert("", END, values=posicaoDaData)


class Aplicacao_Relatorios(Funcao, Relatorio):
    def __init__(self):
        self.relatorios = relatorios
        self.tela_Relatorios()
        self.abas()
        self.labelsEntryCliente()
        self.botoesCliente()
        self.botoesProduto()
        self.grid_Pessoas()
        self.grid_Produtos()
        self.selecionaCliente()

        self.relatorios.mainloop()

    def tela_Relatorios(self):
        self.relatorios.title("Relatórios")
        self.relatorios.config(bg=co3)
        self.relatorios.geometry("1095x700+263+0")

    def abas(self):
        self.abas = ttk.Notebook(self.relatorios)

        self.abaCliente = Frame(self.abas)
        self.abaCliente.config(bg=co6)
        self.abas.add(self.abaCliente, text="Clientes")

        self.abaProduto = Frame(self.relatorios)
        self.abaProduto.config(bg=co6)
        self.abas.add(self.abaProduto, text="Produtos")

        self.abaOrdemServico = Frame(self.relatorios)
        self.abaOrdemServico.config(bg=co6)
        self.abas.add(self.abaOrdemServico, text="Ordem de Serviço")

        self.abas.place(x=10, y=10, height=660, width=1075)

# - - - Aba Clientes - - -
    def labelsEntryCliente(self):
        self.l_id_pessoa = Label(self.abaCliente, text="Código:", justify='right',
                                  font=("Courier", 13, "italic", "bold"), bg=co6, fg=co10)
        self.l_id_pessoa.place(x=50, y=10)
        self.e_id_pessoa = Entry(self.abaCliente, width=45, justify='left', relief='raised', bg=co0, fg=co10)
        self.e_id_pessoa.place(x=125, y=10)

        self.l_cpf = Label(self.abaCliente, text="CPF:", font=("Courier", 13, "italic", "bold"), bg=co6, fg=co10)
        self.l_cpf.place(x=80, y=35)
        self.e_cpf = Entry(self.abaCliente, width=45, justify='left', relief='raised', bg=co0, fg=co10)
        self.e_cpf.place(x=125, y=35)

        self.l_nome = Label(self.abaCliente, text="Nome:", font=("Courier", 13, "italic", "bold"), bg=co6, fg=co10)
        self.l_nome.place(x=70, y=60)
        self.e_nome = Entry(self.abaCliente, width=45, justify='left', relief='raised', bg=co0, fg=co10)
        self.e_nome.place(x=125, y=60)

        self.l_telefone = Label(self.abaCliente, text="Telefone:", font=("Courier", 13, "italic", "bold"), bg=co6, fg=co10)
        self.l_telefone.place(x=30, y=85)
        self.e_telefone = Entry(self.abaCliente, width=45, justify='left', relief='raised', bg=co0, fg=co10)
        self.e_telefone.place(x=125, y=85)

        self.l_whatsapp = Label(self.abaCliente, text="Whatsapp:", font=("Courier", 13, "italic", "bold"), bg=co6, fg=co10)
        self.l_whatsapp.place(x=30, y=110)
        self.e_whatsapp = Entry(self.abaCliente, width=45, justify='left', relief='raised', bg=co0, fg=co10)
        self.e_whatsapp.place(x=125, y=110)

        self.l_email = Label(self.abaCliente, text="E-mail:", font=("Courier", 13, "italic", "bold"), bg=co6, fg=co10)
        self.l_email.place(x=50, y=135)
        self.e_email = Entry(self.abaCliente, width=45, justify='left', relief='raised', bg=co0, fg=co10)
        self.e_email.place(x=125, y=135)

        self.l_dataInicio = Label(self.abaCliente, text="Inicio:", font=("Courier", 13, "italic", "bold"), bg=co6, fg=co10)
        self.l_dataInicio.place(x=525, y=10)
        self.e_dataInicio = Entry(self.abaCliente, width=45, justify='left', relief='raised', bg=co0, fg=co10)
        self.e_dataInicio.place(x=600, y=10)

        self.l_dataFim = Label(self.abaCliente, text="Fim:", font=("Courier", 13, "italic", "bold"), bg=co6, fg=co10)
        self.l_dataFim.place(x=555, y=35)
        self.e_dataFim = Entry(self.abaCliente, width=45, justify='left', relief='raised', bg=co0, fg=co10)
        self.e_dataFim.place(x=600, y=35)

# - - - Botões Clientes - - -
    def botoesCliente(self):
        self.b_limpar = Button(self.abaCliente, command=self.limpaTelaClientes, text="Limpar",
                               font=("Courier", 13, "italic", "bold"), bg=co1, fg=co2, relief=RAISED, overrelief=RIDGE)
        self.b_limpar.place(x=480, y=115, height=40, width=100)

        self.b_procurar = Button(self.abaCliente, command=self.procuraCliente, text="Procurar",
                                 font=("Courier", 13, "italic", "bold"), bg=co1, fg=co2, relief=RAISED, overrelief=RIDGE)
        self.b_procurar.place(x=590, y=115, height=40, width=100)

        self.b_imprimir = Button(self.abaCliente, command=self.geraRelatorioClientes, text="Imprimir", width=10, font=("Courier", 13, "italic", "bold"),
                                 bg=co1, fg=co2, relief=RAISED, overrelief=RIDGE)
        self.b_imprimir.place(x=700, y=115, height=40, width=100)

# - - - Grid Clientes - - -
    def grid_Pessoas(self):
        self.listapessoas = ttk.Treeview(self.abaCliente, columns=("col0", "col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8", "col9", "col10", "col11", "col12", "col13", "col14"""))
        self.listapessoas.heading("#0", text="")
        self.listapessoas.heading("#1", text="Código")
        self.listapessoas.heading("#2", text="CPF")
        self.listapessoas.heading("#3", text="Nome")
        self.listapessoas.heading("#4", text="Telefone")
        self.listapessoas.heading("#5", text="WhatsApp")
        self.listapessoas.heading("#6", text="E-Mail")
        self.listapessoas.heading("#7", text="CEP")
        self.listapessoas.heading("#8", text="Rua")
        self.listapessoas.heading("#9", text="Número")
        self.listapessoas.heading("#10", text="Bairro")
        self.listapessoas.heading("#11", text="Cidade")
        self.listapessoas.heading("#12", text="Estado")
        self.listapessoas.heading("#13", text="Observações")
        self.listapessoas.heading("#14", text="Status")
        self.listapessoas.heading("#15", text="Data Cadastro")

        self.listapessoas.column("#0", anchor='center', width=2)
        self.listapessoas.column("#1", anchor='center', width=50)
        self.listapessoas.column("#2", anchor='center', width=75)
        self.listapessoas.column("#3", anchor='center',  width=100)
        self.listapessoas.column("#4", anchor='center',  width=100)
        self.listapessoas.column("#5", anchor='center', width=100)
        self.listapessoas.column("#6", anchor='center', width=130)
        self.listapessoas.column("#7", anchor='center',  width=65)
        self.listapessoas.column("#8", anchor='center',  width=100)
        self.listapessoas.column("#9", anchor='center',  width=65)
        self.listapessoas.column("#10", anchor='center',  width=65)
        self.listapessoas.column("#11", anchor='center',  width=65)
        self.listapessoas.column("#12", anchor='center',  width=55)
        self.listapessoas.column("#13", anchor='center',  width=100)
        self.listapessoas.column("#14", anchor='center', width=65)
        self.listapessoas.column("#15", anchor='center', width=100)

        self.listapessoas.place(x=10, y=200, height=400, width=1035)

        self.barra_vertical = ttk.Scrollbar(self.abaCliente, orient='vertical', command=self.listapessoas.yview)
        self.barra_vertical.place(x=1044, y=201, height=398, width=15)

        self.barra_horizontal = ttk.Scrollbar(self.abaCliente, orient='horizontal', command=self.listapessoas.xview)
        self.barra_horizontal.place(x=10, y=598, height=15, width=1050)

        self.listapessoas.configure(yscrollcommand=self.barra_vertical.set, xscrollcommand=self.barra_horizontal.set)

# - - - Aba Produto - - -
        self.l_id_produto = Label(self.abaProduto, text="Código:", font=("Courier", 13, "italic", "bold"), bg=co6, fg=co10)
        self.l_id_produto.place(x=50, y=10)
        self.e_id_produto = Entry(self.abaProduto, width=45, justify='left', relief='raised', bg=co0, fg=co10)
        self.e_id_produto.place(x=125, y=10)

        self.l_produto = Label(self.abaProduto, text="Produto:", font=("Courier", 13, "italic", "bold"), bg=co6, fg=co10)
        self.l_produto.place(x=40, y=35)
        self.e_produto = Entry(self.abaProduto, width=45, justify='left', relief='raised', bg=co0, fg=co10)
        self.e_produto.place(x=125, y=35)

        self.l_marca = Label(self.abaProduto, text="Marca:", font=("Courier", 13, "italic", "bold"), bg=co6, fg=co10)
        self.l_marca.place(x=60, y=60)
        self.e_marca = Entry(self.abaProduto, width=45, justify='left', relief='raised', bg=co0, fg=co10)
        self.e_marca.place(x=125, y=60)

        self.l_modelo = Label(self.abaProduto, text="Modelo:", font=("Courier", 13, "italic", "bold"), bg=co6, fg=co10)
        self.l_modelo.place(x=50, y=85)
        self.e_modelo = Entry(self.abaProduto, width=45, justify='left', relief='raised', bg=co0, fg=co10)
        self.e_modelo.place(x=125, y=85)

        self.l_cor = Label(self.abaProduto, text="Cor:", font=("Courier", 13, "italic", "bold"), bg=co6, fg=co10)
        self.l_cor.place(x=80, y=110)
        self.e_cor = Entry(self.abaProduto, width=45, justify='left', relief='raised', bg=co0, fg=co10)
        self.e_cor.place(x=125, y=110)

        self.l_estoque = Label(self.abaProduto, text="Estoque:", font=("Courier", 13, "italic", "bold"), bg=co6, fg=co10)
        self.l_estoque.place(x=40, y=135)
        self.e_estoque = Entry(self.abaProduto, width=45, justify='left', relief='raised', bg=co0, fg=co10)
        self.e_estoque.place(x=125, y=135)

# - - - Grid Produtos - - -
    def grid_Produtos(self):
        self.listaproduto = ttk.Treeview(self.abaProduto, columns=("col0", "col1", "col2", "col3", "col4", "col5", "col6",))
        self.listaproduto.heading("#0", text="")
        self.listaproduto.heading("#1", text="Código")
        self.listaproduto.heading("#2", text="Produto")
        self.listaproduto.heading("#3", text="Marca")
        self.listaproduto.heading("#4", text="Modelo")
        self.listaproduto.heading("#5", text="Cor")
        self.listaproduto.heading("#6", text="Estoque")

        self.listaproduto.column("#0", anchor='center', width=1)
        self.listaproduto.column("#1", anchor='center', width=174)
        self.listaproduto.column("#2", anchor='center', width=174)
        self.listaproduto.column("#3", anchor='center',  width=174)
        self.listaproduto.column("#4", anchor='center',  width=174)
        self.listaproduto.column("#5", anchor='center', width=174)
        self.listaproduto.column("#6", anchor='center', width=174)

        self.listaproduto.place(x=10, y=200, height=400, width=1037)

        self.barra_vertical = ttk.Scrollbar(self.abaProduto, orient='vertical', command=self.listaproduto.yview)
        self.barra_vertical.place(x=1045, y=201, height=398, width=15)

        self.barra_horizontal = ttk.Scrollbar(self.abaProduto, orient='horizontal', command=self.listaproduto.xview)
        self.barra_horizontal.place(x=10, y=598, height=15, width=1050)

        self.listaproduto.configure(yscrollcommand=self.barra_vertical.set, xscrollcommand=self.barra_horizontal.set)

# - - - Botões Produtos - - -
    def botoesProduto(self):
        self.b_limpar = Button(self.abaProduto, text="Limpar", width=10, font=("Courier", 13, "italic", "bold"),
                               bg=co1, fg=co2, relief=RAISED, overrelief=RIDGE)
        self.b_limpar.place(x=480, y=115, height=40, width=100)

        self.b_procurar = Button(self.abaProduto, text="Procurar", font=("Courier", 13, "italic", "bold"),
                                 bg=co1, fg=co2, relief=RAISED, overrelief=RIDGE)
        self.b_procurar.place(x=590, y=115, height=40, width=100)

        self.b_imprimir = Button(self.abaProduto, text="Imprimir", width=10, font=("Courier", 13, "italic", "bold"),
                                 bg=co1, fg=co2, relief=RAISED, overrelief=RIDGE)
        self.b_imprimir.place(x=700, y=115, height=40, width=100)


Aplicacao_Relatorios()

