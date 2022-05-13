from tkinter import *
from tkinter import ttk
from tkinter import ttk
from tkinter import ttk
from tkinter import ttk
from tkinter import messagebox
from tkinter import tix
from tkinter import font
import mysql.connector
from tkcalendar import Calendar, DateEntry

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

venda = Tk()

class Aplicacao_Venda():
    def __init__(self):
        self.venda = venda
        self.tela_venda()
        self.frames_venda()
        self.labels_entry()
        self.botoes()
        self.grid_venda()

        self.venda.mainloop()

    def tela_venda(self):
        self.venda.title("Vendas")
        self.venda.config(bg=co3)
        self.venda.geometry("1095x680+263+0")

    def frames_venda(self):
        self.frame_superior = Frame(self.venda, bg=co4, highlightbackground=co5, highlightthickness=6)
        self.frame_superior.place(x=10, y=10, height=200, width=1075)

        self.frame_grid = Frame(self.venda, bg=co10, highlightbackground=co5, highlightthickness=6)
        self.frame_grid.place(x=10, y=230, height=200, width=1075)

        self.frame_inferior = Frame(self.venda, bg=co4, highlightbackground=co5, highlightthickness=6)
        self.frame_inferior.place(x=10, y=500, height=160, width=1075)

    def labels_entry(self):
        # - - Frame Superior - -

        self.l_orcamento = Label(self.frame_superior, text="Orçamento:", font=("Courier", 13, "italic", "bold"), bg=co4, fg=co10)
        self.l_orcamento.place(x=5, y=10)
        self.e_orcamento = Entry(self.frame_superior, width=45, justify='left', relief='raised', bg=co2, fg=co10)
        self.e_orcamento.place(x=110, y=10)

        self.l_venda = Label(self.frame_superior, text="Venda:", font=("Courier", 13, "italic", "bold"), bg=co4, fg=co10)
        self.l_venda.place(x=45, y=35)
        self.e_venda = Entry(self.frame_superior, width=45, justify='left', relief='raised', bg=co2, fg=co10)
        self.e_venda.place(x=110, y=35)

        self.l_nome = Label(self.frame_superior, text="Nome:", font=("Courier", 13, "italic", "bold"), bg=co4, fg=co10)
        self.l_nome.place(x=55, y=60)
        self.e_nome = Entry(self.frame_superior, width=45, justify='left', relief='raised', bg=co2, fg=co10)
        self.e_nome.place(x=110, y=60)

        self.l_whatsapp = Label(self.frame_superior, text="Whatsapp:", font=("Courier", 13, "italic", "bold"), bg=co4, fg=co10)
        self.l_whatsapp.place(x=15, y=85)
        self.e_whatsapp = Entry(self.frame_superior, width=45, justify='left', relief='raised', bg=co2, fg=co10)
        self.e_whatsapp.place(x=110, y=85)

        self.l_aparelho = Label(self.frame_superior, text="Aparelho:", font=("Courier", 13, "italic", "bold"), bg=co4, fg=co10)
        self.l_aparelho.place(x=15, y=110)
        self.e_aparelho = Entry(self.frame_superior, width=45, justify='left', relief='raised', bg=co2, fg=co10)
        self.e_aparelho.place(x=110, y=110)

        self.l_marca = Label(self.frame_superior, text="Marca:", font=("Courier", 13, "italic", "bold"), bg=co4, fg=co10)
        self.l_marca.place(x=45, y=135)
        self.e_marca = Entry(self.frame_superior, width=45, justify='left', relief='raised', bg=co2, fg=co10)
        self.e_marca.place(x=110, y=135)

        self.l_cor = Label(self.frame_superior, text="Cor:", font=("Courier", 13, "italic", "bold"), bg=co4, fg=co10)
        self.l_cor.place(x=65, y=160)
        self.e_cor = Entry(self.frame_superior, width=45, justify='left', relief='raised', bg=co2, fg=co10)
        self.e_cor.place(x=110, y=160)

        self.l_defeito = Label(self.frame_superior, text="Defeito:", justify='right', font=("Courier", 13, "italic", "bold"), bg=co4, fg=co10)
        self.l_defeito.place(x=540, y=10)
        self.e_defeito = Entry(self.frame_superior, width=45, justify='left', relief='solid', bg=co2, fg=co10)
        self.e_defeito.place(x=625, y=10)

        self.l_observacoes = Label(self.frame_superior, text="Obersvações:", font=("Courier", 13, "italic", "bold"),
                                   bg=co4, fg=co10)
        self.l_observacoes.place(x=500, y=35)
        self.e_observacoes = Entry(self.frame_superior, width=45, justify='left', relief='solid', bg=co2, fg=co10)
        self.e_observacoes.place(x=625, y=35)

        self.l_entrada = Label(self.frame_superior, text="Entrada:", font=("Courier", 13, "italic", "bold"), bg=co4,
                               fg=co10)
        self.l_entrada.place(x=540, y=60)
        self.e_entrada = DateEntry(self.frame_superior, width=42, justify='left', relief='solid', bg=co2, fg=co10)
        self.e_entrada.place(x=625, y=60)

        self.l_retirada = Label(self.frame_superior, text="Retirada:", font=("Courier", 13, "italic", "bold"), bg=co4,
                                fg=co10)
        self.l_retirada.place(x=530, y=85)
        self.e_retirada = DateEntry(self.frame_superior, width=42, justify='left', relief='solid', bg=co2, fg=co10)
        self.e_retirada.place(x=625, y=85)

# - - Frame Inferior - -
        self.l_quantidade = Label(self.frame_inferior, text="Quantidade de Itens:", justify='right', font=("Courier", 13, "italic", "bold"), bg=co4, fg=co10)
        self.l_quantidade.place(x=10, y=25)
        self.e_quantidade = Entry(self.frame_inferior, width=45, justify='left', relief='solid', bg=co2, fg=co10)
        self.e_quantidade.place(x=215, y=25)

        self.l_desconto = Label(self.frame_inferior, text="Desconto:", justify='right', font=("Courier", 13, "italic", "bold"), bg=co4, fg=co10)
        self.l_desconto.place(x=120, y=50)
        self.e_desconto= Entry(self.frame_inferior, width=45, justify='left', relief='solid', bg=co2, fg=co10)
        self.e_desconto.place(x=215, y=50)

        self.l_valor = Label(self.frame_inferior, text="Valor Total:", justify='right', font=("Courier", 13, "italic", "bold"), bg=co4, fg=co10)
        self.l_valor.place(x=90, y=75)
        self.e_valor = Entry(self.frame_inferior, width=45, justify='left', relief='solid', bg=co2, fg=co10)
        self.e_valor.place(x=215, y=75)

    def botoes(self):

        # - - Frame Inferior - -
        self.b_limpar = Button(self.frame_superior, text="Limpar", width=10, font=('Ivy 8 bold'), bg=co6, fg=co2, relief=RAISED, overrelief=RIDGE)
        self.b_limpar.place(x=480, y=130, height=40, width=100)

        self.b_procurar = Button(self.frame_superior, text="Procurar:", width=10, font=('Ivy 8 bold'), bg=co6, fg=co2, relief=RAISED, overrelief=RIDGE)
        self.b_procurar.place(x=590, y=130, height=40, width=100)

        self.b_adicionar = Button(self.frame_superior, text="Adicionar",  width=10, font=('Ivy 8 bold'), bg=co7, fg=co2, relief=RAISED, overrelief=RIDGE)
        self.b_adicionar.place(x=700, y=130, height=40, width=100)

        self.b_alterar = Button(self.frame_superior, text="Alterar",  width=10, font=('Ivy 8 bold'), bg=co8, fg=co2, relief=RAISED, overrelief=RIDGE)
        self.b_alterar.place(x=810, y=130, height=40, width=100)

        self.b_excluir = Button(self.frame_superior, text="Excluir",  width=10, font=('Ivy 8 bold'), bg=co9, fg=co2, relief=RAISED, overrelief=RIDGE)
        self.b_excluir.place(x=920, y=130, height=40, width=100)

    def grid_venda(self):
        self.lista_venda = ttk.Treeview(self.frame_grid, columns=("col0", "col1", "col2", "col3", "col4"))
        self.lista_venda.heading("#0", text="")
        self.lista_venda.heading("#1", text="Produto")
        self.lista_venda.heading("#2", text="Marca")
        self.lista_venda.heading("#3", text="Modelo")
        self.lista_venda.heading("#4", text="Cor")
        self.lista_venda.heading("#5", text="Valor")

        self.lista_venda.column("#0", anchor='center', width=5)
        self.lista_venda.column("#1", anchor='center', width=174)
        self.lista_venda.column("#2", anchor='center', width=174)
        self.lista_venda.column("#3", anchor='center', width=174)
        self.lista_venda.column("#4", anchor='center', width=174)
        self.lista_venda.column("#5", anchor='center', width=174)

        self.lista_venda.place(x=10, y=10, height=160, width=1035) #height=340

        self.barra_vertical = ttk.Scrollbar(self.frame_grid, orient='vertical', command=self.lista_venda.yview)
        self.barra_vertical.place(x=1048, y=0, height=189, width=15)

        self.barra_horizontal = ttk.Scrollbar(self.frame_grid, orient='horizontal', command=self.lista_venda.xview)
        self.barra_horizontal.place(x=0, y=174, height=15, width=1050)

        self.lista_venda.configure(yscrollcommand=self.barra_vertical.set, xscrollcommand=self.barra_horizontal.set)

Aplicacao_Venda()