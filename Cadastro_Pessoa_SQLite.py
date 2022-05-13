"""

"""
import os
import pickle
import sys
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from view import *
import view
import sqlite3
from tkcalendar import Calendar, DateEntry
import datetime



database = "gerenciador.db"

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

# - - janela Cadastro de Pessoas - -

cadpessoas = Tk()

class Funcao_Pessoas():
    def limpa_Tela_Pessoas(self):
        self.e_id_pessoas.delete(0, END)
        self.e_cpf.delete(0, END)
        self.e_nome.delete(0, END)
        self.e_telefone.delete(0, END)
        self.e_whatsapp.delete(0, END)
        self.e_email.delete(0, END)
        self.e_cep.delete(0, END)
        self.e_rua.delete(0, END)
        self.e_numero.delete(0, END)
        self.e_bairro.delete(0, END)
        self.e_cidade.delete(0, END)
        self.e_estado.delete(0, END)
        self.e_observacoes.delete(0, END)
        self.e_data_cadastro.delete(0, END)

    def conecta_bd(self):
        self.conn = sqlite3.connect('gerenciador.db')
        self.cursor = self.conn.cursor()

    def desconecta_bd(self):
        self.conn.close()

    def monta_Tabela_Pessoas(self):
        self.conecta_bd()
        print("Conectando ao banco de dados")
        self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS cad_pessoas(
                id_pessoas INTEGER AUTO_INCREMENT,
                cpf INTEGER PRIMARY KEY UNIQUE,
                nome VARCHAR(100),
                telefone VARCHAR(100),
                whatsapp VARCHAR(100),
                email VARCHAR(100),
                cep INTEGER,
                rua VARCHAR(100),
                numero INTEGER,
                bairro VARCHAR(100),
                cidade VARCHAR(100),
                estado VARCHAR(100),
                observacoes VARCHAR(200),
                data_cadastro VARCHAR(10)
            );
        """)
        self.conn.commit()
        print("Criou o Banco de dados")
        self.desconecta_bd()
        print("Desconectando ao banco de dados")

    def pessoas_Variaveis(self):
        self.id_pessoas = self.e_id_pessoas.get()
        self.cpf = self.e_cpf.get()
        self.nome = self.e_nome.get()
        self.telefone = self.e_telefone.get()
        self.whatsapp = self.e_whatsapp.get()
        self.email = self.e_email.get()
        self.cep = self.e_cep.get()
        self.rua = self.e_rua.get()
        self.numero = self.e_numero.get()
        self.bairro = self.e_bairro.get()
        self.cidade = self.e_cidade.get()
        self.estado = self.e_estado.get()
        self.observacoes = self.e_observacoes.get()
        self.data_cadastro = self.e_data_cadastro.get()

    def adiciona_Pessoa(self):
        self.pessoas_Variaveis()
        if self.e_cpf.get() == "" or self.e_nome.get() == "":
            messagebox.showerror(title="Cadastro de Pessoas", message="Campos CPF ou Nome estão vazios")
        else:
            self.conecta_bd()
            self.cursor.execute("""
                INSERT INTO 
                    cad_pessoas(cpf, nome, telefone, whatsapp, email, cep, rua, numero, bairro, cidade, estado, observacoes, data_cadastro)
                VALUES 
                    (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (self.cpf, self.nome, self.telefone, self.whatsapp, self.email, self.cep, self.rua, self.numero, self.bairro, self.cidade, self.estado, self.observacoes, self.data_cadastro))
            messagebox.showinfo(title="Cadastro de Pessoas", message="Pessoa Cadastrado com Sucesso")
        self.conn.commit()
        self.desconecta_bd()
        self.select_Pessoa()
        self.limpa_Tela_Pessoas()

    def select_Pessoa(self):
        self.listapessoas.delete(*self.listapessoas.get_children())
        self.conecta_bd()
        listaPe = self.cursor.execute("""
            SELECT * FROM
                cad_pessoas 
            ORDER BY 
                id_pessoas ASC; """)

        for i in listaPe:
            self.listapessoas.insert("", END, values=i)
        self.desconecta_bd()

    def duplo_Clique_Pessoa(self, event):
        self.limpa_Tela_Pessoas()
        self.listapessoas.selection()

        for n in self.listapessoas.selection():
            col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13, col14 = self.listapessoas.item(n, 'values')
            self.e_id_pessoas.insert(END, col1)
            self.e_cpf.insert(END, col2)
            self.e_nome.insert(END, col3)
            self.e_telefone.insert(END, col4)
            self.e_whatsapp.insert(END, col5)
            self.e_email.insert(END, col6)
            self.e_cep.insert(END, col7)
            self.e_rua.insert(END, col8)
            self.e_numero.insert(END, col9)
            self.e_bairro.insert(END, col10)
            self.e_cidade.insert(END, col11)
            self.e_estado.insert(END, col12)
            self.e_observacoes.insert(END, col13)
            self.e_data_cadastro.insert(END, col14)

    def deleta_Pessoa(self):
        self.pessoas_Variaveis()
        self.conecta_bd()
        self.cursor.execute("""DELETE FROM cad_pessoas WHERE id_pessoas = ? """, (self.id_pessoas,))
        self.conn.commit()
        self.desconecta_bd()
        self.limpa_Tela_Pessoas()
        self.select_Pessoa()

    def altera_Pessoa(self):
        self.pessoas_Variaveis()
        self.conecta_bd()
        self.cursor.execute("""
            UPDATE
                cad_pessoas
            SET
                cpf = ?,
                nome = ?,
                telefone = ?,
                whatsapp = ?,
                email = ?,
                cep = ?,
                rua = ?,
                numero = ?,
                bairro = ?,
                cidade = ?,
                estado = ?,
                observacoes = ?
                data_cadastro = ?
            WHERE
                id_pessoas = ?""",
                (self.cpf,
                 self.nome,
                 self.telefone,
                 self.whatsapp,
                 self.email,
                 self.cep,
                 self.rua,
                 self.numero,
                 self.bairro,
                 self.cidade,
                 self.estado,
                 self.observacoes,
                 self.data_cadastro,
                 self.id_pessoas))

        self.conn.commit()
        self.desconecta_bd()
        self.select_Pessoa()
        self.limpa_Tela_Pessoas()

    def buscar_Pessoa(self):
        self.conecta_bd()
        self.listapessoas.delete(*self.listapessoas.get_children())

        cpf = self.e_cpf.get()
        nome = self.e_nome.get()
        id_pessoas = self.e_id_pessoas.get()
        telefone = self.e_telefone.get()
        whatsapp = self.e_whatsapp.get()
        email = self.e_email.get()

        if len(cpf) > 0:
            self.e_cpf.insert(END, "%")
            cpf = self.e_cpf.get()
            self.cursor.execute("""
                SELECT * FROM 
                    cad_pessoas
                WHERE 
                    cpf 
                LIKE '%s' ORDER BY cpf ASC""" % cpf, )

            buscacpf = self.cursor.fetchall()

            for i in buscacpf:
                self.listapessoas.insert("", END, values=i)

        elif len(nome) > 0:
            self.e_nome.insert(END, "%")
            nome = self.e_nome.get()
            self.cursor.execute("""
                SELECT * FROM 
                    cad_pessoas 
                WHERE 
                    nome 
                LIKE '%s' ORDER BY nome ASC""" % nome, )
            buscanome = self.cursor.fetchall()

            for i in buscanome:
                self.listapessoas.insert("", END, values=i)

        elif len(id_pessoas) > 0:
            self.e_id_pessoas.insert(END, "%")
            id_pessoas = self.e_id_pessoas.get()
            self.cursor.execute("""
                SELECT * FROM 
                    cad_pessoas 
                WHERE 
                    id_pessoas 
                LIKE '%s' ORDER BY id_pessoas ASC""" % id_pessoas, )
            buscaid_pessoas = self.cursor.fetchall()

            for i in buscaid_pessoas:
                self.listapessoas.insert("", END, values=i)

        elif len(telefone) > 0:
            self.e_telefone.insert(END, "%")
            telefone = self.e_telefone.get()
            self.cursor.execute("""
                SELECT * FROM 
                    cad_pessoas 
                WHERE 
                    telefone 
                LIKE '%s' ORDER BY telefone ASC""" % telefone, )
            buscatelefone = self.cursor.fetchall()

            for i in buscatelefone:
                self.listapessoas.insert("", END, values=i)

        elif len(whatsapp) > 0:
            self.e_whatsapp.insert(END, "%")
            whatsapp = self.e_whatsapp.get()
            self.cursor.execute("""
                SELECT * FROM 
                    cad_pessoas 
                WHERE 
                    whatsapp 
                LIKE '%s' ORDER BY whatsapp ASC""" % whatsapp, )
            buscawhatsapp = self.cursor.fetchall()

            for i in buscawhatsapp:
                self.listapessoas.insert("", END, values=i)

        elif len(email) > 0:
            self.e_email.insert(END, "%")
            email = self.e_email.get()
            self.cursor.execute("""
                SELECT * FROM 
                    cad_pessoas 
                WHERE 
                    email 
                LIKE '%s' ORDER BY email ASC""" % email, )
            buscaemail = self.cursor.fetchall()

            for i in buscaemail:
                self.listapessoas.insert("", END, values=i)

        self.limpa_Tela_Pessoas()
        self.desconecta_bd()



class Aplicacao_Pessoas(Funcao_Pessoas):
    def __init__(self):
        self.cadpessoas = cadpessoas
        self.tela_cadastro_Pessoas()
        self.frames_cad_pessoas()
        self.labels_entry_pessoas()
        self.botoes_tela_pessoas()
        self.grid_Pessoas()
        self.monta_Tabela_Pessoas()
        self.select_Pessoa()
        self.deleta_Pessoa()

        self.cadpessoas.mainloop()

    def tela_cadastro_Pessoas(self):
        self.cadpessoas.title("Cadastro de Pessoas")
        self.cadpessoas.config(bg="#1e3743")
        self.cadpessoas.geometry("1095x680+263+0")

    def frames_cad_pessoas(self):
        self.frame_superior_pessoas = Frame(self.cadpessoas, bd=4, bg=co4, highlightbackground=co5, highlightthickness=6)
        self.frame_superior_pessoas.place(x=10, y=10, height=300, width=1075)

        self.frame_grid_pessoas = Frame(self.cadpessoas, height=418, width=1075, bg=co10, highlightbackground=co5, highlightthickness=6)
        self.frame_grid_pessoas.place(x=10, y=330, height=340, width=1075)

    def labels_entry_pessoas(self):

        self.l_id_pessoas = Label(self.frame_superior_pessoas, text="Código:", justify='right', font=("Courier", 13, "italic", "bold"), bg=co4, fg=co10)
        self.l_id_pessoas.place(x=50, y=10)
        self.e_id_pessoas = Entry(self.frame_superior_pessoas, width=45, justify='left', relief='raised', bg=co2, fg=co10)
        self.e_id_pessoas.place(x=125, y=10)

        self.l_cpf = Label(self.frame_superior_pessoas, text="Cpf:", font=("Courier", 13, "italic", "bold"), bg=co4, fg=co10)
        self.l_cpf.place(x=555, y=10)
        self.e_cpf = Entry(self.frame_superior_pessoas, width=45, justify='left', relief='raised', bg=co2, fg=co10)
        self.e_cpf.place(x=600, y=10)

        self.l_nome = Label(self.frame_superior_pessoas, text="Nome:", font=("Courier", 13, "italic", "bold"), bg=co4, fg=co10)
        self.l_nome.place(x=70, y=35)
        self.e_nome = Entry(self.frame_superior_pessoas, width=45, justify='left', relief='raised', bg=co2, fg=co10)
        self.e_nome.place(x=125, y=35)

        self.l_telefone = Label(self.frame_superior_pessoas, text="Telefone:", font=("Courier", 13, "italic", "bold"), bg=co4, fg=co10)
        self.l_telefone.place(x=505, y=35)
        self.e_telefone = Entry(self.frame_superior_pessoas, width=45, justify='left', relief='raised', bg=co2, fg=co10)
        self.e_telefone.place(x=600, y=35)

        self.l_whatsapp = Label(self.frame_superior_pessoas, text="Whatsapp:", font=("Courier", 13, "italic", "bold"), bg=co4, fg=co10)
        self.l_whatsapp.place(x=30, y=60)
        self.e_whatsapp = Entry(self.frame_superior_pessoas, width=45, justify='left', relief='raised', bg=co2, fg=co10)
        self.e_whatsapp.place(x=125, y=60)

        self.l_email = Label(self.frame_superior_pessoas, text="E-mail:", font=("Courier", 13, "italic", "bold"), bg=co4, fg=co10)
        self.l_email.place(x=525, y=60)
        self.e_email = Entry(self.frame_superior_pessoas, width=45, justify='left', relief='raised', bg=co2, fg=co10)
        self.e_email.place(x=600, y=60)

        self.l_cep = Label(self.frame_superior_pessoas, text="Cep:", font=("Courier", 13, "italic", "bold"), bg=co4, fg=co10)
        self.l_cep.place(x=85, y=85)
        self.e_cep = Entry(self.frame_superior_pessoas, width=45, justify='left', relief='raised', bg=co2, fg=co10)
        self.e_cep.place(x=125, y=85)

        self.l_rua = Label(self.frame_superior_pessoas, text="Rua:", font=("Courier", 13, "italic", "bold"), bg=co4, fg=co10)
        self.l_rua.place(x=555, y=85)
        self.e_rua = Entry(self.frame_superior_pessoas, width=45, justify='left', relief='raised', bg=co2, fg=co10)
        self.e_rua.place(x=600, y=85)

        self.l_numero = Label(self.frame_superior_pessoas, text="Número:", font=("Courier", 13, "italic", "bold"), bg=co4, fg=co10)
        self.l_numero.place(x=50, y=110)
        self.e_numero = Entry(self.frame_superior_pessoas, width=45, justify='left', relief='raised', bg=co2, fg=co10)
        self.e_numero.place(x=125, y=110)

        self.l_bairro = Label(self.frame_superior_pessoas, text="Bairro:", font=("Courier", 13, "italic", "bold"), bg=co4, fg=co10)
        self.l_bairro.place(x=525, y=110)
        self.e_bairro = Entry(self.frame_superior_pessoas, width=45, justify='left', relief='raised', bg=co2, fg=co10)
        self.e_bairro.place(x=600, y=110)

        self.l_cidade = Label(self.frame_superior_pessoas, text="Cidade:", font=("Courier", 13, "italic", "bold"), bg=co4, fg=co10)
        self.l_cidade.place(x=50, y=135)
        self.e_cidade = Entry(self.frame_superior_pessoas, width=45, justify='left', relief='raised', bg=co2, fg=co10)
        self.e_cidade.place(x=125, y=135)

        self.l_estado = Label(self.frame_superior_pessoas, text="Estado:", font=("Courier", 13, "italic", "bold"), bg=co4, fg=co10)
        self.l_estado.place(x=525, y=135)
        self.e_estado = Entry(self.frame_superior_pessoas, width=45, justify='left', relief='raised', bg=co2, fg=co10)
        self.e_estado.place(x=600, y=135)

        self.l_observacoes = Label(self.frame_superior_pessoas, text="Observações:", font=("Courier", 13, "italic", "bold"), bg=co4, fg=co10)
        self.l_observacoes.place(x=0, y=160)
        self.e_observacoes = Entry(self.frame_superior_pessoas, width=45, justify='left', relief='raised', bg=co2, fg=co10)
        self.e_observacoes.place(x=125, y=160)

        self.l_data = Label(self.frame_superior_pessoas, text="Data de Cadastro:", font=("Courier", 13, "italic", "bold"), bg=co4, fg=co10)
        self.l_data.place(x=425, y=160)
        self.e_data_cadastro = DateEntry(self.frame_superior_pessoas, width=42, justify='left', relief='raised', locale="pt_br")
        self.e_data_cadastro.place(x=600, y=160)

    def botoes_tela_pessoas(self):
        self.b_limpar = Button(self.frame_superior_pessoas, text="Limpar", command=self.limpa_Tela_Pessoas, width=10,font=('Ivy 8 bold'), bg=co6, fg=co2, relief=RAISED, overrelief=RIDGE)
        self.b_limpar.place(x=280, y=200, height=40, width=100)

        self.b_procurar = Button(self.frame_superior_pessoas, text="Procurar:", command=self.buscar_Pessoa, width=10, font=('Ivy 8 bold'), bg=co6, fg=co2, relief=RAISED, overrelief=RIDGE)
        self.b_procurar.place(x=390, y=200, height=40, width=100)

        self.b_adicionar = Button(self.frame_superior_pessoas, text="Adicionar:", command=self.adiciona_Pessoa, width=10, font=('Ivy 8 bold'), bg=co7, fg=co2, relief=RAISED, overrelief=RIDGE)
        self.b_adicionar.place(x=500, y=200, height=40, width=100)

        self.b_alterar = Button(self.frame_superior_pessoas, text="Alterar:", command=self.altera_Pessoa, width=10, font=('Ivy 8 bold'), bg=co8, fg=co2, relief=RAISED, overrelief=RIDGE)
        self.b_alterar.place(x=610, y=200, height=40, width=100)

        self.b_excluir = Button(self.frame_superior_pessoas, text="Excluir:", command=self.deleta_Pessoa, width=10, font=('Ivy 8 bold'), bg=co9, fg=co2, relief=RAISED, overrelief=RIDGE)
        self.b_excluir.place(x=720, y=200, height=40, width=100)

    def grid_Pessoas(self):
        self.listapessoas = ttk.Treeview(self.frame_grid_pessoas, columns=("col0", "col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8", "col9", "col10", "col11", "col12", "col13"))
        self.listapessoas.heading("#0", text="")
        self.listapessoas.heading("#1", text="Código")
        self.listapessoas.heading("#2", text="Cpf")
        self.listapessoas.heading("#3", text="Nome")
        self.listapessoas.heading("#4", text="Telefone")
        self.listapessoas.heading("#5", text="WhatsApp")
        self.listapessoas.heading("#6", text="E-Mail")
        self.listapessoas.heading("#7", text="Cep")
        self.listapessoas.heading("#8", text="Rua")
        self.listapessoas.heading("#9", text="Número")
        self.listapessoas.heading("#10", text="Bairro")
        self.listapessoas.heading("#11", text="Cidade")
        self.listapessoas.heading("#12", text="Estado")
        self.listapessoas.heading("#13", text="Observações")
        self.listapessoas.heading("#14", text="Data Cadastro")

        self.listapessoas.column("#0", anchor='center', width=2)
        self.listapessoas.column("#1", anchor='center', width=50)
        self.listapessoas.column("#2", anchor='center', width=75)
        self.listapessoas.column("#3", anchor='center',  width=85)
        self.listapessoas.column("#4", anchor='center',  width=85)
        self.listapessoas.column("#5", anchor='center', width=85)
        self.listapessoas.column("#6", anchor='center', width=85)
        self.listapessoas.column("#7", anchor='center',  width=74)
        self.listapessoas.column("#8", anchor='center',  width=74)
        self.listapessoas.column("#9", anchor='center',  width=50)
        self.listapessoas.column("#10", anchor='center',  width=74)
        self.listapessoas.column("#11", anchor='center',  width=74)
        self.listapessoas.column("#12", anchor='center',  width=74)
        self.listapessoas.column("#13", anchor='center',  width=74)
        self.listapessoas.column("#14", anchor='center', width=74)

        self.listapessoas.place(x=10, y=10, height=290, width=1035)

        self.barra_vertical = ttk.Scrollbar(self.frame_grid_pessoas, orient='vertical', command=self.listapessoas.yview)
        self.barra_vertical.place(x=1048, y=0, height=328, width=15)

        self.barra_horizontal = ttk.Scrollbar(self.frame_grid_pessoas, orient='horizontal', command=self.listapessoas.xview)
        self.barra_horizontal.place(x=0, y=313, height=15, width=1050)

        self.listapessoas.configure(yscrollcommand=self.barra_vertical.set, xscrollcommand=self.barra_horizontal.set)

        self.listapessoas.bind("<Double-1>", self.duplo_Clique_Pessoa)

Aplicacao_Pessoas()