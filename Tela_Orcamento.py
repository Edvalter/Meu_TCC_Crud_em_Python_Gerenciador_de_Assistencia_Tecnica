
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from tkinter import messagebox
from tkinter import tix
from tkinter.tix import *
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
from subprocess import call
import pywhatkit as kt

database = "gerenciador.db"

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

# - - janela Cadastro de Pessoas - -

orcamento = tix.Tk()

class Relatorio():
    def imprimir(self):
        webbrowser.open("OS.pdf")

    def geraRelatorio(self):
        self.conecta_bd()
        self.listaPessoas = self.cursor.execute(f""" 
            SELECT 
                id_pessoa, 
                id_orcamento, 
                id_produto, 
                quantidade, 
                valor_venda, 
                defeito, 
                observacao
                as data_cadastro  FROM produto_orcado ; """)

        self.listaPessoas = self.cursor.fetchall()

        self.relatorioOrcamento = canvas.Canvas( "OS.pdf", pagesize=A4) # abre o relatório os
        self.relatorioOrcamento.drawImage("C:/Users/Edinho/PycharmProjects/Meu_TCC/Logo/LogoE.png", x=30, y=720, width=100, height=130) # imprime a logo no relatório

# - - Meu Cabeçalho - - - -
        self.relatorioOrcamento.setFont("Helvetica", 10)
        self.relatorioOrcamento.drawString(150, 810,  'Segat - Sistema Gerenciador de assistência Técnica')
        self.relatorioOrcamento.drawString(150, 795, 'Endereço: R: Quênia 94')
        self.relatorioOrcamento.drawString(150, 780, 'Centro - Timbó - SC')
        self.relatorioOrcamento.drawString(150, 765, 'CNPJ: 12.123.12.0001/23')
        self.relatorioOrcamento.drawString(150, 750, 'Telefone / WhatsApp: (47) 9 9247 9998')

# - - Titulo do Relatório- - - -
        self.relatorioOrcamento.setFont("Helvetica-Bold", 15)
        self.relatorioOrcamento.drawString(240, 720, 'Ordem de Serviço')

# - - pega as informações dos entry - - - -
        self.idRel = self.e_id_orcamento.get()
        self.idPessoaRel = self.e_id_pessoa.get()
        self.nomeRel = self.e_nome.get()
        self.telefoneRel = self.e_telefone.get()
        self.whatsappRel = self.e_whatsapp.get()
        self.dataEntradaRel = self.e_data_entrada.get()
        self.dataRetiradaRel = self.e_data_retirada.get()
        self.produtoRel = self.e_produto.get()
        self.marcaRel = self.e_marca.get()
        self.modeloRel = self.e_modelo.get()
        self.corRel = self.e_cor.get()
        self.valorRel = self.e_valor_venda.get()
        self.defeitoRel = self.e_defeito.get()
        self.observaroRel = self.e_observacao.get()

# - - - Imprime as chamadas da informações - - - -
        self.relatorioOrcamento.setFont("Helvetica-Bold", 10)
        self.relatorioOrcamento.drawString(50, 700, 'OS:')
        self.relatorioOrcamento.drawString(50, 685, 'Cliente:')
        self.relatorioOrcamento.drawString(230, 700, 'Telefone:')
        self.relatorioOrcamento.drawString(230, 685, 'Whatsapp:')
        self.relatorioOrcamento.drawString(50, 660, 'Produto:')
        self.relatorioOrcamento.drawString(50, 645, 'Marca:')
        self.relatorioOrcamento.drawString(50, 630, 'Modelo:')
        self.relatorioOrcamento.drawString(50, 615, 'Cor:')
        self.relatorioOrcamento.drawString(420, 700, 'Data de Entrada:')
        self.relatorioOrcamento.drawString(420, 685, 'Data de Retirada:')
        self.relatorioOrcamento.drawString(230, 660, 'Valor:')
        self.relatorioOrcamento.drawString(230, 645, 'Defeito:')
        self.relatorioOrcamento.drawString(230, 630, 'Observação:')
        self.relatorioOrcamento.setFont("Helvetica", 10)
        self.relatorioOrcamento.drawString(260, 660, 'R$ ')

# - - - Imprime as informações - - - -
        self.relatorioOrcamento.setFont("Helvetica", 10)
        self.relatorioOrcamento.drawString(75, 700, self.idRel)
        self.relatorioOrcamento.drawString(90, 685, self.idPessoaRel)
        self.relatorioOrcamento.drawString(98, 685, self.nomeRel)
        self.relatorioOrcamento.drawString(280, 700, self.telefoneRel)
        self.relatorioOrcamento.drawString(285, 685, self.whatsappRel)
        self.relatorioOrcamento.drawString(505, 700, self.dataEntradaRel)
        self.relatorioOrcamento.drawString(505, 685, self.dataRetiradaRel)
        self.relatorioOrcamento.drawString(95, 660, self.produtoRel)
        self.relatorioOrcamento.drawString(85, 645, self.marcaRel)
        self.relatorioOrcamento.drawString(90, 630, self.modeloRel)
        self.relatorioOrcamento.drawString(75, 615, self.corRel)
        self.relatorioOrcamento.drawString(280, 660, self.valorRel)
        self.relatorioOrcamento.drawString(270, 645, self.defeitoRel)
        self.relatorioOrcamento.drawString(295, 630, self.observaroRel)

        # - - - Aviso - - - -
        self.relatorioOrcamento.setFont("Helvetica", 7)
        self.relatorioOrcamento.drawString(400, 660, 'Não cubrimos a garantia de aparelhos molhados')
        self.relatorioOrcamento.drawString(400, 650, 'Não cubrimos a garantia de Software')
        self.relatorioOrcamento.drawString(400, 640, 'Arrumanos o aparelho mediante entrada')
        self.relatorioOrcamento.drawString(400, 630, 'Aparelhos com 90 dias em loja, serão vendidos')
        self.relatorioOrcamento.drawString(400, 620, 'para amenizar o custo')


# - - - Rodapé - - - -
        self.relatorioOrcamento.setFont("Helvetica", 10)
        self.relatorioOrcamento.drawString(50, 575, 'Ass Cliente:')

# - - - Funções - - - -
        self.relatorioOrcamento.showPage() # exibe a pagina do PDF
        self.relatorioOrcamento.save() # Salva o PDF
        self.imprimir() # Função de Abrir



class Funcao():
    def limpa_Tela(self):
        self.e_id_orcamento.delete(0, END)
        self.e_id_pessoa.delete(0, END)
        self.e_cpf.delete(0, END)
        self.e_nome.delete(0, END)
        self.e_whatsapp.delete(0, END)
        self.e_telefone.delete(0, END)
        self.e_item.get()
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
        self.c_status_orcamento.delete(0, END)
        self.e_id_orcamento.focus()

    def limpa_Tela_Produto_Orcado(self):
        self.e_id_produto.delete(0, END)
        self.e_produto.delete(0, END)
        self.e_marca.delete(0, END)
        self.e_modelo.delete(0, END)
        self.e_cor.delete(0, END)
        self.e_quantidade.delete(0, END)
        self.e_valor_venda.delete(0, END)
        self.e_defeito.delete(0, END)
        self.e_observacao.delete(0, END)
        self.c_status_orcamento.delete(0, END)


    def conecta_bd(self):
        self.conn = mysql.connector.connect(host='localhost', database='gerenciador', user='root', password='admin')
        self.cursor = self.conn.cursor()

    def desconecta_bd(self):
        self.conn.close()

    def montaTabelaOrca(self):
        self.conecta_bd()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS
                orcamento(
                    id_orcamento INT PRIMARY KEY,
                    id_pessoa INT,
                    data_entrada DATE,
                    data_retirada DATE,
            CONSTRAINT FOREIGN KEY (id_pessoa) REFERENCES pessoas (id_pessoa));""")

        self.conn.commit()
        self.desconecta_bd()

    def montaTabelaProdutoOrcado(self):
        self.conecta_bd()
        self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS produto_orcado(
                    cod_orcamento INT AUTO_INCREMENT PRIMARY KEY, 
                    id_orcamento INT,
                    id_pessoa INT, 	
                    id_produto INT, 
                    quantidade INT,
                    valor_venda FLOAT,
                    defeito VARCHAR(100),
                    observacao VARCHAR(100),
                    status_orcamento VARCHAR(20),
                FOREIGN KEY (id_orcamento) REFERENCES orcamento (id_orcamento),
                FOREIGN KEY (id_pessoa) REFERENCES pessoas (id_pessoa),
                FOREIGN KEY (id_produto) REFERENCES produto (id_produto)); """)

        self.conn.commit()
        self.desconecta_bd()

    def infoVariaveis(self):
        self.id_orcamento = self.e_id_orcamento.get()
        self.id_pessoa = self.e_id_pessoa.get()
        self.cpf = self.e_cpf.get()
        self.nome = self.e_nome.get()
        self.whatsapp = self.e_whatsapp.get()
        self.telefone = self.e_telefone.get()
        self.item = self.e_item.get()
        self.id_produto = self.e_id_produto.get()
        self.produto = self.e_produto.get()
        self.marca = self.e_marca.get()
        self.modelo = self.e_modelo.get()
        self.cor = self.e_cor.get()
        self.quantidade = self.e_quantidade.get()
        self.valor = self.e_valor_venda.get()
        self.defeito = self.e_defeito.get()
        self.observacao = self.e_observacao.get()
        self.status_orcamento = self.c_status_orcamento.get()

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

        if self.e_id_orcamento.get() == '':
            messagebox.showerror(title="Orçamento", message="Orçamento precisa ser preenchido")
            pass

        else:
            self.cursor.execute("""
                INSERT INTO 
                    orcamento(
                        id_orcamento,
                        id_pessoa,
                        data_entrada, 
                        data_retirada) 
                    VALUES (%s, %s, %s, %s)""", (
                        self.id_orcamento,
                        self.id_pessoa,
                        self.dataEntradaConvertida,
                        self.dataRetiradaConvertida))

            messagebox.showinfo(title="Orçamento", message="Orçamento Gravado")

        self.conn.commit()
        self.desconecta_bd()
        self.selecionaOrcamento()

    def adicionaProdutoOrcado(self):
        self.infoVariaveis()
        if self.e_produto.get() == '' or self.e_quantidade.get() == '':
            messagebox.showerror(title="Orçamento", message="PRODUTO ou QUANTIDADE não foi preenchido")
            pass

        else:
            self.conecta_bd()
            self.cursor.execute("""
                INSERT INTO 
                    produto_orcado(
                        id_orcamento,
                        id_pessoa, 
                        id_produto, 
                        quantidade, 
                        valor_venda, 
                        defeito, 
                        observacao,
                        status_orcamento)
                 VALUES 
                        (%s, %s, %s, %s, %s, %s, %s, %s) """, (
                        self.id_orcamento,
                        self.id_pessoa,
                        self.id_produto,
                        self.quantidade,
                        self.valor,
                        self.defeito,
                        self.observacao,
                        self.status_orcamento))

            messagebox.showinfo(title="Cadastro de Pessoas", message="Cadastro realizado com sucesso")

        self.conn.commit()
        self.desconecta_bd()
        self.orcar()
        self.contaProduto()
        self.selecionaOrcamento()
        self.limpa_Tela_Produto_Orcado()

    def selecionaPessoa(self):
        self.listaOrcamentoCliente.delete(*self.listaOrcamentoCliente.get_children())
        self.conecta_bd()
        listaPe = self.cursor.execute(""" SELECT * FROM pessoas ORDER BY id_pessoa ASC; """)
        listaPe = self.cursor.fetchall()
        for i in listaPe:
            self.listaOrcamentoCliente.insert("", END, values=i)

        self.desconecta_bd()

    def selecionaProduto(self):
        self.listaOrcarmentoProduto.delete(*self.listaOrcarmentoProduto.get_children())
        self.conecta_bd()
        listaPro = self.cursor.execute(""" SELECT * FROM produto ORDER BY marca ASC; """)

        listaPro = self.cursor.fetchall()

        for i in listaPro:
            self.listaOrcarmentoProduto.insert("", END, values=i)

        self.desconecta_bd()

    def selecionaOrcamento(self):
        self.listaOrcamento.delete(*self.listaOrcamento.get_children())
        self.conecta_bd()
        lista = self.cursor.execute(f"""
            SELECT * FROM produto_orcado WHERE 
                id_orcamento = '{self.e_id_orcamento.get()}' AND id_pessoa = '{self.e_id_pessoa.get()}'; """)

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
        self.conecta_bd()
        self.listaOrcamento.selection()

        for n in self.listaOrcamento.selection():
            col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, \
            col12, col13, col14, col15, col16, col17, col18, col19 = self.listaOrcamento.item(n, 'values')

            self.e_item.delete(0, END)
            self.e_id_orcamento.delete(0, END)
            self.e_id_pessoa.delete(0, END)
            self.e_id_produto.delete(0, END)
            self.e_quantidade.delete(0, END)
            self.e_valor_venda.delete(0, END)
            self.e_defeito.delete(0, END)
            self.e_observacao.delete(0, END)
            self.c_status_orcamento.delete(0, END)

            self.e_item.insert(END, col1)
            self.e_id_orcamento.insert(END, col2)
            self.e_id_pessoa.insert(END, col3)
            self.e_id_produto.insert(END, col4)
            self.e_quantidade.insert(END, col5)
            self.e_valor_venda.insert(END, col6)
            self.e_defeito.insert(END, col7)
            self.e_observacao.insert(END, col8)
            self.e_nome.insert(END, col9)
            self.e_cpf.insert(END, col10)
            self.e_telefone.insert(END, col11)
            self.e_whatsapp.insert(END, col12)
            self.e_produto.insert(END, col13)
            self.e_marca.insert(END, col14)
            self.e_modelo.insert(END, col15)
            self.e_cor.insert(END, col16)
            self.c_status_orcamento.insert(END, col17)
            self.e_data_entrada.insert(END, col18)
            self.e_data_retirada.insert(END, col19)


    def busca_Cliente(self):
        self.conecta_bd()
        self.listaOrcarmentoCliente.delete(*self.listaOrcarmentoCliente.get_children())

        id_pessoa = self.e_id_pessoa.get()
        cpf = self.e_cpf.get()
        nome = self.e_nome.get()
        whatsapp = self.e_whatsapp.get()

        if len(id_pessoa) > 0:
            self.e_id_pessoa.insert(END, "")
            id_pessoa = self.e_id_pessoa.get()
            self.cursor.execute(f"""
                   SELECT id_pessoa, cpf, nome, whatsapp, telefone FROM 
                       pessoas
                   WHERE 
                       id_pessoa 
                   LIKE '%{id_pessoa}%' ORDER BY cpf ASC; """)

            buscaid_pessoa = self.cursor.fetchall()

            for i in buscaid_pessoa:
                self.listaOrcarmentoCliente.insert("", END, values=i)

        elif len(cpf) > 0:
            self.e_cpf.insert(END, "")
            cpf = self.e_cpf.get()
            self.cursor.execute(f"""
                   SELECT id_pessoa, cpf, nome, whatsapp, telefone FROM 
                       pessoas
                   WHERE 
                       cpf 
                   LIKE '%{cpf}%' ORDER BY cpf ASC; """ )
            buscacpf = self.cursor.fetchall()

            for i in buscacpf:
                self.listaOrcarmentoCliente.insert("", END, values=i)

        elif len(nome) > 0:
            self.e_nome.insert(END, "")
            nome = self.e_nome.get()
            self.cursor.execute(f"""
                   SELECT id_pessoa, cpf, nome, whatsapp, telefone FROM 
                       pessoas
                   WHERE 
                       nome 
                   LIKE '%{nome}%' ORDER BY cpf ASC; """)
            buscanome = self.cursor.fetchall()

            for i in buscanome:
                self.listaOrcarmentoCliente.insert("", END, values=i)


        elif len(whatsapp) > 0:
            self.e_whatsapp.insert(END, "")
            whatsapp = self.e_whatsapp.get()
            self.cursor.execute(f"""
                   SELECT id_pessoa, cpf, nome, whatsapp, telefone FROM 
                       pessoas
                   WHERE 
                       whatsapp 
                   LIKE '%{whatsapp}%' ORDER BY cpf ASC; """)

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

        if len(id_produto) > 0 or len(produto) > 0 or len(marca) > 0 or len(modelo) > 0 or len(cor) > 0:

            self.e_id_produto.insert(END, "")
            id_produto = self.e_id_produto.get()
            self.cursor.execute(f"""
                 SELECT id_produto, produto, marca, modelo, cor, valor_venda FROM 
                     produto
                 WHERE 
                     id_produto 
                 LIKE '%{id_produto}%' ORDER BY id_produto ASC; """)

            buscaid_produto = self.cursor.fetchall()

            for i in buscaid_produto:
                self.listaOrcarmentoProduto.insert("", END, values=i)

        elif len(produto) > 0:
            self.e_produto.insert(END, "")
            produto = self.e_produto.get()
            self.cursor.execute(f"""
                 SELECT id_produto, produto, marca, modelo, cor, valor_venda FROM 
                     produto LIKE '%{produto}%' 
                 AND id_produto LIKE '%{id_produto}%' 
                 AND marca LIKE '%{marca}%'
                 AND modelo LIKE '%{modelo}%'
                 AND cor LIKE '%{cor}%'
                 ORDER BY id_produto;""")

            buscaproduto = self.cursor.fetchall()

            for i in buscaproduto:
                self.listaOrcarmentoProduto.insert("", END, values=i)


        elif len(marca) > 0:
            self.e_marca.insert(END, "")
            marca = self.e_marca.get()
            self.cursor.execute(f"""
                 SELECT id_produto, produto, marca, modelo, cor, valor_venda FROM 
                     produto
                 WHERE 
                     marca 
                 LIKE '%{marca}%' ORDER BY id_produto ASC; """)

            buscamarca = self.cursor.fetchall()

            for i in buscamarca:
                self.listaOrcarmentoProduto.insert("", END, values=i)

        elif len(modelo) > 0:
            self.e_modelo.insert(END, "")
            modelo = self.e_modelo.get()
            self.cursor.execute(f"""
                 SELECT id_produto, produto, marca, modelo, cor, valor_venda FROM 
                     produto
                 modelo 
                     id_produto 
                 LIKE '%{modelo}%' ORDER BY id_produto ASC; """)

            buscamodelo = self.cursor.fetchall()

            for i in buscamodelo:
                self.listaOrcarmentoProduto.insert("", END, values=i)

            self.desconecta_bd()

        elif len(cor) > 0:
            self.e_cor.insert(END, "")
            cor = self.e_cor.get()
            self.cursor.execute(f"""
                 SELECT id_produto, produto, marca, modelo, cor, valor_venda FROM 
                     produto
                 WHERE 
                     cor 
                 LIKE '%{cor}%' ORDER BY id_produto ASC; """)

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
                    produto_orcado
                SET 
                    id_orcamento = %s,
                    id_pessoa = %s, 
                    id_produto = %s, 
                    quantidade = %s, 
                    valor_venda = %s, 
                    defeito = %s, 
                    observacao = %s,
                    status_orcamento = %s
                WHERE
                    cod_orcamento = %s """, (
                    self.id_orcamento,
                    self.id_pessoa,
                    self.id_produto,
                    self.quantidade,
                    self.valor,
                    self.defeito,
                    self.observacao,
                    self.status_orcamento,
                    self.item))

        messagebox.showinfo(title="Orçamento", message="Orçamento Foi Alterado")

        self.conn.commit()
        self.desconecta_bd()
        self.selecionaOrcamento()

    def buscaOrcamento(self):
        self.conecta_bd()
        self.listaOrcamento.delete(*self.listaOrcamento.get_children())

        id_orcamento = self.e_id_orcamento.get()

        if len(id_orcamento) > 0:
            self.e_id_orcamento.insert(END, "")
            self.cursor.execute(f"""
                   SELECT PRODUTO_ORC.COD_ORCAMENTO,
                        PRODUTO_ORC.ID_ORCAMENTO
                        , PESSOA.ID_PESSOA
                        CODIGO_PESSOA
                        , PRODUTO.ID_PRODUTO
                        , PRODUTO_ORC.QUANTIDADE
                        , PRODUTO_ORC.VALOR_VENDA
                        , PRODUTO_ORC.DEFEITO
                        , PRODUTO_ORC.OBSERVACAO
                        , PESSOA.NOME
                        , PESSOA.CPF
                        , PESSOA.TELEFONE
                        , PESSOA.WHATSAPP
                        , PRODUTO.PRODUTO
                        , PRODUTO.MARCA
                        , PRODUTO.MODELO
                        , PRODUTO.COR
                        , PRODUTO_ORC.STATUS_ORCAMENTO
                        , DATE_FORMAT(data_entrada, '%d/%m/%Y') as data_entrada 
                        , DATE_FORMAT(data_retirada, '%d/%m/%Y') as data_retirada
                        FROM PRODUTO_ORCADO PRODUTO_ORC
                        INNER JOIN PESSOAS PESSOA ON PESSOA.ID_PESSOA = PRODUTO_ORC.ID_PESSOA
                        INNER JOIN PRODUTO PRODUTO ON PRODUTO.ID_PRODUTO = PRODUTO_ORC.ID_PRODUTO
                        INNER JOIN ORCAMENTO ORC ON ORC.ID_ORCAMENTO = PRODUTO_ORC.ID_ORCAMENTO
                        WHERE ORC.ID_ORCAMENTO = {id_orcamento}
                   ORDER BY cpf ASC; """)

            buscaOrcam = self.cursor.fetchall()

            for i in buscaOrcam:
                self.listaOrcamento.insert("", END, values=i)

    def orcar(self):
        self.conecta_bd()
        self.cursor.execute(f""" 
            SELECT SUM(valor_venda) 
            FROM produto_orcado WHERE 
                id_orcamento = '{self.e_id_orcamento.get()}'
                AND id_pessoa = '{self.e_id_pessoa.get()}'; """)

        somaValores = self.cursor.fetchone()
        self.somaDeValores = somaValores[0]
        self.e_valor.delete(0, END)
        self.e_valor.insert(0, self.somaDeValores)
        self.desconecta_bd()

    def calcula_desconto(self, valor):
        if len(valor) > 0:
            self.valor2 = float(self.somaDeValores) - float(valor)
        else:
            self.valor2 = float(self.somaDeValores) - 0
        self.e_valor.delete(0, END)
        self.e_valor.insert(0, self.valor2)

    def retorna_desconto(self, var, index, mode):
        self.desconto = self.callback_desconto.get()
        self.calcula_desconto(self.desconto)

    def desconto(self):
        self.valor_orcamento = float(self.e_valor.get())
        self.desconto = self.e_desconto.get()
        self.desconto = float(self.desconto)
        self.valor = self.e_valor.get()
        self.valor = float(self.valor)
        self.valorDoDesconto = self.valor - self.desconto

    def contaProduto(self):
        self.conecta_bd()
        self.cursor.execute(f"""
            SELECT COUNT(cod_orcamento) FROM produto_orcado WHERE 
                id_orcamento = '{self.e_id_orcamento.get()}'
                AND id_pessoa = '{self.e_id_pessoa.get()}'; """)

        contador = self.cursor.fetchall()

        self.e_quantidadeItens.delete(0, END)
        self.e_quantidadeItens.insert(0, contador)
        self.desconecta_bd()

    def enviarAvisoNoWhatsapp(self):

        self.conecta_bd()
        selecionaNumeroWhatsapp = self.cursor.execute(f""" 
            SELECT whatsapp FROM pessoas WHERE id_pessoa = '{self.e_id_pessoa.get()}'; """)

        selecionaNumeroWhatsapp = self.cursor.fetchone()

        self.aviso = kt.sendwhatmsg_instantly(
            f'+55{selecionaNumeroWhatsapp}',
            'SEGAT - Sistema Gerenciador de Assistência Técnica Avisa.'
            'Seu Celular já está Pronto!')
        self.conn.commit()
        self.desconecta_bd()

    def vender(self):
        orcamento.destroy()
        call(["python", "Tela_Venda.py"])


class Aplicacao_Orcamento(Funcao, Relatorio):
    def __init__(self):
        self.orcamento = orcamento
        self.tela_orcamento()
        self.frames_Orcamento()
        self.labels_entry()
        self.botoes()
        self.limpa_Tela()
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
        self.orcamento.iconbitmap("C:/Users/Edinho/PycharmProjects/Meu_TCC/Logo/segatIcone.ico")

    def frames_Orcamento(self):
        self.frameSuperior = Frame(self.orcamento, bg=co6, highlightbackground=co5, highlightthickness=6)
        self.frameSuperior.place(x=5, y=5, height=310, width=1085)

        self.frameGridCliente = Frame(self.orcamento, bg=co10, highlightbackground=co5, highlightthickness=6)
        self.frameGridCliente.place(x=5, y=330, height=105, width=400)

        self.frameGridProduto = Frame(self.orcamento, bg=co10, highlightbackground=co5, highlightthickness=6)
        self.frameGridProduto.place(x=410, y=330, height=105, width=680)

        self.frameGridOrcamento = Frame(self.orcamento, bg=co10, highlightbackground=co5, highlightthickness=6)
        self.frameGridOrcamento.place(x=5, y=450, height=155, width=1085)

        self.frameInferior = Frame(self.orcamento, bg=co6, highlightbackground=co5, highlightthickness=6)
        self.frameInferior.place(x=5, y=620, height=70, width=1085)

    # - - - - - - - Frame Superior- - - - - - -

    def labels_entry(self):
        # - - - - - - - Pessoas - - - - - -
        self.l_id_orcamento = Label(self.frameSuperior, text="Orçamento:", font=("Courier", 13, "italic", "bold"), bg=co6, fg=co10)
        self.l_id_orcamento.place(x=50, y=5)
        self.e_id_orcamento = Entry(self.frameSuperior, width=45, justify='left', relief='raised', bg=co0, fg=co10)
        self.e_id_orcamento.place(x=155, y=5)

        self.l_id_pessoa = Label(self.frameSuperior, text="Código Cliente:", font=("Courier", 13, "italic", "bold"), bg=co6, fg=co10)
        self.l_id_pessoa.place(x=0, y=30)
        self.e_id_pessoa = Entry(self.frameSuperior, width=45, justify='left', relief='raised', bg=co0, fg=co10)
        self.e_id_pessoa.place(x=155, y=30)

        self.l_cpf = Label(self.frameSuperior, text="CPF:", font=("Courier", 13, "italic", "bold"), bg=co6, fg=co10)
        self.l_cpf.place(x=110, y=55)
        self.e_cpf = Entry(self.frameSuperior, width=45, justify='left', relief='raised', bg=co0, fg=co10)
        self.e_cpf.place(x=155, y=55)

        self.l_nome = Label(self.frameSuperior, text="Nome:", font=("Courier", 13, "italic", "bold"), bg=co6, fg=co10)
        self.l_nome.place(x=100, y=80)
        self.e_nome = Entry(self.frameSuperior, width=45, justify='left', relief='raised', bg=co0, fg=co10)
        self.e_nome.place(x=155, y=80)

        self.l_whatsapp = Label(self.frameSuperior, text="Whatsapp:", font=("Courier", 13, "italic", "bold"), bg=co6, fg=co10)
        self.l_whatsapp.place(x=60, y=105)
        self.e_whatsapp = Entry(self.frameSuperior, width=45, justify='left', relief='raised', bg=co0, fg=co10)
        self.e_whatsapp.place(x=155, y=105)

        self.l_telefone = Label(self.frameSuperior, text="Telefone:", font=("Courier", 13, "italic", "bold"), bg=co6, fg=co10)
        self.l_telefone.place(x=60, y=130)
        self.e_telefone = Entry(self.frameSuperior, width=45, justify='left', relief='raised', bg=co0, fg=co10)
        self.e_telefone.place(x=155, y=130)

        self.l_data_entrada = Label(self.frameSuperior, text="Entrada:", font=("Courier", 13, "italic", "bold"), bg=co6, fg=co10)
        self.l_data_entrada.place(x=70, y=155)
        self.e_data_entrada = DateEntry(self.frameSuperior, width=42, justify='left', relief='raised', locale="pt_br")
        self.e_data_entrada.place(x=155, y=155)

        self.l_data_retirada = Label(self.frameSuperior, text="Retirada:", font=("Courier", 13, "italic", "bold"), bg=co6, fg=co10)
        self.l_data_retirada.place(x=60, y=180)
        self.e_data_retirada = DateEntry(self.frameSuperior, width=42, justify='left', relief='raised', locale="pt_br")
        self.e_data_retirada.place(x=155, y=180)

        self.l_status_orcamento = Label(self.frameSuperior, text="Status:", font=("Courier", 13, "italic", "bold"),
                                        bg=co6, fg=co10)
        self.l_status_orcamento.place(x=80, y=205)
        self.c_status_orcamento = Combobox(self.frameSuperior, width=42)
        self.c_status_orcamento["values"] = ("Orçamento", "Aprovado", "Retirado")
        self.c_status_orcamento.set("")
        self.c_status_orcamento.place(x=155, y=205)

        # - - - - - - - Produtos - - - - - -
        self.l_item = Label(self.frameSuperior, text="Item:", font=("Courier", 13, "italic", "bold"), bg=co6, fg=co10)
        self.l_item.place(x=645, y=5)
        self.e_item = Entry(self.frameSuperior, width=45, justify='left', relief='raised', bg=co0, fg=co10)
        self.e_item.place(x=700, y=5)


        self.l_id_produto = Label(self.frameSuperior, text="Id Produdo:", font=("Courier", 13, "italic", "bold"), bg=co6, fg=co10)
        self.l_id_produto.place(x=585, y=30)
        self.e_id_produto = Entry(self.frameSuperior, width=45, justify='left', relief='raised', bg=co0, fg=co10)
        self.e_id_produto.place(x=700, y=30)

        self.l_produto = Label(self.frameSuperior, text="Produdo:", font=("Courier", 13, "italic", "bold"), bg=co6, fg=co10)
        self.l_produto.place(x=615, y=55)
        self.e_produto = Entry(self.frameSuperior, width=45, justify='left', relief='raised', bg=co0, fg=co10)
        self.e_produto.place(x=700, y=55)

        self.l_marca = Label(self.frameSuperior, text="Marca:", font=("Courier", 13, "italic", "bold"), bg=co6, fg=co10)
        self.l_marca.place(x=635, y=80)
        self.e_marca = Entry(self.frameSuperior, width=45, justify='left', relief='raised', bg=co0, fg=co10)
        self.e_marca.place(x=700, y=80)

        self.l_modelo = Label(self.frameSuperior, text="Modelo:", font=("Courier", 13, "italic", "bold"), bg=co6, fg=co10)
        self.l_modelo.place(x=625, y=105)
        self.e_modelo = Entry(self.frameSuperior, width=45, justify='left', relief='raised', bg=co0, fg=co10)
        self.e_modelo.place(x=700, y=105)

        self.l_cor = Label(self.frameSuperior, text="Cor:", font=("Courier", 13, "italic", "bold"), bg=co6, fg=co10)
        self.l_cor.place(x=655, y=130)
        self.e_cor = Entry(self.frameSuperior, width=45, justify='left', relief='raised', bg=co0, fg=co10)
        self.e_cor.place(x=700, y=130)

        self.l_quantidade = Label(self.frameSuperior, text="Quantidade:", font=("Courier", 13, "italic", "bold"), bg=co6, fg=co10)
        self.l_quantidade.place(x=585, y=155)
        self.e_quantidade = Entry(self.frameSuperior, width=45, justify='left', relief='raised', bg=co0, fg=co10)
        self.e_quantidade.place(x=700, y=155)

        self.l_valor_venda = Label(self.frameSuperior, text="Valor:", font=("Courier", 13, "italic", "bold"), bg=co6, fg=co10)
        self.l_valor_venda.place(x=635, y=180)
        self.e_valor_venda = Entry(self.frameSuperior, width=45, justify='left', relief='raised', bg=co0, fg=co10)
        self.e_valor_venda.place(x=700, y=180)

        self.l_defeito = Label(self.frameSuperior, text="Defeito:", font=("Courier", 13, "italic", "bold"), bg=co6, fg=co10)
        self.l_defeito.place(x=615, y=205)
        self.e_defeito = Entry(self.frameSuperior, width=45, justify='left', relief='raised', bg=co0, fg=co10)
        self.e_defeito.place(x=700, y=205)

        self.l_observacao = Label(self.frameSuperior, text="Observações:", font=("Courier", 13, "italic", "bold"), bg=co6, fg=co10)
        self.l_observacao.place(x=575, y=230)
        self.e_observacao = Entry(self.frameSuperior, width=45, justify='left', relief='raised', bg=co0, fg=co10)
        self.e_observacao.place(x=700, y=230)

        # - - - - - - - Frame Inferior - - - - - - -

        self.l_quantidadeItens = Label(self.frameInferior, text="Quantidade de Itens:", font=("Courier", 13, "italic", "bold"), bg=co6, fg=co10)
        self.l_quantidadeItens.place(x=10, y=20)
        self.e_quantidadeItens = Entry(self.frameInferior, width=35, justify='left', relief='solid', bg=co0, fg=co10)
        self.e_quantidadeItens.place(x=215, y=20, width=80)

        self.l_desconto = Label(self.frameInferior, text="Desconto:", font=("Courier", 13, "italic", "bold"), bg=co6, fg=co10)
        self.l_desconto.place(x=325, y=20)

        self.callback_desconto = StringVar()
        self.e_desconto = Entry(self.frameInferior, textvariable=self.callback_desconto, width=35, justify='left', relief='solid', bg=co0, fg=co10)
        self.callback_desconto.trace_variable("w", self.retorna_desconto)
        self.e_desconto.place(x=420, y=20, width=80)

        self.l_valor = Label(self.frameInferior, text="Valor Total:", font=("Courier", 13, "italic", "bold"), bg=co6, fg=co10)
        self.l_valor.place(x=505, y=20)
        self.e_valor = Entry(self.frameInferior, width=35, justify='left', relief='solid', bg=co0, fg=co10)
        self.e_valor.place(x=630, y=20, width=80)

# - - - - - - - Botões - - - - - - -

    def botoes(self):
# - - - - - - - Botões do Orçamento - - - - - - -
        self.b_procurarCliente = Button(self.frameSuperior, text="Procurar", command=self.busca_Cliente,
                                        font=('Courier 9 italic bold'), bg=co1, fg=co10, relief=RAISED, overrelief=RIDGE)
        self.b_procurarCliente.place(x=440, y=5, height=25, width=70)

        self.b_adicionarCliente = Button(self.frameSuperior, text="Gravar", command=self.adicionaOrcamento,
                                         font=("Courier", 13, "italic", "bold"), bg=co7, fg=co10, relief=RAISED, overrelief=RIDGE)
        self.b_adicionarCliente.place(x=330, y=255, height=40, width=100)

# - - - - - - - Botões do Produto - - - - - - -
        self.b_procurarProduto = Button(self.frameSuperior, text="Procurar", command=self.busca_Produto,
                                        font=('Courier 9 italic bold'), bg=co1, fg=co10, relief=RAISED, overrelief=RIDGE)
        self.b_procurarProduto.place(x=990, y=5, height=25, width=70)

        self.b_limpar = Button(self.frameSuperior, text="Limpar", command=self.limpa_Tela,
                               font=("Courier", 13, "italic", "bold"), bg=co1, fg=co10, relief=RAISED, overrelief=RIDGE)
        self.b_limpar.place(x=220, y=255, height=40, width=100)

        self.b_imprimir = Button(self.frameSuperior, text="Imprimir", command=self.geraRelatorio,
                                 font=("Courier", 13, "italic", "bold"), bg=co1, fg=co10, relief=RAISED, overrelief=RIDGE)
        self.b_imprimir.place(x=520, y=255, height=40, width=100)

        self.b_procurarOrcamento = Button(self.frameSuperior, text="Procurar", command=self.buscaOrcamento,
                                 font=("Courier", 13, "italic", "bold"), bg=co1, fg=co10, relief=RAISED, overrelief=RIDGE)
        self.b_procurarOrcamento.place(x=630, y=255, height=40, width=100)

        self.b_adicionar = Button(self.frameSuperior, text="Adicionar", command=self.adicionaProdutoOrcado,
                                  font=("Courier", 13, "italic", "bold"), bg=co7, fg=co10, relief=RAISED, overrelief=RIDGE)
        self.b_adicionar.place(x=740, y=255, height=40, width=100)

        self.b_alterar = Button(self.frameSuperior, text="Alterar", command=self.alteraOrcamento,
                                font=("Courier", 13, "italic", "bold"), bg=co8, fg=co10, relief=RAISED, overrelief=RIDGE)
        self.b_alterar.place(x=850, y=255, height=40, width=100)

        self.b_avisoWhatsapp = Button(self.frameSuperior, text="Avisar", command=self.enviarAvisoNoWhatsapp,
                                      font=("Courier", 13, "italic", "bold"), bg=co8, fg=co10, relief=RAISED, overrelief=RIDGE)
        self.b_avisoWhatsapp.place(x=960, y=255, height=40, width=100)

# - - - - - - - Botão Frame Inferior - - - - - - -
        self.b_vender = Button(self.frameInferior, text="Vender", command=self.vender,
                              font=("Courier", 13, "italic", "bold"), bg=co7, fg=co10, relief=RAISED, overrelief=RIDGE)
        self.b_vender.place(x=960, y=10, height=40, width=100)

# - - - - - - - Método para Criar os balões - - - - - - -
        self.balaoProcurarCliente = tix.Balloon(self.frameInferior)
        self.balaoProcurarCliente.bind_widget(self.b_procurarCliente, balloonmsg="Procura o Cliente Cadastrado")

        self.balaoProcurarProduto = tix.Balloon(self.frameInferior)
        self.balaoProcurarProduto.bind_widget(self.b_procurarProduto, balloonmsg="Procura as Informações do Produto")

        self.balaoGravar = tix.Balloon(self.frameInferior)
        self.balaoGravar.bind_widget(self.b_adicionarCliente, balloonmsg="Grava as Informações do Cliente na OS")

        self.balaoAdicionar = tix.Balloon(self.frameInferior)
        self.balaoAdicionar.bind_widget(self.b_adicionar, balloonmsg="Adicionar as Informações do Produto na OS")

        self.balaoVender = tix.Balloon(self.frameInferior)
        self.balaoVender.bind_widget(self.b_vender, balloonmsg="Abre a Tela de Vendas e Busca as informações do Cliente e do Produto")


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
                                                    "col4", "col5", "col6", "col7"))
        self.listaOrcamento.heading("#0", text="")
        self.listaOrcamento.heading("#1", text="Item")
        self.listaOrcamento.heading("#2", text="ID Orçamento")
        self.listaOrcamento.heading("#3", text="ID Cliente")
        self.listaOrcamento.heading("#4", text="ID Produto")
        self.listaOrcamento.heading("#5", text="Quantidade")
        self.listaOrcamento.heading("#6", text="Valor")
        self.listaOrcamento.heading("#7", text="Defeito")
        self.listaOrcamento.heading("#8", text="Observação")

        self.listaOrcamento.column("#0", anchor='center', width=1)
        self.listaOrcamento.column("#1", anchor='center', width=60)
        self.listaOrcamento.column("#2", anchor='center', width=60)
        self.listaOrcamento.column("#3", anchor='center', width=60)
        self.listaOrcamento.column("#4", anchor='center', width=60)
        self.listaOrcamento.column("#5", anchor='center', width=60)
        self.listaOrcamento.column("#6", anchor='center', width=60)
        self.listaOrcamento.column("#7", anchor='center', width=60)
        self.listaOrcamento.column("#8", anchor='center', width=60)


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
