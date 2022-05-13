from tkinter import *
from tkinter import ttk
from tkinter import ttk
from tkinter import ttk
from tkinter import ttk
from tkinter import messagebox
from tkinter import tix
from tkinter import font
from tkcalendar import Calendar, DateEntry
import mysql.connector

database = "gerenciador.db"

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

# - - janela Cadastro de Pessoas - -

orcamento = Tk()

class Funcao():
    def conecta_bd(self):
        self.conn = mysql.connector.connect(host='localhost', database='gerenciador', user='root', password='admin')
        self.cursor = self.conn.cursor()

    def desconecta_bd(self):
        self.conn.close()

    def montatabelas(self):
        self.conecta_bd()
        self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS orcamentoteste(
                    id_orcamento INTEGER AUTO_INCREMENT,
                    id_cliente INTEGER NOT NULL,
                    cpf INT(11) NOT NULL,
                    nome VARCHAR(10) NOT NULL,
                    whatsapp INT(10)  NOT NULL,
                    produto VARCHAR(100) NOT NULL,
                    marca VARCHAR(100) NOT NULL,
                    modelo VARCHAR(100) NOT NULL,
                    cor VARCHAR(100),
                    defeito VARCHAR(100),
                    observacao VARCHAR(200),
                PRIMARY KEY (id_orcamento)
            );
        """)

        self.conn.commit()
        self.desconecta_bd()

    def adiciona_Orcamento(self):
        self.conecta_bd()
        self.cursor.execute("""
            INSERT INTO
                orcamento 
                    (id_pessoa, id_produto, marca, modelo, cor, valor_venda, estoque) 
            VALUES 
                    (%s, %s, %s, %s, %s, %s, %s);""",
                    (self.id_pessoa, self.id_produto, self.marca, self.modelo, self.cor, self.valor_venda))

        messagebox.showinfo(title="Cadastrado de Produto", message="Produto Cadastro com Sucesso")

        self.conn.commit()
        self.desconecta_bd()
        self.select_Produto()
        self.limpa_tela()

    def select_Pessoa(self):
        self.lista_orcarmento.delete(*self.lista_orcarmento.get_children())
        self.conecta_bd()
        listaPe = self.cursor.execute("""
             SELECT * FROM
                 cad_pessoas 
             ORDER BY 
                 id_pessoas ASC; """)

        listaPe = self.cursor.fetchall()

        for i in listaPe:
            self.lista_orcarmento.insert("", END, values=i)

        self.desconecta_bd()

    def duplo_Clique(self, event):
        self.limpa_Tela()
        self.lista_orcarmento.selection()

        for n in self.lista_orcarmento.selection():
            col1, col2, col3 = self.lista_orcarmento.item(n, 'values')
            self.e_cpf.insert(END, col1)
            self.e_nome.insert(END, col2)
            self.e_whatsapp.insert(END, col3)

    def busca_Cliente(self):
        self.conecta_bd()
        self.lista_orcarmento.delete(*self.lista_orcarmento.get_children())

        cpf = self.e_cpf.get()
        nome = self.e_nome.get()
        whatsapp = self.e_whatsapp.get()

        if len(cpf) > 0:
            self.e_cpf.insert(END, "%")
            cpf = self.e_cpf.get()
            self.cursor.execute("""
                   SELECT cpf, nome, whatsapp FROM 
                       cad_pessoas
                   WHERE 
                       cpf 
                   LIKE '%s' ORDER BY cpf ASC""" % cpf, )

            buscacpf = self.cursor.fetchall()

            for i in buscacpf:
                self.lista_orcarmento.insert("", END, values=i)

        elif len(nome) > 0:
            self.e_nome.insert(END, "%")
            nome = self.e_nome.get()
            self.cursor.execute("""
                   SELECT cpf, nome, whatsapp FROM 
                       cad_pessoas 
                   WHERE 
                       nome 
                   LIKE '%s' ORDER BY nome ASC""" % nome, )
            buscanome = self.cursor.fetchall()

            for i in buscanome:
                self.lista_orcarmento.insert("", END, values=i)

        elif len(whatsapp) > 0:
            self.e_whatsapp.insert(END, "%")
            id_pessoas = self.e_whatsapp.get()
            self.cursor.execute("""
                   SELECT cpf, nome, whatsapp FROM 
                       cad_pessoas 
                   WHERE 
                       id_pessoas 
                   LIKE '%s' ORDER BY id_pessoas ASC""" % id_pessoas, )

            buscaWhatsapp = self.cursor.fetchall()

            for i in buscaWhatsapp:
                self.lista_orcarmento.insert("", END, values=i)

        self.desconecta_bd()


class Aplicacao_Orcamento(Funcao):
    def __init__(self):
        self.orcamento = orcamento
        self.tela_orcamento()
        self.frames_Orcamento()
        self.labels_entry()
        self.botoes()
        self.grid_orcamento()
        self.montatabelas()

        self.orcamento.mainloop()

    def tela_orcamento(self):
        self.orcamento.title("Orçamento")
        self.orcamento.config(bg=co3)
        self.orcamento.geometry("1095x680+263+0")

    def frames_Orcamento(self):
        self.frame_superior = Frame(self.orcamento, bg=co4, highlightbackground=co5, highlightthickness=6)
        self.frame_superior.place(x=10, y=10, height=250, width=1075)

        self.frame_grid = Frame(self.orcamento, bg=co10, highlightbackground=co5, highlightthickness=6)
        self.frame_grid.place(x=10, y=230, height=240, width=1075)

        self.frame_inferior = Frame(self.orcamento, bg=co4, highlightbackground=co5, highlightthickness=6)
        self.frame_inferior.place(x=10, y=500, height=160, width=1075)

    def labels_entry(self):
        # - - Frame Superior - -
        self.l_id_orcamento = Label(self.frame_superior, text="Orçamento:", font=("Courier", 13, "italic", "bold"),
                                    bg=co4, fg=co10)
        self.l_id_orcamento.place(x=5, y=10)
        self.e_id_orcamento = Entry(self.frame_superior, width=45, justify='left', relief='raised', bg=co2, fg=co10)
        self.e_id_orcamento.place(x=110, y=10)

        self.l_id_cliente = Label(self.frame_superior, text="Código Cliente:", font=("Courier", 13, "italic", "bold"),
                                  bg=co4, fg=co10)
        self.l_id_cliente.place(x=5, y=35)
        self.e_id_cliente = Entry(self.frame_superior, width=45, justify='left', relief='raised', bg=co2, fg=co10)
        self.e_id_cliente.place(x=110, y=35)

        self.l_cpf = Label(self.frame_superior, text="Cpf:", font=("Courier", 13, "italic", "bold"), bg=co4, fg=co10)
        self.l_cpf.place(x=65, y=60)
        self.e_cpf = Entry(self.frame_superior, width=45, justify='left', relief='raised', bg=co2, fg=co10)
        self.e_cpf.place(x=110, y=60)

        self.l_nome = Label(self.frame_superior, text="Nome:", font=("Courier", 13, "italic", "bold"), bg=co4, fg=co10)
        self.l_nome.place(x=55, y=85)
        self.e_nome = Entry(self.frame_superior, width=45, justify='left', relief='raised', bg=co2, fg=co10)
        self.e_nome.place(x=110, y=85)

        self.l_whatsapp = Label(self.frame_superior, text="Whatsapp:", font=("Courier", 13, "italic", "bold"), bg=co4,
                                fg=co10)
        self.l_whatsapp.place(x=15, y=110)
        self.e_whatsapp = Entry(self.frame_superior, width=45, justify='left', relief='raised', bg=co2, fg=co10)
        self.e_whatsapp.place(x=110, y=110)

        self.l_produto = Label(self.frame_superior, text="Produto:", font=("Courier", 13, "italic", "bold"), bg=co4,
                               fg=co10)
        self.l_produto.place(x=25, y=135)
        self.e_produto = Entry(self.frame_superior, width=45, justify='left', relief='raised', bg=co2, fg=co10)
        self.e_produto.place(x=110, y=135)

        self.l_marca = Label(self.frame_superior, text="Marca:", font=("Courier", 13, "italic", "bold"), bg=co4,
                             fg=co10)
        self.l_marca.place(x=45, y=160)
        self.e_marca = Entry(self.frame_superior, width=45, justify='left', relief='raised', bg=co2, fg=co10)
        self.e_marca.place(x=110, y=160)

        self.l_modelo = Label(self.frame_superior, text="Modelo:", font=("Courier", 13, "italic", "bold"), bg=co4,
                              fg=co10)
        self.l_modelo.place(x=35, y=185)
        self.e_modelo = Entry(self.frame_superior, width=45, justify='left', relief='raised', bg=co2, fg=co10)
        self.e_modelo.place(x=110, y=185)

        self.l_cor = Label(self.frame_superior, text="Cor:", font=("Courier", 13, "italic", "bold"), bg=co4, fg=co10)
        self.l_cor.place(x=65, y=210)
        self.e_cor = Entry(self.frame_superior, width=45, justify='left', relief='raised', bg=co2, fg=co10)
        self.e_cor.place(x=110, y=210)

        self.l_defeito = Label(self.frame_superior, text="Defeito:", font=("Courier", 13, "italic", "bold"), bg=co4,
                               fg=co10)
        self.l_defeito.place(x=540, y=10)
        self.e_defeito = Entry(self.frame_superior, width=45, justify='left', relief='solid', bg=co2, fg=co10)
        self.e_defeito.place(x=625, y=10)

        self.l_observacao = Label(self.frame_superior, text="Obersvações:", font=("Courier", 13, "italic", "bold"),
                                  bg=co4, fg=co10)
        self.l_observacao.place(x=500, y=35)
        self.e_observacao = Entry(self.frame_superior, width=45, justify='left', relief='solid', bg=co2, fg=co10)
        self.e_observacao.place(x=625, y=35)

# - - Frame Inferior - -
        self.l_quantidade = Label(self.frame_inferior, text="Quantidade de Itens:", font=("Courier", 13, "italic", "bold"), bg=co4, fg=co10)
        self.l_quantidade.place(x=10, y=25)
        self.e_quantidade = Entry(self.frame_inferior, width=45, justify='left', relief='solid', bg=co2, fg=co10)
        self.e_quantidade.place(x=215, y=25)

        self.l_desconto = Label(self.frame_inferior, text="Desconto:", font=("Courier", 13, "italic", "bold"), bg=co4, fg=co10)
        self.l_desconto.place(x=120, y=50)
        self.e_desconto= Entry(self.frame_inferior, width=45, justify='left', relief='solid', bg=co2, fg=co10)
        self.e_desconto.place(x=215, y=50)

        self.l_valor = Label(self.frame_inferior, text="Valor Total:", font=("Courier", 13, "italic", "bold"), bg=co4, fg=co10)
        self.l_valor.place(x=90, y=75)
        self.e_valor = Entry(self.frame_inferior, width=45, justify='left', relief='solid', bg=co2, fg=co10)
        self.e_valor.place(x=215, y=75)

    def botoes(self):

        # - - Frame Inferior - -
        self.b_limpar = Button(self.frame_superior, text="Limpar", width=10, font=('Ivy 8 bold'), bg=co6, fg=co2, relief=RAISED, overrelief=RIDGE)
        self.b_limpar.place(x=480, y=130, height=40, width=100)

        self.b_procurar = Button(self.frame_superior, text="Procurar", width=10, font=('Ivy 8 bold'), bg=co6, fg=co2, relief=RAISED, overrelief=RIDGE)
        self.b_procurar.place(x=590, y=130, height=40, width=100)

        self.b_procurarCliente = Button(self.frame_superior, text="Procurar", command=self.busca_Cliente, width=10, font=('Ivy 6 bold'), bg=co6, fg=co2, relief=RAISED, overrelief=RIDGE)
        self.b_procurarCliente.place(x=390, y=35, height=20, width=60)

        self.b_procurarProduto = Button(self.frame_superior, text="Procurar", command=self.busca_Produto, width=10, font=('Ivy 6 bold'), bg=co6, fg=co2, relief=RAISED, overrelief=RIDGE)
        self.b_procurarProduto.place(x=390, y=110, height=20, width=60)

        self.b_adicionar = Button(self.frame_superior, text="Adicionar",  width=10, font=('Ivy 8 bold'), bg=co7, fg=co2, relief=RAISED, overrelief=RIDGE)
        self.b_adicionar.place(x=700, y=130, height=40, width=100)

        self.b_alterar = Button(self.frame_superior, text="Alterar",  width=10, font=('Ivy 8 bold'), bg=co8, fg=co2, relief=RAISED, overrelief=RIDGE)
        self.b_alterar.place(x=810, y=130, height=40, width=100)

        self.b_excluir = Button(self.frame_superior, text="Excluir",  width=10, font=('Ivy 8 bold'), bg=co9, fg=co2, relief=RAISED, overrelief=RIDGE)
        self.b_excluir.place(x=920, y=130, height=40, width=100)

    def grid_orcamento(self):
        self.lista_orcarmento = ttk.Treeview(self.frame_grid, columns=("col0", "col1", "col2", "col3", "col4", "col5", "col6", "col7"))
        self.lista_orcarmento.heading("#0", text="")
        self.lista_orcarmento.heading("#1", text="CPF")
        self.lista_orcarmento.heading("#2", text="Nome")
        self.lista_orcarmento.heading("#3", text="Whatsapp")
        self.lista_orcarmento.heading("#4", text="Produto")
        self.lista_orcarmento.heading("#5", text="Marca")
        self.lista_orcarmento.heading("#6", text="Modelo")
        self.lista_orcarmento.heading("#7", text="Cor")
        self.lista_orcarmento.heading("#8", text="Valor")

        self.lista_orcarmento.column("#0", anchor='center', width=5)
        self.lista_orcarmento.column("#1", anchor='center', width=100)
        self.lista_orcarmento.column("#2", anchor='center', width=132)
        self.lista_orcarmento.column("#3", anchor='center', width=132)
        self.lista_orcarmento.column("#4", anchor='center', width=132)
        self.lista_orcarmento.column("#5", anchor='center', width=132)
        self.lista_orcarmento.column("#6", anchor='center', width=132)
        self.lista_orcarmento.column("#7", anchor='center', width=132)
        self.lista_orcarmento.column("#8", anchor='center', width=132)

        self.lista_orcarmento.place(x=10, y=10, height=160, width=1035)

        self.barra_vertical = ttk.Scrollbar(self.frame_grid, orient='vertical', command=self.lista_orcarmento.yview)
        self.barra_vertical.place(x=1048, y=0, height=189, width=15)

        self.barra_horizontal = ttk.Scrollbar(self.frame_grid, orient='horizontal', command=self.lista_orcarmento.xview)
        self.barra_horizontal.place(x=0, y=174, height=15, width=1050)

        self.lista_orcarmento.configure(yscrollcommand=self.barra_vertical.set, xscrollcommand=self.barra_horizontal.set)

        self.lista_orcarmento.bind("<Double-1>", self.duplo_Clique)
Aplicacao_Orcamento()