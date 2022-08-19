


import os
import pickle
import sys
import mysql.connector
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox

from datetime import datetime as dt
from tkcalendar import Calendar, DateEntry

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image
import webbrowser


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

relatorio = Tk()


class Conexao():
    def conecta_bd(self):
        self.conn = mysql.connector.connect(host='localhost', database='gerenciador', user='root', password='admin')
        self.cursor = self.conn.cursor()

    def desconecta_bd(self):
        self.conn.close()

class RelatorioClientes(Conexao):
    # - -Pessoas - - - - - - -
    def imprimirClientes(self):
        webbrowser.open("Lista de Clientes.pdf")

    def geraRelatorioClientes(self):
        self.conecta_bd()
        self.listaPessoas = self.cursor.execute(""" 
            SELECT id_pessoa, nome, 
            DATE_FORMAT(data_cadastro, '%d/%m/%Y') 
                as data_cadastro  FROM pessoas; """)

        self.listaPessoas = self.cursor.fetchall()

        self.relatorioListaCliente = canvas.Canvas("Lista de Clientes.pdf", pagesize=A4)  # abre o relatório os
        self.relatorioListaCliente.drawImage("C:/Users/Edinho/PycharmProjects/Meu_TCC/Logo/LogoE.png", x=30, y=720,
                                             width=100, height=130)  # imprime a logo no relatório

        # - - Meu Cabeçalho - - - -
        self.relatorioListaCliente.setFont("Helvetica", 10)
        self.relatorioListaCliente.drawString(150, 810, 'Segat - Sistema Gerenciador de assistência Técnica')
        self.relatorioListaCliente.drawString(150, 795, 'Endereço: R: Quênia 94')
        self.relatorioListaCliente.drawString(150, 780, 'Centro - Timbó - SC')
        self.relatorioListaCliente.drawString(150, 765, 'CNPJ: 12.123.12.0001/23')
        self.relatorioListaCliente.drawString(150, 750, 'Telefone / WhatsApp: (47) 9 9247 9998')

        # - - Titulo do Relatório- - - -
        self.relatorioListaCliente.setFont("Helvetica-Bold", 15)
        self.relatorioListaCliente.drawString(240, 720, 'Lista de Clientes')


        self.relatorioListaCliente.setFont("Helvetica-Bold", 12)
        self.relatorioListaCliente.drawString(50, 700, "Código")
        self.relatorioListaCliente.drawString(270, 700, "Nome")
        self.relatorioListaCliente.drawString(480, 700, "Data")

        self.relatorioListaCliente.setFont("Helvetica", 10)
        y = 0
        for i in range(0, len(self.listaPessoas)):
            y = y + 15
            self.relatorioListaCliente.drawString(75, 700 - y, str(self.listaPessoas[i][0]))
            self.relatorioListaCliente.drawString(270, 700 - y, str(self.listaPessoas[i][1]))
            self.relatorioListaCliente.drawString(470, 700 - y, str(self.listaPessoas[i][2]))

        self.relatorioListaCliente.save()
        self.imprimirClientes()
        self.desconecta_bd()

# - - - Relatório de Produtos
class RelatorioProdutos(Conexao):
    def imprimirProdutos(self):
        webbrowser.open("Lista de Produtos.pdf")

    def geraRelatorioProdutos(self):
        self.conecta_bd()
        self.listaproduto = self.cursor.execute(""" 
            SELECT id_produto, produto, marca, modelo, cor, estoque FROM produto; """)

        self.listaproduto = self.cursor.fetchall()

        self.relatorioListaProduto = canvas.Canvas("Lista de Produtos.pdf", pagesize=A4)  # abre o relatório os
        self.relatorioListaProduto.drawImage("C:/Users/Edinho/PycharmProjects/Meu_TCC/Logo/LogoE.png", x=30, y=720,
                                             width=100, height=130)  # imprime a logo no relatório

        # - - Meu Cabeçalho - - - -
        self.relatorioListaProduto.setFont("Helvetica", 10)
        self.relatorioListaProduto.drawString(150, 810, 'Segat - Sistema Gerenciador de assistência Técnica')
        self.relatorioListaProduto.drawString(150, 795, 'Endereço: R: Quênia 94')
        self.relatorioListaProduto.drawString(150, 780, 'Centro - Timbó - SC')
        self.relatorioListaProduto.drawString(150, 765, 'CNPJ: 12.123.12.0001/23')
        self.relatorioListaProduto.drawString(150, 750, 'Telefone / WhatsApp: (47) 9 9247 9998')

        # - - Titulo do Relatório- - - -
        self.relatorioListaProduto.setFont("Helvetica-Bold", 15)
        self.relatorioListaProduto.drawString(240, 720, 'Lista de Produtos')


        self.relatorioListaProduto.setFont("Helvetica-Bold", 12)
        self.relatorioListaProduto.drawString(50, 700, "Id")
        self.relatorioListaProduto.drawString(100, 700, "Produto")
        self.relatorioListaProduto.drawString(225, 700, "Marca")
        self.relatorioListaProduto.drawString(300, 700, "Modelo")
        self.relatorioListaProduto.drawString(450, 700, "Cor")
        self.relatorioListaProduto.drawString(500, 700, "Estoque")

        self.relatorioListaProduto.setFont("Helvetica", 10)
        y = 0
        for i in range(0, len(self.listaproduto)):
            y = y + 15
            self.relatorioListaProduto.drawString(50, 700 - y, str(self.listaproduto[i][0]))
            self.relatorioListaProduto.drawString(100, 700 - y, str(self.listaproduto[i][1]))
            self.relatorioListaProduto.drawString(225, 700 - y, str(self.listaproduto[i][2]))
            self.relatorioListaProduto.drawString(300, 700 - y, str(self.listaproduto[i][3]))
            self.relatorioListaProduto.drawString(450, 700 - y, str(self.listaproduto[i][4]))
            self.relatorioListaProduto.drawString(525, 700 - y, str(self.listaproduto[i][5]))

        self.relatorioListaProduto.save()
        self.imprimirProdutos()
        self.desconecta_bd()


class RelatorioOrcamentos(Conexao):
    def imprimirOrcamento(self):
        webbrowser.open("Orçamentos.pdf")

    def geraRelatorioOrcamento(self):
        self.conecta_bd()
        self.listaOrcamento = self.cursor.execute(f""" 
            SELECT PRODUTO_ORC.ID_ORCAMENTO
			, PRODUTO_ORC.STATUS_ORCAMENTO
            , PESSOA.ID_PESSOA
            , PESSOA.NOME
            , PRODUTO_ORC.QUANTIDADE
            , PRODUTO.PRODUTO
            , PRODUTO.MODELO
            , PRODUTO_ORC.VALOR_VENDA
            , DATE_FORMAT(data_entrada, '%d/%m/%Y') as data_entrada 
            FROM PRODUTO_ORCADO PRODUTO_ORC
            INNER JOIN PESSOAS PESSOA ON PESSOA.ID_PESSOA = PRODUTO_ORC.ID_PESSOA
            INNER JOIN PRODUTO PRODUTO ON PRODUTO.ID_PRODUTO = PRODUTO_ORC.ID_PRODUTO
            INNER JOIN ORCAMENTO ORC ON ORC.ID_ORCAMENTO = PRODUTO_ORC.ID_ORCAMENTO; """)

        self.listaOrcamento = self.cursor.fetchall()

        self.relatorioListaOrcamento = canvas.Canvas("Orçamentos.pdf", pagesize=A4)  # abre o relatório os
        self.relatorioListaOrcamento.drawImage("C:/Users/Edinho/PycharmProjects/Meu_TCC/Logo/LogoE.png", x=30, y=720,
                                             width=100, height=130)  # imprime a logo no relatório

        # - - Meu Cabeçalho - - - -
        self.relatorioListaOrcamento.setFont("Helvetica", 10)
        self.relatorioListaOrcamento.drawString(150, 810, 'Segat - Sistema Gerenciador de assistência Técnica')
        self.relatorioListaOrcamento.drawString(150, 795, 'Endereço: R: Quênia 94')
        self.relatorioListaOrcamento.drawString(150, 780, 'Centro - Timbó - SC')
        self.relatorioListaOrcamento.drawString(150, 765, 'CNPJ: 12.123.12.0001/23')
        self.relatorioListaOrcamento.drawString(150, 750, 'Telefone / WhatsApp: (47) 9 9247 9998')

        # - - Titulo do Relatório- - - -
        self.relatorioListaOrcamento.setFont("Helvetica-Bold", 15)
        self.relatorioListaOrcamento.drawString(240, 720, 'Orçamentos')


        self.relatorioListaOrcamento.setFont("Helvetica-Bold", 9)
        self.relatorioListaOrcamento.drawString(40, 700, "OS")
        self.relatorioListaOrcamento.drawString(65, 700, "Status")
        self.relatorioListaOrcamento.drawString(130, 700, "Cliente")
        self.relatorioListaOrcamento.drawString(250, 700, "Qtdade")
        self.relatorioListaOrcamento.drawString(300, 700, "Produto")
        self.relatorioListaOrcamento.drawString(380, 700, "Modelo")
        self.relatorioListaOrcamento.drawString(460, 700, "Valor")
        self.relatorioListaOrcamento.drawString(520, 700, "Data Entrada")


        self.relatorioListaOrcamento.setFont("Helvetica", 9)
        y = 0
        for i in range(0, len(self.listaOrcamento)):
            y = y + 15
            self.relatorioListaOrcamento.drawString(45, 700 - y, str(self.listaOrcamento[i][0]))
            self.relatorioListaOrcamento.drawString(65, 700 - y, str(self.listaOrcamento[i][1]))
            self.relatorioListaOrcamento.drawString(130, 700 - y, str(self.listaOrcamento[i][2]))
            self.relatorioListaOrcamento.drawString(150, 700 - y, str(self.listaOrcamento[i][3]))
            self.relatorioListaOrcamento.drawString(260, 700 - y, str(self.listaOrcamento[i][4]))
            self.relatorioListaOrcamento.drawString(300, 700 - y, str(self.listaOrcamento[i][5]))
            self.relatorioListaOrcamento.drawString(380, 700 - y, str(self.listaOrcamento[i][6]))
            self.relatorioListaOrcamento.drawString(460, 700 - y, str(self.listaOrcamento[i][7]))
            self.relatorioListaOrcamento.drawString(510, 700 - y, str(self.listaOrcamento[i][8]))

        self.relatorioListaOrcamento.save()
        self.imprimirOrcamento()
        self.desconecta_bd()


# - - - Pessoas - - - - - -
class Pessoas(RelatorioClientes, Conexao):
    def limpaTelaClientes(self):
        self.e_id_pessoa.delete(0, END)
        self.e_cpf.delete(0, END)
        self.e_nome.delete(0, END)
        self.e_telefone.delete(0, END)
        self.e_whatsapp.delete(0, END)
        self.e_email.delete(0, END)
        self.e_dataInicioCliente.delete(0, END)
        self.e_dataFimCliente.delete(0, END)

    def entradaVariaveis(self):
        self.id_pessoa = self.e_id_pessoa.get()
        self.cpf= self.e_cpf.get()
        self.nome= self.e_nome.get()
        self.telefone= self.e_telefone.get()
        self.whatsapp= self.e_whatsapp.get()
        self.email= self.e_email.get()
        self.dataInicioCliente= self.e_dataInicioCliente.get()
        self.dataConvertidaInicial = self.converteDataInicial()
        self.dataFimCliente= self.e_dataFimCliente.get()
        self.dataConvertidaFinal = self.converteDataFinal()


    def converteDataInicial(self):
        if self.dataInicioCliente != '':
            dataConvertidaInicial = dt.strptime(self.dataInicioCliente, '%d/%m/%Y')
            return dataConvertidaInicial
        else:
            pass

    def converteDataFinal(self):
        if self.dataFimCliente != '':
            dataConvertidaFinal = dt.strptime(self.dataFimCliente, '%d/%m/%Y')
            return dataConvertidaFinal
        else:
            pass


    def selecionaCliente(self):
        self.listapessoas.delete(*self.listapessoas.get_children())
        self.conecta_bd()
        listaPe = self.cursor.execute(f"""
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
        dataInicioCliente = self.e_dataInicioCliente.get()
        dataFimCliente = self.e_dataFimCliente.get()

        if len(id_pessoa) > 0 or len(cpf) > 0 or len(nome) > 0 or len(telefone) > 0 or len(whatsapp) > 0 or len(email) > 0 or len(dataInicioCliente) > 0 or len(dataFimCliente) > 0:
            self.e_dataInicioCliente.insert(END, "")
            self.e_dataFimCliente.insert(END, "")

            if dataFimCliente == '':
                dataFimCliente = '01/01/4001'
                dataFimCliente = dt.strptime(dataFimCliente, "%d/%m/%Y")
                dataFimCliente = dt.strftime(dataFimCliente, "%Y-%m-%d")
            else:
                dataFimCliente = dt.strptime(dataFimCliente, "%d/%m/%Y")
                dataFimCliente = dt.strftime(dataFimCliente, "%Y-%m-%d")

            if dataInicioCliente == '':
                dataInicioCliente = '01/01/1001'
                dataInicioCliente = dt.strptime(dataInicioCliente, "%d/%m/%Y")
                dataInicioCliente = dt.strftime(dataInicioCliente, "%Y-%m-%d")
            else:
                dataInicioCliente = dt.strptime(dataInicioCliente, "%d/%m/%Y")
                dataInicioCliente = dt.strftime(dataInicioCliente, "%Y-%m-%d")

            self.cursor.execute(f"""
                     SELECT * FROM  
                         pessoas 
                     WHERE 
                         cpf LIKE '%{cpf}%'
                        AND nome LIKE '%{nome}%' 
                        AND telefone LIKE '%{telefone}%'
                        AND whatsapp LIKE '%{whatsapp}%'
                        AND email LIKE '%{email}%'
                        AND data_cadastro BETWEEN '{dataInicioCliente}' AND '{dataFimCliente}' ; """)

            buscaCliente = self.cursor.fetchall()

            for i in buscaCliente:
                posicaoDaData = i[0:14] + (i[14].strftime('%d/%m/%Y'),)
                self.listapessoas.insert("", END, values=posicaoDaData)

        self.desconecta_bd()

# - - - Produtos - - - - - -
class Produtos(RelatorioProdutos, Conexao):
    def limpaTelaProdutos(self):
        self.e_id_produto.delete(0, END)
        self.e_produto.delete(0, END)
        self.e_modelo.delete(0, END)
        self.e_marca.delete(0, END)
        self.e_cor.delete(0, END)
        self.e_estoque.delete(0, END)
        self.e_produto.focus()

    def produtos_Variaveis(self):
        self.id_produto = self.e_id_produto.get()
        self.produto = self.e_produto.get()
        self.marca = self.e_marca.get()
        self.modelo = self.e_modelo.get()
        self.cor = self.e_cor.get()
        self.estoque = self.e_estoque.get()


    def selecionaProduto(self):
        self.conecta_bd()
        self.listaproduto.delete(*self.listaproduto.get_children())
        lista = self.cursor.execute(f"""
            SELECT 
                id_produto, produto, marca, modelo, cor, estoque  
            FROM 
                produto 
            ORDER BY 
                id_produto 
            ASC; """)

        lista = self.cursor.fetchall()

        for i in lista:
            self.listaproduto.insert("", END, values=i)

        self.desconecta_bd()

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
                SELECT id_produto, produto, marca, modelo, cor, estoque FROM 
                    produto
                WHERE 
                    produto 
                LIKE '%{produto}%' AND marca 
                LIKE '%{marca}%' AND modelo 
                LIKE '%{modelo}%' AND cor 
                LIKE '%{cor}%' AND estoque 
                LIKE '{estoque}%'
                ORDER BY id_produto;""")

            buscaproduto = self.cursor.fetchall()

            for i in buscaproduto:
                self.listaproduto.insert("", END, values=i)

        self.desconecta_bd()

class Orcamento(Conexao):
    def limpaTelaAbaOrcamento(self):
        self.c_status_orcamento.delete(0, END)
        self.e_dataFim.delete(0, END)
        self.e_dataInicio.delete(0, END)

    def selecionaOrcamento(self):
        self.conecta_bd()
        self.listaOrcamento.delete(*self.listaOrcamento.get_children())

        listaData = self.cursor.execute(f"""
            SELECT PRODUTO_ORC.ID_ORCAMENTO
            , PESSOA.ID_PESSOA
            , PESSOA.NOME
            , PRODUTO_ORC.QUANTIDADE
            , PRODUTO_ORC.VALOR_VENDA
            , PRODUTO_ORC.DEFEITO
            , PRODUTO.PRODUTO
            , PRODUTO.MARCA
            , PRODUTO.MODELO
            , PRODUTO.COR
            , DATE_FORMAT(data_entrada, '%d/%m/%Y') as data_entrada 
            , DATE_FORMAT(data_retirada, '%d/%m/%Y') as data_retirada
            FROM PRODUTO_ORCADO PRODUTO_ORC
            INNER JOIN PESSOAS PESSOA ON PESSOA.ID_PESSOA = PRODUTO_ORC.ID_PESSOA
            INNER JOIN PRODUTO PRODUTO ON PRODUTO.ID_PRODUTO = PRODUTO_ORC.ID_PRODUTO
            INNER JOIN ORCAMENTO ORC ON ORC.ID_ORCAMENTO = PRODUTO_ORC.ID_ORCAMENTO
            WHERE PRODUTO_ORC.STATUS_ORCAMENTO = 'Orçamento'; """)

        listaData = self.cursor.fetchall()

        for i in listaData:
            self.listaOrcamento.insert("", END, values=i)

        self.desconecta_bd()


    def procuraStatusOrcamento(self):
        self.conecta_bd()
        self.listaOrcamento.delete(*self.listaOrcamento.get_children())

        status_orcamento = self.c_status_orcamento.get()
        dataInicio = self.e_dataInicio.get()
        dataFim = self.e_dataFim.get()

        if len(status_orcamento) > 0 or len(dataInicio) > 0 or len(dataFim) > 0:

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


            listaOrca = self.cursor.execute(f"""
            SELECT PRODUTO_ORC.ID_ORCAMENTO
            , PESSOA.ID_PESSOA
            , PESSOA.NOME
            , PRODUTO_ORC.QUANTIDADE
            , PRODUTO_ORC.VALOR_VENDA
            , PRODUTO_ORC.DEFEITO
            , PRODUTO.PRODUTO
            , PRODUTO.MARCA
            , PRODUTO.MODELO
            , PRODUTO.COR
            , DATE_FORMAT(data_entrada, '%d/%m/%Y') as data_entrada 
            , DATE_FORMAT(data_retirada, '%d/%m/%Y') as data_retirada
            FROM PRODUTO_ORCADO PRODUTO_ORC
            INNER JOIN PESSOAS PESSOA ON PESSOA.ID_PESSOA = PRODUTO_ORC.ID_PESSOA
            INNER JOIN PRODUTO PRODUTO ON PRODUTO.ID_PRODUTO = PRODUTO_ORC.ID_PRODUTO
            INNER JOIN ORCAMENTO ORC ON ORC.ID_ORCAMENTO = PRODUTO_ORC.ID_ORCAMENTO
            WHERE PRODUTO_ORC.STATUS_ORCAMENTO = '{status_orcamento}'
            AND data_entrada BETWEEN '{dataInicio}' AND '{dataFim}' ;""")


        buscaOr = self.cursor.fetchall()

        for i in buscaOr:
            self.listaOrcamento.insert("", END, values=i)


class Aplicacao_Relatorios(Pessoas, Produtos, RelatorioClientes, RelatorioProdutos, Orcamento, RelatorioOrcamentos):
    def __init__(self):
        self.relatorios = relatorio
        self.tela_Relatorios()
        self.abas()
        self.labelsEntryCliente()
        self.labelsProduto()
        self.labesOrcamento()
        self.botoesCliente()
        self.botoesProduto()
        self.botoesOrcamento()
        self.grid_Pessoas()
        self.grid_Produtos()
        self.grid_Orcamento()
        self.selecionaCliente()
        self.selecionaProduto()
        self.selecionaOrcamento()
        self.limpaTelaAbaOrcamento()
        self.limpaTelaClientes()

        self.relatorios.mainloop()

    def tela_Relatorios(self):
        self.relatorios.title("Relatórios")
        self.relatorios.config(bg=co3)
        self.relatorios.geometry("1095x700+263+0")
        self.relatorios.iconbitmap("C:/Users/Edinho/PycharmProjects/Meu_TCC/Logo/segatIcone.ico")

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

        self.l_dataInicioCliente = Label(self.abaCliente, text="Inicio:", font=("Courier", 13, "italic", "bold"), bg=co6, fg=co10)
        self.l_dataInicioCliente.place(x=525, y=10)
        self.e_dataInicioCliente = DateEntry(self.abaCliente, width=42, justify='left', relief='raised', bg=co0, fg=co10, locale="pt_br")
        self.e_dataInicioCliente.place(x=600, y=10)

        self.l_dataFimCliente = Label(self.abaCliente, text="Fim:", font=("Courier", 13, "italic", "bold"), bg=co6, fg=co10)
        self.l_dataFimCliente.place(x=555, y=35)
        self.e_dataFimCliente = DateEntry(self.abaCliente, width=42, justify='left', relief='raised', bg=co0, fg=co10, locale="pt_br")
        self.e_dataFimCliente.place(x=600, y=35)

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
    def labelsProduto(self):
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
        self.b_limpar = Button(self.abaProduto, text="Limpar", command=self.limpaTelaProdutos, font=("Courier", 13, "italic", "bold"),
                               bg=co1, fg=co2, relief=RAISED, overrelief=RIDGE)
        self.b_limpar.place(x=480, y=115, height=40, width=100)

        self.b_procurar = Button(self.abaProduto, text="Procurar", command=self.buscar_Produto, font=("Courier", 13, "italic", "bold"),
                                 bg=co1, fg=co2, relief=RAISED, overrelief=RIDGE)
        self.b_procurar.place(x=590, y=115, height=40, width=100)

        self.b_imprimir = Button(self.abaProduto, text="Imprimir", command=self.geraRelatorioProdutos, font=("Courier", 13, "italic", "bold"),
                                 bg=co1, fg=co2, relief=RAISED, overrelief=RIDGE)
        self.b_imprimir.place(x=700, y=115, height=40, width=100)

# - - - Orçamento - - -
    def labesOrcamento(self):
        self.l_status_orcamento = Label(self.abaOrdemServico, text="Status:", font=("Courier", 13, "italic", "bold"), bg=co6, fg=co10)
        self.l_status_orcamento.place(x=50, y=10)
        self.c_status_orcamento = Combobox(self.abaOrdemServico, width=42)
        self.c_status_orcamento["values"] = ("", "Orçamento", "Aprovado", "Retirado")
        self.c_status_orcamento.set("")
        self.c_status_orcamento.place(x=125, y=10)

        self.l_dataInicio = Label(self.abaOrdemServico, text="Inicio:", font=("Courier", 13, "italic", "bold"), bg=co6, fg=co10)
        self.l_dataInicio.place(x=50, y=35)
        self.e_dataInicio = DateEntry(self.abaOrdemServico, width=42, justify='left', relief='raised', bg=co0, fg=co10, locale = "pt_br")
        self.e_dataInicio.place(x=125, y=35)

        self.l_dataFim = Label(self.abaOrdemServico, text="Fim:", font=("Courier", 13, "italic", "bold"), bg=co6, fg=co10)
        self.l_dataFim.place(x=80, y=60)
        self.e_dataFim = DateEntry(self.abaOrdemServico, width=42, justify='left', relief='raised', bg=co0, fg=co10, locale = "pt_br")
        self.e_dataFim.place(x=125, y=60)


    def botoesOrcamento(self):
        self.b_procurar = Button(self.abaOrdemServico, command=self.procuraStatusOrcamento, text="Procurar",
                                 font=("Courier", 13, "italic", "bold"), bg=co1, fg=co2, relief=RAISED, overrelief=RIDGE)
        self.b_procurar.place(x=450, y=14, height=40, width=100)

        self.b_imprimir = Button(self.abaOrdemServico, text="Imprimir", command=self.geraRelatorioOrcamento,  font=("Courier", 13, "italic", "bold"),
                                 bg=co1, fg=co2, relief=RAISED, overrelief=RIDGE)
        self.b_imprimir.place(x=560, y=14, height=40, width=100)

    def grid_Orcamento(self):
        self.listaOrcamento = ttk.Treeview(self.abaOrdemServico, columns=("col0", "col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8", "col9", "col10", "col11", "col12"))
        self.listaOrcamento.heading("#0", text="")
        self.listaOrcamento.heading("#1", text="Orçamento")
        self.listaOrcamento.heading("#2", text="ID")
        self.listaOrcamento.heading("#3", text="Cliente")
        self.listaOrcamento.heading("#4", text="Qtdade")
        self.listaOrcamento.heading("#5", text="Valor")
        self.listaOrcamento.heading("#6", text="Defeito")
        self.listaOrcamento.heading("#7", text="Produto")
        self.listaOrcamento.heading("#8", text="Marca")
        self.listaOrcamento.heading("#9", text="Modelo")
        self.listaOrcamento.heading("#10", text="Cor")
        self.listaOrcamento.heading("#11", text="Data Entrada")
        self.listaOrcamento.heading("#12", text="Data Saída")

        self.listaOrcamento.column("#0", anchor='center', width=1)
        self.listaOrcamento.column("#1", anchor='center', width=75)
        self.listaOrcamento.column("#2", anchor='center', width=100)
        self.listaOrcamento.column("#3", anchor='center', width=60)
        self.listaOrcamento.column("#4", anchor='center', width=50)
        self.listaOrcamento.column("#5", anchor='center', width=60)
        self.listaOrcamento.column("#6", anchor='center', width=100)
        self.listaOrcamento.column("#7", anchor='center', width=100)
        self.listaOrcamento.column("#8", anchor='center', width=100)
        self.listaOrcamento.column("#9", anchor='center', width=100)
        self.listaOrcamento.column("#10", anchor='center', width=60)
        self.listaOrcamento.column("#11", anchor='center', width=90)
        self.listaOrcamento.column("#12", anchor='center', width=90)

        self.listaOrcamento.place(x=10, y=200, height=400, width=1037)

        self.barra_vertical = ttk.Scrollbar(self.abaOrdemServico, orient='vertical', command=self.listaproduto.yview)
        self.barra_vertical.place(x=1045, y=201, height=398, width=15)

        self.barra_horizontal = ttk.Scrollbar(self.abaOrdemServico, orient='horizontal', command=self.listapessoas.xview)
        self.barra_horizontal.place(x=10, y=598, height=15, width=1050)

        self.listaOrcamento.configure(yscrollcommand=self.barra_vertical.set, xscrollcommand=self.barra_horizontal.set)


Aplicacao_Relatorios()

