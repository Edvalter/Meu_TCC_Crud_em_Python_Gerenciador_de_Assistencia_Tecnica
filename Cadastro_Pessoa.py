
import os
import pickle
import sys
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import Combobox
from view import *
import view
from datetime import datetime as dt
import mysql.connector
from tkcalendar import Calendar, DateEntry


database = "gerenciador.db"

# Configuração das Cores

co0 = "#f0f3f5"  # white
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


# - - janela Cadastro de Pessoas - -

cadpessoas = Tk()


class Funcao_Pessoas():
    def limpa_Tela_Pessoas(self):
        self.e_id_pessoa.delete(0, END)
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
        self.c_status_pessoa.delete(0, END)

    def conecta_bd(self):
        self.conn = mysql.connector.connect(host='localhost', database='gerenciador', user='root', password='admin')
        self.cursor = self.conn.cursor()

    def desconecta_bd(self):
        self.conn.close()

    def monta_Tabela_Pessoas(self):
        self.conecta_bd()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS pessoas(
                id_pessoa INTEGER AUTO_INCREMENT,
                cpf VARCHAR(100),
                nome VARCHAR(100),
                telefone VARCHAR(100),
                whatsapp VARCHAR(100),
                email VARCHAR(100),
                cep VARCHAR(100),
                rua VARCHAR(100),
                numero INTEGER,
                bairro VARCHAR(100),
                cidade VARCHAR(100),
                estado VARCHAR(100),
                observacoes VARCHAR(200),
                statuspessoa VARCHAR(100),
                data_cadastro DATE,
            PRIMARY KEY (id_pessoa));
            """)
        self.conn.commit()
        self.desconecta_bd()

    def pessoas_Variaveis(self):
        self.id_pessoa = self.e_id_pessoa.get()
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
        self.status_pessoa = self.c_status_pessoa.get()
        self.data_cadastro = self.e_data_cadastro.get()
        self.dataConvertida = self.converteData()

    def converteData(self):
        if self.data_cadastro != '':
            dataConvertida = dt.strptime(self.data_cadastro, '%d/%m/%Y')
            return dataConvertida
        else:
            pass

    def adiciona_Pessoa(self):
        self.pessoas_Variaveis()
        if self.e_cpf.get() == "" or self.e_nome.get() == "":
            messagebox.showerror(title="Cadastro de Pessoas", message="Algumas Informações Não Foram Inseridas")
            pass
        else:
            self.conecta_bd()
            self.cursor.execute(f"""
                INSERT INTO 
                    pessoas( 
                        cpf, 
                        nome, 
                        telefone, 
                        whatsapp, 
                        email, 
                        cep, 
                        rua, 
                        numero, 
                        bairro, 
                        cidade, 
                        estado, 
                        observacoes,
                        status_pessoa, 
                        data_cadastro) 
                VALUES 
                         ('{self.cpf}',
                        '{self.nome}',
                        '{self.telefone}',
                        '{self.whatsapp}',
                        '{self.email}',
                        '{self.cep}',
                        '{self.rua}',
                        '{self.numero}',
                        '{self.bairro}',
                        '{self.cidade}',
                        '{self.estado}',
                        '{self.observacoes}',
                        '{self.status_pessoa}',
                        '{self.dataConvertida}'); """)

            messagebox.showinfo(title="Cadastro de Pessoas", message="Cadastro realizado com sucesso")

        self.conn.commit()
        self.desconecta_bd()
        self.select_Pessoa()
        self.limpa_Tela_Pessoas()

    def select_Pessoa(self):
        self.listapessoas.delete(*self.listapessoas.get_children())
        self.conecta_bd()
        listaPe = self.cursor.execute(f"""
            SELECT * FROM pessoas ORDER BY id_pessoa ASC; """)

        listaPe = self.cursor.fetchall()

        for i in listaPe:
            posicaoDaData = i[0:14]+(i[14].strftime('%d/%m/%Y'),)
            self.listapessoas.insert("", END, values=posicaoDaData)

        self.desconecta_bd()

    def duploCliquePessoa(self, event):
        self.limpa_Tela_Pessoas()
        self.listapessoas.selection()

        for n in self.listapessoas.selection():
            col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13, col14, col15 = self.listapessoas.item(n, 'values')

            self.e_id_pessoa.insert(END, col1)
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
            self.c_status_pessoa .insert(END, col14)
            self.e_data_cadastro.insert(END, col15)

    def deleta_Pessoa(self):
        self.pessoas_Variaveis()
        self.conecta_bd()
        self.cursor.execute(f"""
            DELETE FROM 
                pessoas 
            WHERE 
                id_pessoa = '{self.id_pessoa}'; """)

        messagebox.showinfo(title="Cadastro de Pessoas", message="Cadastro Excluído com sucesso")

        self.conn.commit()
        self.desconecta_bd()
        self.limpa_Tela_Pessoas()
        self.select_Pessoa()


    def altera_Pessoa(self):
        self.pessoas_Variaveis()
        if self.id_pessoa == '':
            pass
        else:
            self.conecta_bd()
            self.cursor.execute(f"""
                UPDATE
                    pessoas
                SET
                    cpf = '{self.cpf}',
                    nome = '{self.nome}',
                    telefone = '{self.telefone}',
                    whatsapp = '{self.whatsapp}',
                    email = '{self.email}',
                    cep = '{self.cep}',
                    rua = '{self.rua}',
                    numero = '{self.numero}',
                    bairro = '{self.bairro}',
                    cidade = '{self.cidade}',
                    estado = '{self.estado}',
                    observacoes = '{self.observacoes}',
                    status_pessoa = '{self.status_pessoa}',
                    data_cadastro = '{self.dataConvertida}'
                WHERE
                    id_pessoa = {self.id_pessoa}; """)

            messagebox.showinfo(title="Cadastro de Pessoas", message="Cadastro Alterado com Sucesso")

        self.conn.commit()
        self.desconecta_bd()
        self.select_Pessoa()

    def buscar_Pessoa(self):
        self.conecta_bd()
        self.listapessoas.delete(*self.listapessoas.get_children())

        cpf = self.e_cpf.get()
        nome = self.e_nome.get()
        id_pessoa = self.e_id_pessoa.get()
        telefone = self.e_telefone.get()
        whatsapp = self.e_whatsapp.get()
        email = self.e_email.get()

        if len(cpf) > 0:
            self.e_cpf.insert(END, "")
            cpf = self.e_cpf.get()
            self.cursor.execute(f"""
               SELECT * FROM  
                   pessoas 
               WHERE 
                   cpf 
               LIKE '%{cpf}%' ORDER BY id_pessoa ASC; """)

            buscacpf = self.cursor.fetchall()

            for i in buscacpf:
                posicaoDaData = i[0:14] + (i[14].strftime('%d/%m/%Y'),)
                self.listapessoas.insert("", END, values=posicaoDaData)

        elif len(nome) > 0:
            self.e_nome.insert(END, "")
            nome = self.e_nome.get()
            self.cursor.execute(f"""
               SELECT * FROM  
                   pessoas 
               WHERE 
                   nome 
               LIKE '%{nome}%' ORDER BY id_pessoa ASC; """)

            buscanome = self.cursor.fetchall()

            for i in buscanome:
                posicaoDaData = i[0:14] + (i[14].strftime('%d/%m/%Y'),)
                self.listapessoas.insert("", END, values=posicaoDaData)

        elif len(id_pessoa) > 0:
            self.e_id_pessoa.insert(END, "")
            id_pessoa = self.e_id_pessoa.get()
            self.cursor.execute(f"""
               SELECT * FROM  
                   pessoas 
               WHERE 
                   id_pessoa 
               LIKE '%{id_pessoa}%' ORDER BY id_pessoa ASC; """)

            buscaid_pessoas = self.cursor.fetchall()

            for i in buscaid_pessoas:
                posicaoDaData = i[0:14] + (i[14].strftime('%d/%m/%Y'),)
                self.listapessoas.insert("", END, values=posicaoDaData)

        elif len(telefone) > 0:
            self.e_telefone.insert(END, "")
            telefone = self.e_telefone.get()
            self.cursor.execute(f"""
               SELECT * FROM  
                   pessoas 
               WHERE 
                   telefone 
               LIKE '%{telefone}%' ORDER BY id_pessoa ASC; """)

            buscatelefone = self.cursor.fetchall()

            for i in buscatelefone:
                posicaoDaData = i[0:14] + (i[14].strftime('%d/%m/%Y'),)
                self.listapessoas.insert("", END, values=posicaoDaData)

        elif len(whatsapp) > 0:
            self.e_whatsapp.insert(END, "")
            whatsapp = self.e_whatsapp.get()
            self.cursor.execute(f"""
               SELECT * FROM  
                   pessoas 
               WHERE 
                   whatsapp 
               LIKE '%{whatsapp}%' ORDER BY id_pessoa ASC; """)

            buscawhatsapp = self.cursor.fetchall()

            for i in buscawhatsapp:
                posicaoDaData = i[0:14] + (i[14].strftime('%d/%m/%Y'),)
                self.listapessoas.insert("", END, values=posicaoDaData)

        elif len(email) > 0:
            self.e_email.insert(END, "")
            email = self.e_email.get()
            self.cursor.execute(f"""
               SELECT * FROM  
                   pessoas 
               WHERE 
                   email 
               LIKE '%{email}%' ORDER BY id_pessoa ASC; """)
            buscaemail = self.cursor.fetchall()

            for i in buscaemail:
                posicaoDaData = i[0:14] + (i[14].strftime('%d/%m/%Y'),)
                self.listapessoas.insert("", END, values=posicaoDaData)

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

        self.cadpessoas.mainloop()

    def tela_cadastro_Pessoas(self):
        self.cadpessoas.title("Cadastro de Pessoas")
        self.cadpessoas.config(bg="#1e3743")
        self.cadpessoas.geometry("1095x700+263+0")
        self.cadpessoas.iconbitmap("C:/Users/Edinho/PycharmProjects/Meu_TCC/Logo/segatIcone.ico")

    def frames_cad_pessoas(self):
        self.frame_superior_pessoas = Frame(self.cadpessoas, bd=4, bg=co6, highlightbackground=co5, highlightthickness=6)
        self.frame_superior_pessoas.place(x=10, y=10, height=300, width=1075)

        self.frame_grid_pessoas = Frame(self.cadpessoas, height=418, width=1075, bg=co0, highlightbackground=co5, highlightthickness=6)
        self.frame_grid_pessoas.place(x=10, y=325, height=360, width=1075)

    def labels_entry_pessoas(self):
        self.l_id_pessoa= Label(self.frame_superior_pessoas, text="Código:", justify='right', font=("Courier", 13, "italic", "bold"), bg=co6, fg=co10)
        self.l_id_pessoa.place(x=75, y=10)
        self.e_id_pessoa = Entry(self.frame_superior_pessoas, width=45, justify='left', relief='raised', bg=co0, fg=co10)
        self.e_id_pessoa.place(x=150, y=10)

        self.l_cpf = Label(self.frame_superior_pessoas, text="CPF:", font=("Courier", 13, "italic", "bold"), bg=co6, fg=co10)
        self.l_cpf.place(x=605, y=10)
        self.e_cpf = Entry(self.frame_superior_pessoas, width=45, justify='left', relief='raised', bg=co0, fg=co10)
        self.e_cpf.place(x=650, y=10)

        self.l_nome = Label(self.frame_superior_pessoas, text="Nome:", font=("Courier", 13, "italic", "bold"), bg=co6, fg=co10)
        self.l_nome.place(x=95, y=35)
        self.e_nome = Entry(self.frame_superior_pessoas, width=45, justify='left', relief='raised', bg=co0, fg=co10)
        self.e_nome.place(x=150, y=35)

        self.l_telefone = Label(self.frame_superior_pessoas, text="Telefone:", font=("Courier", 13, "italic", "bold"), bg=co6, fg=co10)
        self.l_telefone.place(x=555, y=35)
        self.e_telefone = Entry(self.frame_superior_pessoas, width=45, justify='left', relief='raised', bg=co0, fg=co10)
        self.e_telefone.place(x=650, y=35)

        self.l_whatsapp = Label(self.frame_superior_pessoas, text="Whatsapp:", font=("Courier", 13, "italic", "bold"), bg=co6, fg=co10)
        self.l_whatsapp.place(x=55, y=60)
        self.e_whatsapp = Entry(self.frame_superior_pessoas, width=45, justify='left', relief='raised', bg=co0, fg=co10)
        self.e_whatsapp.place(x=150, y=60)

        self.l_email = Label(self.frame_superior_pessoas, text="E-mail:", font=("Courier", 13, "italic", "bold"), bg=co6, fg=co10)
        self.l_email.place(x=575, y=60)
        self.e_email = Entry(self.frame_superior_pessoas, width=45, justify='left', relief='raised', bg=co0, fg=co10)
        self.e_email.place(x=650, y=60)

        self.l_cep = Label(self.frame_superior_pessoas, text="CEP:", font=("Courier", 13, "italic", "bold"), bg=co6, fg=co10)
        self.l_cep.place(x=105, y=85)
        self.e_cep = Entry(self.frame_superior_pessoas, width=45, justify='left', relief='raised', bg=co0, fg=co10)
        self.e_cep.place(x=150, y=85)

        self.l_rua = Label(self.frame_superior_pessoas, text="Rua:", font=("Courier", 13, "italic", "bold"), bg=co6, fg=co10)
        self.l_rua.place(x=605, y=85)
        self.e_rua = Entry(self.frame_superior_pessoas, width=45, justify='left', relief='raised', bg=co0, fg=co10)
        self.e_rua.place(x=650, y=85)

        self.l_numero = Label(self.frame_superior_pessoas, text="Número:", font=("Courier", 13, "italic", "bold"), bg=co6, fg=co10)
        self.l_numero.place(x=75, y=110)
        self.e_numero = Entry(self.frame_superior_pessoas, width=45, justify='left', relief='raised', bg=co0, fg=co10)
        self.e_numero.place(x=150, y=110)

        self.l_bairro = Label(self.frame_superior_pessoas, text="Bairro:", font=("Courier", 13, "italic", "bold"), bg=co6, fg=co10)
        self.l_bairro.place(x=575, y=110)
        self.e_bairro = Entry(self.frame_superior_pessoas, width=45, justify='left', relief='raised', bg=co0, fg=co10)
        self.e_bairro.place(x=650, y=110)

        self.l_cidade = Label(self.frame_superior_pessoas, text="Cidade:", font=("Courier", 13, "italic", "bold"), bg=co6, fg=co10)
        self.l_cidade.place(x=75, y=135)
        self.e_cidade = Entry(self.frame_superior_pessoas, width=45, justify='left', relief='raised', bg=co0, fg=co10)
        self.e_cidade.place(x=150, y=135)

        self.l_estado = Label(self.frame_superior_pessoas, text="Estado:", font=("Courier", 13, "italic", "bold"), bg=co6, fg=co10)
        self.l_estado.place(x=575, y=135)
        self.e_estado = Entry(self.frame_superior_pessoas, width=45, justify='left', relief='raised', bg=co0, fg=co10)
        self.e_estado.place(x=650, y=135)

        self.l_observacoes = Label(self.frame_superior_pessoas, text="Observações:", font=("Courier", 13, "italic", "bold"), bg=co6, fg=co10)
        self.l_observacoes.place(x=25, y=160)
        self.e_observacoes = Entry(self.frame_superior_pessoas, width=45, justify='left', relief='raised', bg=co0, fg=co10)
        self.e_observacoes.place(x=150, y=160)

        self.l_data = Label(self.frame_superior_pessoas, text="Data de Cadastro:", font=("Courier", 13, "italic", "bold"), bg=co6, fg=co10)
        self.l_data.place(x=475, y=160)
        self.e_data_cadastro = DateEntry(self.frame_superior_pessoas, width=42, justify='left', relief='raised', locale="pt_br")
        self.e_data_cadastro.place(x=650, y=160)

        self.l_status_pessoa = Label(self.frame_superior_pessoas, text="Status:", font=("Courier", 13, "italic", "bold"), bg=co6, fg=co10)
        self.l_status_pessoa.place(x=70, y=185)
        self.c_status_pessoa = Combobox(self.frame_superior_pessoas, width=42)
        self.c_status_pessoa["values"] = ("Cliente", "Usuário", "Administrador")
        self.c_status_pessoa.set("Cliente")
        self.c_status_pessoa.place(x=150, y=185)

    def botoes_tela_pessoas(self):
        self.b_limpar = Button(self.frame_superior_pessoas, text="Limpar", command=self.limpa_Tela_Pessoas, width=10,font=("Courier", 13, "italic", "bold"), bg=co1, fg=co2, relief=RAISED, overrelief=RIDGE)
        self.b_limpar.place(x=380, y=225, height=40, width=100)

        self.b_procurar = Button(self.frame_superior_pessoas, text="Procurar", command=self.buscar_Pessoa, width=10, font=("Courier", 13, "italic", "bold"), bg=co1, fg=co2, relief=RAISED, overrelief=RIDGE)
        self.b_procurar.place(x=490, y=225, height=40, width=100)

        self.b_adicionar = Button(self.frame_superior_pessoas, text="Adicionar", command=self.adiciona_Pessoa, width=10, font=("Courier", 13, "italic", "bold"), bg=co7, fg=co2, relief=RAISED, overrelief=RIDGE)
        self.b_adicionar.place(x=600, y=225, height=40, width=100)

        self.b_alterar = Button(self.frame_superior_pessoas, text="Alterar", command=self.altera_Pessoa, width=10, font=("Courier", 13, "italic", "bold"), bg=co8, fg=co2, relief=RAISED, overrelief=RIDGE)
        self.b_alterar.place(x=710, y=225, height=40, width=100)

        self.b_excluir = Button(self.frame_superior_pessoas, text="Excluir", command=self.deleta_Pessoa, width=10, font=("Courier", 13, "italic", "bold"), bg=co9, fg=co2, relief=RAISED, overrelief=RIDGE)
        self.b_excluir.place(x=820, y=225, height=40, width=100)



    def grid_Pessoas(self):
        self.listapessoas = ttk.Treeview(self.frame_grid_pessoas, columns=("col0", "col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8", "col9", "col10", "col11", "col12", "col13", "col14"""))
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

        self.listapessoas.column("#0", anchor='center', width=1)
        self.listapessoas.column("#1", anchor='center', width=45)
        self.listapessoas.column("#2", anchor='center', width=70)
        self.listapessoas.column("#3", anchor='center',  width=90)
        self.listapessoas.column("#4", anchor='center',  width=90)
        self.listapessoas.column("#5", anchor='center', width=90)
        self.listapessoas.column("#6", anchor='center', width=120)
        self.listapessoas.column("#7", anchor='center',  width=80)
        self.listapessoas.column("#8", anchor='center',  width=100)
        self.listapessoas.column("#9", anchor='center',  width=50)
        self.listapessoas.column("#10", anchor='center',  width=70)
        self.listapessoas.column("#11", anchor='center',  width=70)
        self.listapessoas.column("#12", anchor='center',  width=65)
        self.listapessoas.column("#13", anchor='center',  width=65)
        self.listapessoas.column("#14", anchor='center', width=80)
        self.listapessoas.column("#15", anchor='center', width=100)

        self.listapessoas.place(x=0, y=1, height=325, width=1050)

        self.barra_vertical = ttk.Scrollbar(self.frame_grid_pessoas, orient='vertical', command=self.listapessoas.yview)
        self.barra_vertical.place(x=1048, y=0, height=342, width=15)

        self.barra_horizontal = ttk.Scrollbar(self.frame_grid_pessoas, orient='horizontal', command=self.listapessoas.xview)
        self.barra_horizontal.place(x=0, y=328, height=15, width=1045)

        self.listapessoas.configure(yscrollcommand=self.barra_vertical.set, xscrollcommand=self.barra_horizontal.set)

        self.listapessoas.bind("<Double-1>", self.duploCliquePessoa)

Aplicacao_Pessoas()
