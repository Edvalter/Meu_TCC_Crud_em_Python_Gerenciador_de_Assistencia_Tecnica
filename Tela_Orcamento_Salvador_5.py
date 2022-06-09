from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import tix
from tkinter import font
from tkcalendar import Calendar, DateEntry
from datetime import datetime as dt
import mysql.connector
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image
import webbrowser

database = "gerenciador.db"

co0 = "#f0f3f5"  # white
co1 = "#f0f3f5"  # cizenta / grey
co2 = "#403d3d"  # letra
co3 = "#333333"  # azul escuro / fundo da tela / fundo dos label
co4 = "#666666"  # roxo claro / fundo do frame
co5 = "#759fe6"  # cor da borda - highlightbackground
co6 = "#A8A8A8"  # cinza
co7 = "#6aabb5"  # Botão Adicionar
co8 = "#ffff99"  # Botão Alterar
co9 = "#d54c4a"  # botão excluir
co10 = "Black"

# - - janela Cadastro de Pessoas - -

orcamento = Tk()


class Relatorio():
    def imprimir(self):
        webbrowser.open("cliente.pdf")

    def geraRelatorio(self):
        self.c = canvas.Canvas("cliente.pdf")

        self.idPessoaRelatorio = self.e_id_pessoa.get()
        self.nomeRelatorio = self.e_nome.get()
        self.whatsappRelatorio = self.e_whatsapp.get()
        self.data_cadastroRelatorio = self.e_data_cadastro.get()

        self.c.setFont("Helvetica-Bold", 18)
        self.c.drawString(200, 790, 'Ficha do Cliente')

        self.c.setFont("Helvetica-Bold", 12)
        self.c.drawString(50, 700,
                          'Código: ')  # + self.codigoRel) se eu quiser fazer a concatenação é so colocar essa parte
        self.c.drawString(50, 680, 'Nome: ')
        self.c.drawString(50, 660, 'Telefone: ')
        self.c.drawString(50, 640, 'Data do Cadastro: ')

        self.c.setFont("Helvetica", 12)

        self.c.drawString(110, 700, self.idPessoaRelatorio)
        self.c.drawString(90, 680, self.nomeRelatorio)
        self.c.drawString(110, 660, self.whatsappRelatorio)
        self.c.drawString(160, 640, self.data_cadastroRelatorio)

        self.c.rect(20, 550, 550, 5, fill=True, stroke=False)  # cria o retangulo no final da folha

        self.c.showPage()
        self.c.save()
        self.imprimir()


class Funcao():
    def limpa_Tela(self):
        self.e_id_orcamento.delete(0, END)
        self.e_id_pessoa.delete(0, END)
        self.e_cpf.delete(0, END)
        self.e_nome.delete(0, END)
        self.e_whatsapp.delete(0, END)
        self.e_telefone.delete(0, END)
        self.e_codOrcamento.get()
        self.e_id_produto.delete(0, END)
        self.e_produto.delete(0, END)
        self.e_marca.delete(0, END)
        self.e_modelo.delete(0, END)
        self.e_cor.delete(0, END)
        self.e_quantidade.delete(0, END)
        self.e_valor_venda.delete(0, END)
        self.e_defeito.delete(0, END)
        self.e_observacao.delete(0, END)
        self.e_data_entrada.delete(0, END)
        self.e_data_retirada.delete(0, END)

    def conecta_bd(self):
        self.conn = mysql.connector.connect(host='localhost', database='gerenciador', user='root', password='admin')
        self.cursor = self.conn.cursor()

    def desconecta_bd(self):
        self.conn.close()

    def montaTabelaOrca(self):
        self.conecta_bd()
        self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS
                    orca(
                        id_orcamento INT AUTO_INCREMENT PRIMARY KEY,
                        id_pessoa INT,
                        data_entrada DATE,
                        data_retirada DATE,
                    FOREIGN KEY (id_pessoa) REFERENCES pessoas (id_pessoa));""")

        self.conn.commit()
        self.desconecta_bd()

    def montaTabelaProdutoOrcado(self):
        self.conecta_bd()
        self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS 
                    produto_orcado(
                        cod_orcamento INT PRIMARY KEY, 
                        id_orcamento INT,
                        id_pessoa INT, 	
                        id_produto INT, 
                        quantidade INT,
                        valor_venda FLOAT,
                        defeito VARCHAR(100),
                        observacao VARCHAR(100),
                FOREIGN KEY (id_orcamento) REFERENCES orca (id_orcamento),
                FOREIGN KEY (id_pessoa) REFERENCES pessoas (id_pessoa),
                FOREIGN KEY (id_produto) REFERENCES produto (id_produto));""")

        self.conn.commit()
        self.desconecta_bd()

    def infoVariaveis(self):
        self.id_orcamento = self.e_id_orcamento.get()
        self.id_pessoa = self.e_id_pessoa.get()
        self.cpf = self.e_cpf.get()
        self.nome = self.e_nome.get()
        self.whatsapp = self.e_whatsapp.get()
        self.telefone = self.e_telefone.get()
        self.codOrcamento = self.e_codOrcamento.get()
        self.id_produto = self.e_id_produto.get()
        self.produto = self.e_produto.get()
        self.marca = self.e_marca.get()
        self.modelo = self.e_modelo.get()
        self.cor = self.e_cor.get()
        self.quantidade = self.e_quantidade.get()
        self.valor = self.e_valor_venda.get()
        self.defeito = self.e_defeito.get()
        self.observacao = self.e_observacao.get()

        self.data_entrada = self.e_data_entrada.get()
        self.dataEntradaConvertida = self.converteDataEntrada()

        self.data_retirada = self.e_data_retirada.get()
        self.dataRetiradaConvertida = self.converteDataRetirada()

    def converteDataEntrada(self):
        if self.data_entrada != '':
            dataEntradaConvertida = dt.strptime(self.data_entrada, '%d/%m/%Y')
            return dataEntradaConvertida
        else:
            pass

    def converteDataRetirada(self):
        if self.data_retirada != '':
            dataRetiradaConvertida = dt.strptime(self.data_retirada, '%d/%m/%Y')
            return dataRetiradaConvertida
        else:
            pass

    def adicionaOrcamento(self):
        self.infoVariaveis()
        self.conecta_bd()
        self.cursor.execute("""
            INSERT INTO 
                orca(
                    id_pessoa,
                    data_entrada, 
                    data_retirada) 
                VALUES (%s, %s, %s)""", (
                    self.id_pessoa,
                    self.dataEntradaConvertida,
                    self.dataRetiradaConvertida))

        messagebox.showinfo(title="Orçamento", message="Orçamento Gravado")

        self.conn.commit()
        self.desconecta_bd()


    def adicionaProdutoOrcado(self):
        self.infoVariaveis()
        if self.e_produto.get() == '':
            messagebox.showerror(title="Orçamento", message="Campo ID PRODUTO é Obrigatório")
            pass
        else:
            self.conecta_bd()
            self.cursor.execute("""
                INSERT INTO 
                    produto_orcado(cod_orcamento, id_pessoa, id_produto, quantidade, valor_venda, defeito, observacao)
                 VALUES (%s, %s, %s, %s, %s, %s)""", (
                        self.codOrcamento,
                        self.id_pessoa,
                        self.id_produto,
                        self.quantidade,
                        self.valor,
                        self.defeito,
                        self.observacao))

            messagebox.showinfo(title="Cadastro de Pessoas", message="Cadastro realizado com sucesso")

        self.conn.commit()
        self.desconecta_bd()
        self.selecionaOrcamento()
        self.limpa_Tela()

    def selecionaPessoa(self):
        self.listaOrcamentoCliente.delete(*self.listaOrcamentoCliente.get_children())
        self.conecta_bd()
        listaPe = self.cursor.execute(""" SELECT * FROM cad_pessoas ORDER BY id_pessoa ASC; """)
        listaPe = self.cursor.fetchall()
        for i in listaPe:
            self.listaOrcamentoCliente.insert("", END, values=i)

        self.desconecta_bd()

    def selecionaProduto(self):
        self.listaOrcarmentoProduto.delete(*self.listaOrcarmentoProduto.get_children())
        self.conecta_bd()
        listaPro = self.cursor.execute(""" SELECT * FROM cad_produto ORDER BY marca ASC; """)

        listaPro = self.cursor.fetchall()

        for i in listaPro:
            self.listaOrcarmentoProduto.insert("", END, values=i)

        self.desconecta_bd()

#    def selecionaOrcamento(self):
#        self.listaOrcamento.delete(*self.listaOrcamento.get_children())
#        self.conecta_bd()
#        lista = self.cursor.execute(""" SELECT * FROM orca; """)
#        lista = self.cursor.fetchall()
#        for i in lista:
#            posicao = i[0:3] + (i[3].strftime('%d/%m/%Y'), i[4].strftime('%d/%m/%Y'))
#            self.listaOrcamento.insert("", END, values=posicao)

#        self.desconecta_bd()

    def selecionaOrcamento(self):
        self.listaOrcamento.delete(*self.listaOrcamento.get_children())
        self.conecta_bd()
        lista = self.cursor.execute(""" SELECT * FROM produto_orcado; """)
        lista = self.cursor.fetchall()
        for i in lista:
            self.listaOrcamento.insert("", END, values=i)

        self.desconecta_bd()

    def duplo_CliqueCliente(self, event):
        self.listaOrcarmentoCliente.selection()

        for n in self.listaOrcarmentoCliente.selection():
            col1, col2, col3, col4, col5 = self.listaOrcarmentoCliente.item(n, 'values')

            self.e_id_pessoa.delete(0, END)
            self.e_cpf.delete(0, END)
            self.e_nome.delete(0, END)
            self.e_whatsapp.delete(0, END)
            self.e_telefone.delete(0, END)

            self.e_id_pessoa.insert(END, col1)
            self.e_cpf.insert(END, col2)
            self.e_nome.insert(END, col3)
            self.e_whatsapp.insert(END, col4)
            self.e_telefone.insert(END, col5)

    def duplo_CliqueProduto(self, event):
        self.listaOrcarmentoProduto.selection()

        for n in self.listaOrcarmentoProduto.selection():
            col1, col2, col3, col4, col5, col6 = self.listaOrcarmentoProduto.item(n, 'values')

            self.e_id_produto.delete(0, END)
            self.e_produto.delete(0, END)
            self.e_marca.delete(0, END)
            self.e_modelo.delete(0, END)
            self.e_cor.delete(0, END)
            self.e_valor_venda.delete(0, END)

            self.e_id_produto.insert(END, col1)
            self.e_produto.insert(END, col2)
            self.e_marca.insert(END, col3)
            self.e_modelo.insert(END, col4)
            self.e_cor.insert(END, col5)
            self.e_valor_venda.insert(END, col6)

    def duplo_CliqueOrcamento(self, event):
        self.limpa_Tela()
        self.listaOrcamento.selection()

        for n in self.listaOrcamento.selection():
            col1, col2, col3, col4, col5, col6, col7 = self.listaOrcamento.item(n, 'values')
            self.e_cod_orcamento.delete(0, END)
            self.e_id_orcamento.delete(0, END)
            self.e_id_produto.delete(0, END)
            self.e_quantidade.delete(0, END)
            self.e_valor_venda.delete(0, END)
            self.e_defeito.delete(0, END)
            self.e_observacao.delete(0, END)


            self.e_cod_orcamento.insert(END, col1)
            self.e_id_orcamento.insert(END, col2)
            self.e_id_produto.insert(END, col3)
            self.e_quantidade.insert(END, col4)
            self.e_valor_venda.insert(END, col5)
            self.e_defeito.insert(END, col6)
            self.e_observacao.insert(END, col7)

    def busca_Cliente(self):
        self.conecta_bd()
        self.listaOrcarmentoCliente.delete(*self.listaOrcarmentoCliente.get_children())

        id_pessoa = self.e_id_pessoa.get()
        cpf = self.e_cpf.get()
        nome = self.e_nome.get()
        whatsapp = self.e_whatsapp.get()

        if len(id_pessoa) > 0:
            self.e_id_pessoa.insert(END, "%")
            id_pessoa = self.e_id_pessoa.get()
            self.cursor.execute("""
                   SELECT id_pessoa, cpf, nome, whatsapp, telefone FROM 
                       cad_pessoas
                   WHERE 
                       id_pessoa 
                   LIKE '%s' ORDER BY cpf ASC""" % id_pessoa, )

            buscaid_pessoa = self.cursor.fetchall()

            for i in buscaid_pessoa:
                self.listaOrcarmentoCliente.insert("", END, values=i)

        elif len(cpf) > 0:
            self.e_cpf.insert(END, "%")
            cpf = self.e_cpf.get()
            self.cursor.execute("""
                   SELECT id_pessoa, cpf, nome, whatsapp, telefone FROM 
                       cad_pessoas 
                   WHERE 
                       cpf 
                   LIKE '%s' ORDER BY nome ASC""" % cpf, )
            buscacpf = self.cursor.fetchall()

            for i in buscacpf:
                self.listaOrcarmentoCliente.insert("", END, values=i)

        elif len(nome) > 0:
            self.e_nome.insert(END, "%")
            nome = self.e_nome.get()
            self.cursor.execute("""
                   SELECT id_pessoa, cpf, nome, whatsapp, telefone FROM 
                       cad_pessoas 
                   WHERE 
                       nome 
                   LIKE '%s' ORDER BY nome ASC""" % nome, )
            buscanome = self.cursor.fetchall()

            for i in buscanome:
                self.listaOrcarmentoCliente.insert("", END, values=i)


        elif len(whatsapp) > 0:
            self.e_whatsapp.insert(END, "%")
            whatsapp = self.e_whatsapp.get()
            self.cursor.execute("""
                   SELECT id_pessoa,cpf, nome, whatsapp, telefone FROM 
                       cad_pessoas 
                   WHERE 
                       whatsapp 
                   LIKE '%s' ORDER BY whatsapp ASC""" % whatsapp, )

            buscaWhatsapp = self.cursor.fetchall()

            for i in buscaWhatsapp:
                self.listaOrcarmentoCliente.insert("", END, values=i)

        self.desconecta_bd()

    def busca_Produto(self):
        self.conecta_bd()
        self.listaOrcarmentoProduto.delete(*self.listaOrcarmentoProduto.get_children())

        id_produto = self.e_id_produto.get()
        produto = self.e_produto.get()
        marca = self.e_marca.get()
        modelo = self.e_modelo.get()
        cor = self.e_cor.get()

        if len(id_produto) > 0:

            self.e_id_produto.insert(END, "%")
            id_produto = self.e_id_produto.get()
            self.cursor.execute("""
                SELECT id_produto, produto, marca, modelo, cor, valor_venda FROM 
                    cad_produto
                WHERE 
                    id_produto 
                LIKE '%s' ORDER BY id_produto ASC""" % id_produto, )

            buscaid_produto = self.cursor.fetchall()

            for i in buscaid_produto:
                self.listaOrcarmentoProduto.insert("", END, values=i)

        elif len(produto) > 0:
            self.e_produto.insert(END, "%")
            produto = self.e_produto.get()
            self.cursor.execute("""
                SELECT id_produto, produto, marca, modelo, cor, valor_venda  FROM 
                    cad_produto 
                WHERE 
                    produto 
                LIKE '%s' ORDER BY marca ASC""" % produto, )

            buscaproduto = self.cursor.fetchall()

            for i in buscaproduto:
                self.listaOrcarmentoProduto.insert("", END, values=i)


        elif len(marca) > 0:
            self.e_marca.insert(END, "%")
            marca = self.e_marca.get()
            self.cursor.execute("""
                SELECT id_produto, produto, marca, modelo, cor, valor_venda  FROM 
                    cad_produto 
                WHERE 
                    marca 
                LIKE '%s' ORDER BY marca ASC""" % marca, )

            buscamarca = self.cursor.fetchall()

            for i in buscamarca:
                self.listaOrcarmentoProduto.insert("", END, values=i)

        elif len(modelo) > 0:
            self.e_modelo.insert(END, "%")
            modelo = self.e_modelo.get()
            self.cursor.execute("""
                SELECT id_produto, produto, marca, modelo, cor, valor_venda  FROM 
                    cad_produto 
                WHERE 
                    modelo 
                LIKE '%s' ORDER BY marca ASC""" % modelo, )

            buscamodelo = self.cursor.fetchall()

            for i in buscamodelo:
                self.listaOrcarmentoProduto.insert("", END, values=i)

            self.desconecta_bd()

        elif len(cor) > 0:
            self.e_cor.insert(END, "%")
            cor = self.e_cor.get()
            self.cursor.execute("""
                SELECT id_produto, produto, marca, modelo, cor, valor_venda FROM 
                    cad_produto 
                WHERE 
                    cor 
                LIKE '%s' ORDER BY cor ASC""" % cor, )

            buscacor = self.cursor.fetchall()

            for i in buscacor:
                self.listaOrcarmentoProduto.insert("", END, values=i)

        self.desconecta_bd()

    def alteraOrcamento(self):
        self.infoVariaveis()
        if self.id_orcamento == '':
            pass
        else:
            self.conecta_bd()
            self.cursor.execute("""
                UPDATE
                    orca
                SET 
                    id_orcamento = %s, 
                    id_produto = %s, 
                    quantidade = %s, 
                    valor_venda = %s, 
                    defeito = %s, 
                    observacao = %s,
                WHERE
                    cod_orcamento = %s """, (
                    self.id_pessoa,
                    self.id_produto,
                    self.quantidade,
                    self.valor,
                    self.defeito,
                    self.observacao,
                    self.codOrcamento))

    def buscaOrcamento(self):
        self.conecta_bd()
        self.listaOrcamento.delete(*self.listaOrcamento.get_children())

        id_orcamento = self.e_id_orcamento.get()
        cpf = self.e_cpf.get()
        nome = self.e_nome.get()
        id_pessoa = self.e_id_pessoa.get()
        telefone = self.e_telefone.get()
        whatsapp = self.e_whatsapp.get()

        if len(id_orcamento) > 0:
            self.e_id_orcamento.insert(END, "%")
            id_orcamento = self.e_id_orcamento.get()
            self.cursor.execute("""
                   SELECT * FROM  
                       orcamento 
                   WHERE 
                       id_orcamento 
                   LIKE '%s' ORDER BY cpf ASC""" % id_orcamento, )

            buscacpf = self.cursor.fetchall()

            for i in buscacpf:
                self.listaOrcamento.insert("", END, values=i)

        elif len(cpf) > 0:
            self.e_cpf.insert(END, "%")
            cpf = self.e_cpf.get()
            self.cursor.execute("""
                   SELECT * FROM  
                       orcamento 
                   WHERE 
                       cpf 
                   LIKE '%s' ORDER BY cpf ASC""" % cpf, )

            buscacpf = self.cursor.fetchall()

            for i in buscacpf:
                self.listaOrcamento.insert("", END, values=i)


        elif len(nome) > 0:
            self.e_nome.insert(END, "%")
            nome = self.e_nome.get()
            self.cursor.execute("""
                   SELECT * FROM 
                       orcamento
                   WHERE 
                       nome 
                   LIKE '%s' ORDER BY nome ASC""" % nome, )

            buscanome = self.cursor.fetchall()

            for i in buscanome:
                self.listaOrcamento.insert("", END, values=i)

        elif len(id_pessoa) > 0:
            self.e_id_pessoa.insert(END, "%")
            id_pessoa = self.e_id_pessoa.get()
            self.cursor.execute("""
                   SELECT * FROM 
                       orcamento 
                   WHERE 
                       id_pessoa 
                   LIKE '%s' ORDER BY id_pessoa ASC""" % id_pessoa, )

            buscaid_pessoas = self.cursor.fetchall()

            for i in buscaid_pessoas:
                self.listaOrcamento.insert("", END, values=i)

        elif len(telefone) > 0:
            self.e_telefone.insert(END, "%")
            telefone = self.e_telefone.get()
            self.cursor.execute("""
                   SELECT * FROM 
                       orcamento 
                   WHERE 
                       telefone 
                   LIKE '%s' ORDER BY telefone ASC""" % telefone, )

            buscatelefone = self.cursor.fetchall()

            for i in buscatelefone:
                self.listaOrcamento.insert("", END, values=i)

        elif len(whatsapp) > 0:
            self.e_whatsapp.insert(END, "%")
            whatsapp = self.e_whatsapp.get()
            self.cursor.execute("""
                               SELECT * FROM 
                                   orcamento 
                               WHERE 
                                   whatsapp
                               LIKE '%s' ORDER BY telefone ASC""" % whatsapp, )

            buscawhatsapp = self.cursor.fetchall()

            for i in buscawhatsapp:
                self.listaOrcamento.insert("", END, values=i)


class Aplicacao_Orcamento(Funcao, Relatorio):
    def __init__(self):
        self.orcamento = orcamento
        self.tela_orcamento()
        self.frames_Orcamento()
        self.labels_entry()
        self.botoes()
        self.infoVariaveis()
        self.montaTabelaOrca()
        self.montaTabelaProdutoOrcado()
        self.gridOrcamentoCliente()
        self.gridOrcamentoProduto()
        self.gridOrcamento()
        self.selecionaOrcamento()

        self.orcamento.mainloop()

    def tela_orcamento(self):
        self.orcamento.title("Orçamento")
        self.orcamento.config(bg=co3)
        self.orcamento.geometry("1095x700+263+0")

    def frames_Orcamento(self):
        self.frameSuperior = Frame(self.orcamento, bg=co4, highlightbackground=co5, highlightthickness=6)
        self.frameSuperior.place(x=5, y=5, height=310, width=1085)

        self.frameGridCliente = Frame(self.orcamento, bg=co10, highlightbackground=co5, highlightthickness=6)
        self.frameGridCliente.place(x=5, y=320, height=105, width=400)

        self.frameGridProduto = Frame(self.orcamento, bg=co10, highlightbackground=co5, highlightthickness=6)
        self.frameGridProduto.place(x=410, y=320, height=105, width=680)

        self.frameGridOrcamento = Frame(self.orcamento, bg=co10, highlightbackground=co5, highlightthickness=6)
        self.frameGridOrcamento.place(x=5, y=430, height=155, width=1085)

        self.frameInferior = Frame(self.orcamento, bg=co4, highlightbackground=co5, highlightthickness=6)
        self.frameInferior.place(x=5, y=590, height=100, width=1085)

    # - - - - - - - Frame Superior- - - - - - -

    def labels_entry(self):
        # - - - - - - - Pessoas - - - - - -
        self.l_id_orcamento = Label(self.frameSuperior, text="Orçamento:", font=("Courier", 13, "italic", "bold"),
                                    bg=co4, fg=co10)
        self.l_id_orcamento.place(x=50, y=5)
        self.e_id_orcamento = Entry(self.frameSuperior, width=45, justify='left', relief='raised', bg=co0, fg=co10)
        self.e_id_orcamento.place(x=155, y=5)

        self.l_id_pessoa = Label(self.frameSuperior, text="Código Cliente:", font=("Courier", 13, "italic", "bold"),
                                 bg=co4, fg=co10)
        self.l_id_pessoa.place(x=0, y=30)
        self.e_id_pessoa = Entry(self.frameSuperior, width=45, justify='left', relief='raised', bg=co0, fg=co10)
        self.e_id_pessoa.place(x=155, y=30)

        self.l_cpf = Label(self.frameSuperior, text="Cpf:", font=("Courier", 13, "italic", "bold"), bg=co4, fg=co10)
        self.l_cpf.place(x=110, y=55)
        self.e_cpf = Entry(self.frameSuperior, width=45, justify='left', relief='raised', bg=co0, fg=co10)
        self.e_cpf.place(x=155, y=55)

        self.l_nome = Label(self.frameSuperior, text="Nome:", font=("Courier", 13, "italic", "bold"), bg=co4, fg=co10)
        self.l_nome.place(x=100, y=80)
        self.e_nome = Entry(self.frameSuperior, width=45, justify='left', relief='raised', bg=co0, fg=co10)
        self.e_nome.place(x=155, y=80)

        self.l_whatsapp = Label(self.frameSuperior, text="Whatsapp:", font=("Courier", 13, "italic", "bold"), bg=co4,
                                fg=co10)
        self.l_whatsapp.place(x=60, y=105)
        self.e_whatsapp = Entry(self.frameSuperior, width=45, justify='left', relief='raised', bg=co0, fg=co10)
        self.e_whatsapp.place(x=155, y=105)

        self.l_telefone = Label(self.frameSuperior, text="Telefone:", font=("Courier", 13, "italic", "bold"),
                                bg=co4, fg=co10)
        self.l_telefone.place(x=60, y=130)
        self.e_telefone = Entry(self.frameSuperior, width=45, justify='left', relief='raised', bg=co0, fg=co10)
        self.e_telefone.place(x=155, y=130)

        self.l_data_entrada = Label(self.frameSuperior, text="Entrada:", font=("Courier", 13, "italic", "bold"), bg=co4,
                                    fg=co10)
        self.l_data_entrada.place(x=70, y=155)
        self.e_data_entrada = DateEntry(self.frameSuperior, width=42, justify='left', relief='raised', locale="pt_br")
        self.e_data_entrada.place(x=155, y=155)

        self.l_data_retirada = Label(self.frameSuperior, text="Retirada:", font=("Courier", 13, "italic", "bold"), bg=co4, fg=co10)
        self.l_data_retirada.place(x=60, y=180)
        self.e_data_retirada = DateEntry(self.frameSuperior, width=42, justify='left', relief='raised', locale="pt_br")
        self.e_data_retirada.place(x=155, y=180)

        # - - - - - - - Produtos - - - - - -
        self.l_codOrcamento = Label(self.frameSuperior, text="Orçamento:", font=("Courier", 13, "italic", "bold"), bg=co4,
                                 fg=co10)
        self.l_codOrcamento.place(x=535, y=5)
        self.e_codOrcamento = Entry(self.frameSuperior, width=45, justify='left', relief='raised', bg=co0, fg=co10)
        self.e_codOrcamento.place(x=650, y=5)


        self.l_id_produto = Label(self.frameSuperior, text="Id Produdo:", font=("Courier", 13, "italic", "bold"),
                                  bg=co4, fg=co10)
        self.l_id_produto.place(x=535, y=30)
        self.e_id_produto = Entry(self.frameSuperior, width=45, justify='left', relief='raised', bg=co0, fg=co10)
        self.e_id_produto.place(x=650, y=30)

        self.l_produto = Label(self.frameSuperior, text="Produdo:", font=("Courier", 13, "italic", "bold"), bg=co4,
                               fg=co10)
        self.l_produto.place(x=565, y=55)
        self.e_produto = Entry(self.frameSuperior, width=45, justify='left', relief='raised', bg=co0, fg=co10)
        self.e_produto.place(x=650, y=55)

        self.l_marca = Label(self.frameSuperior, text="Marca:", font=("Courier", 13, "italic", "bold"), bg=co4, fg=co10)
        self.l_marca.place(x=585, y=80)
        self.e_marca = Entry(self.frameSuperior, width=45, justify='left', relief='raised', bg=co0, fg=co10)
        self.e_marca.place(x=650, y=80)

        self.l_modelo = Label(self.frameSuperior, text="Modelo:", font=("Courier", 13, "italic", "bold"), bg=co4,
                              fg=co10)
        self.l_modelo.place(x=575, y=105)
        self.e_modelo = Entry(self.frameSuperior, width=45, justify='left', relief='raised', bg=co0, fg=co10)
        self.e_modelo.place(x=650, y=105)

        self.l_cor = Label(self.frameSuperior, text="Cor:", font=("Courier", 13, "italic", "bold"), bg=co4, fg=co10)
        self.l_cor.place(x=605, y=130)
        self.e_cor = Entry(self.frameSuperior, width=45, justify='left', relief='raised', bg=co0, fg=co10)
        self.e_cor.place(x=650, y=130)

        self.l_quantidade = Label(self.frameSuperior, text="Quantidade:", font=("Courier", 13, "italic", "bold"),
                                  bg=co4, fg=co10)
        self.l_quantidade.place(x=535, y=155)
        self.e_quantidade = Entry(self.frameSuperior, width=45, justify='left', relief='raised', bg=co0, fg=co10)
        self.e_quantidade.place(x=650, y=155)

        self.l_valor_venda = Label(self.frameSuperior, text="Valor:", font=("Courier", 13, "italic", "bold"), bg=co4,
                                   fg=co10)
        self.l_valor_venda.place(x=585, y=180)
        self.e_valor_venda = Entry(self.frameSuperior, width=45, justify='left', relief='raised', bg=co0, fg=co10)
        self.e_valor_venda.place(x=650, y=180)

        self.l_defeito = Label(self.frameSuperior, text="Defeito:", font=("Courier", 13, "italic", "bold"), bg=co4,
                               fg=co10)
        self.l_defeito.place(x=565, y=205)
        self.e_defeito = Entry(self.frameSuperior, width=45, justify='left', relief='raised', bg=co0, fg=co10)
        self.e_defeito.place(x=650, y=205)

        self.l_observacao = Label(self.frameSuperior, text="Obersvações:", font=("Courier", 13, "italic", "bold"),
                                  bg=co4, fg=co10)
        self.l_observacao.place(x=525, y=230)
        self.e_observacao = Entry(self.frameSuperior, width=45, justify='left', relief='raised', bg=co0, fg=co10)
        self.e_observacao.place(x=650, y=230)

        # - - - - - - - Frame Inferior - - - - - - -

        self.l_quantidadeItens = Label(self.frameInferior, text="Quantidade de Itens:",
                                       font=("Courier", 13, "italic", "bold"), bg=co4, fg=co10)
        self.l_quantidadeItens.place(x=10, y=10)
        self.e_quantidadeItens = Entry(self.frameInferior, width=35, justify='left', relief='solid', bg=co0, fg=co10)
        self.e_quantidadeItens.place(x=215, y=10)

        self.l_desconto = Label(self.frameInferior, text="Desconto:", font=("Courier", 13, "italic", "bold"), bg=co4,
                                fg=co10)
        self.l_desconto.place(x=120, y=35)
        self.e_desconto = Entry(self.frameInferior, width=35, justify='left', relief='solid', bg=co0, fg=co10)
        self.e_desconto.place(x=215, y=35)

        self.l_valor = Label(self.frameInferior, text="Valor Total:", font=("Courier", 13, "italic", "bold"), bg=co4,
                             fg=co10)
        self.l_valor.place(x=90, y=60)
        self.e_valor = Entry(self.frameInferior, width=35, justify='left', relief='solid', bg=co0, fg=co10)
        self.e_valor.place(x=215, y=60)

    # - - - - - - - Botões - - - - - - -

    def botoes(self):
        self.b_procurarCliente = Button(self.frameSuperior, text="Procurar", command=self.busca_Cliente,
                                        width=10, font=('Courier 9 italic bold'), bg=co6, fg=co10,
                                        relief=RAISED, overrelief=RIDGE)
        self.b_procurarCliente.place(x=440, y=5, height=25, width=70)

        self.b_procurarProduto = Button(self.frameSuperior, text="Procurar", command=self.busca_Produto,
                                        width=10, font=('Courier 9 italic bold'), bg=co6, fg=co10,
                                        relief=RAISED, overrelief=RIDGE)
        self.b_procurarProduto.place(x=935, y=5, height=25, width=70)

        self.b_adicionarCliente = Button(self.frameSuperior, text="Gravar", command=self.adicionaOrcamento,
                                         width=10, font=("Courier", 13, "italic", "bold"), bg=co7, fg=co10,
                                         relief=RAISED, overrelief=RIDGE)
        self.b_adicionarCliente.place(x=330, y=255, height=40, width=100)

        self.b_limpar = Button(self.frameSuperior, text="Limpar", command=self.limpa_Tela,
                               width=10, font=("Courier", 13, "italic", "bold"), bg=co6, fg=co10,
                               relief=RAISED, overrelief=RIDGE)
        self.b_limpar.place(x=520, y=255, height=40, width=100)

        self.b_procurar = Button(self.frameSuperior, text="Procurar", command=self.buscaOrcamento,
                                 width=10, font=("Courier", 13, "italic", "bold"),
                                 bg=co6, fg=co10, relief=RAISED, overrelief=RIDGE)
        self.b_procurar.place(x=630, y=255, height=40, width=100)

        self.b_imprimir = Button(self.frameSuperior, text="Imprimir", command=self.geraRelatorio,
                                 width=10, font=("Courier", 13, "italic", "bold"),
                                 bg=co6, fg=co10, relief=RAISED, overrelief=RIDGE)
        self.b_imprimir.place(x=740, y=255, height=40, width=100)

        self.b_adicionar = Button(self.frameSuperior, text="Adicionar", command=self.adicionaProdutoOrcado,
                                  width=10, font=("Courier", 13, "italic", "bold"), bg=co7, fg=co10,
                                  relief=RAISED, overrelief=RIDGE)
        self.b_adicionar.place(x=850, y=255, height=40, width=100)

        self.b_alterar = Button(self.frameSuperior, text="Alterar", command=self.alteraOrcamento,
                                font=("Courier", 13, "italic", "bold"), bg=co8, fg=co10,
                                relief=RAISED, overrelief=RIDGE)
        self.b_alterar.place(x=960, y=255, height=40, width=100)

    # - - - - - - - Grid Clientes - - - - - - -
    def gridOrcamentoCliente(self):
        self.listaOrcarmentoCliente = ttk.Treeview(self.frameGridCliente,
                                                   columns=("col0", "col1", "col2", "col3", "col4"))
        self.listaOrcarmentoCliente.heading("#0", text="")
        self.listaOrcarmentoCliente.heading("#1", text="ID")
        self.listaOrcarmentoCliente.heading("#2", text="CPF")
        self.listaOrcarmentoCliente.heading("#3", text="Nome")
        self.listaOrcarmentoCliente.heading("#4", text="Whatsapp")
        self.listaOrcarmentoCliente.heading("#5", text="Telefone")

        self.listaOrcarmentoCliente.column("#0", anchor='center', width=1)
        self.listaOrcarmentoCliente.column("#1", anchor='center', width=77)
        self.listaOrcarmentoCliente.column("#2", anchor='center', width=77)
        self.listaOrcarmentoCliente.column("#3", anchor='center', width=77)
        self.listaOrcarmentoCliente.column("#4", anchor='center', width=77)
        self.listaOrcarmentoCliente.column("#5", anchor='center', width=77)

        self.listaOrcarmentoCliente.place(x=0, y=0, height=95, width=388)

        self.barra_vertical = ttk.Scrollbar(self.frameGridCliente, orient='vertical',
                                            command=self.listaOrcarmentoCliente.yview)
        self.barra_vertical.place(x=1, y=1, height=82, width=15)

        self.barra_horizontal = ttk.Scrollbar(self.frameGridCliente, orient='horizontal',
                                              command=self.listaOrcarmentoCliente.xview)
        self.barra_horizontal.place(x=1, y=80, height=15, width=386)

        self.listaOrcarmentoCliente.configure(yscrollcommand=self.barra_vertical.set,
                                              xscrollcommand=self.barra_horizontal.set)

        self.listaOrcarmentoCliente.bind("<Double-1>", self.duplo_CliqueCliente)

    # - - - - - - - Grid Produtos - - - - - - -
    def gridOrcamentoProduto(self):
        self.listaOrcarmentoProduto = ttk.Treeview(self.frameGridProduto,
                                                   columns=("col0", "col1", "col2", "col3", "col4", "col5"))
        self.listaOrcarmentoProduto.heading("#0", text="")
        self.listaOrcarmentoProduto.heading("#1", text="ID Produto")
        self.listaOrcarmentoProduto.heading("#2", text="Produto")
        self.listaOrcarmentoProduto.heading("#3", text="Marca")
        self.listaOrcarmentoProduto.heading("#4", text="Modelo")
        self.listaOrcarmentoProduto.heading("#5", text="Cor")
        self.listaOrcarmentoProduto.heading("#6", text="Valor")

        self.listaOrcarmentoProduto.column("#0", anchor='center', width=1)
        self.listaOrcarmentoProduto.column("#1", anchor='center', width=105)
        self.listaOrcarmentoProduto.column("#2", anchor='center', width=105)
        self.listaOrcarmentoProduto.column("#3", anchor='center', width=105)
        self.listaOrcarmentoProduto.column("#4", anchor='center', width=105)
        self.listaOrcarmentoProduto.column("#5", anchor='center', width=105)
        self.listaOrcarmentoProduto.column("#6", anchor='center', width=105)

        self.listaOrcarmentoProduto.place(x=0, y=0, height=95, width=668)

        self.barra_vertical = ttk.Scrollbar(self.frameGridProduto, orient='vertical',
                                            command=self.listaOrcarmentoProduto.yview)
        self.barra_vertical.place(x=0, y=1, height=82, width=15)

        self.barra_horizontal = ttk.Scrollbar(self.frameGridProduto, orient='horizontal',
                                              command=self.listaOrcarmentoProduto.xview)
        self.barra_horizontal.place(x=0, y=79, height=15, width=667)

        self.listaOrcarmentoProduto.configure(yscrollcommand=self.barra_vertical.set,
                                              xscrollcommand=self.barra_horizontal.set)

        self.listaOrcarmentoProduto.bind("<Double-1>", self.duplo_CliqueProduto)

    # - - - - - - - Grid Orçamentos - - - - - - -
    def gridOrcamento(self):
        self.listaOrcamento = ttk.Treeview(self.frameGridOrcamento,
                                           columns=("col0", "col1", "col2", "col3",
                                                    "col4", "col5"))
        self.listaOrcamento.heading("#0", text="")
        self.listaOrcamento.heading("#1", text="Orçamento")
        self.listaOrcamento.heading("#2", text="ID Produto")
        self.listaOrcamento.heading("#3", text="Quantidade")
        self.listaOrcamento.heading("#4", text="Valor")
        self.listaOrcamento.heading("#5", text="Defeito")
        self.listaOrcamento.heading("#6", text="Observação")

        self.listaOrcamento.column("#0", anchor='center', width=1)
        self.listaOrcamento.column("#1", anchor='center', width=60)
        self.listaOrcamento.column("#2", anchor='center', width=60)
        self.listaOrcamento.column("#3", anchor='center', width=60)
        self.listaOrcamento.column("#4", anchor='center', width=60)
        self.listaOrcamento.column("#5", anchor='center', width=60)


        self.listaOrcamento.place(x=0, y=0, height=144, width=1073)

        self.barra_vertical = ttk.Scrollbar(self.frameGridOrcamento, orient='vertical',
                                            command=self.listaOrcamento.yview)
        self.barra_vertical.place(x=1, y=1, height=128, width=15)

        self.barra_horizontal = ttk.Scrollbar(self.frameGridOrcamento, orient='horizontal',
                                              command=self.listaOrcamento.xview)
        self.barra_horizontal.place(x=1, y=128, height=15, width=1065)

        self.listaOrcamento.configure(yscrollcommand=self.barra_vertical.set, xscrollcommand=self.barra_horizontal.set)

        self.listaOrcamento.bind("<Double-1>", self.duplo_CliqueOrcamento)


Aplicacao_Orcamento()