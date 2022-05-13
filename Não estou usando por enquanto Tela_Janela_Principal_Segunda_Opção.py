from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import tix
from tkinter import font
import mysql.connector

janela_principal = Tk()
janela_principal.geometry("1200x680+100+10")
janela_principal.title("Sistema de Gerenciamento")
janela_principal.config(bg="#808080")

# - - - Frame - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

LeftFrame = Frame(janela_principal, width=250, height=680, bg="#8F8FBD")
LeftFrame.pack(side=LEFT)

# - - - Botões - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

Cadastro_Button = Button(LeftFrame, text="Cadastro de Pessoas", width=40, font=("Courier", 15, "italic", "bold"), bg="#808000", activebackground="#66FF99", borderwidth=3)
Cadastro_Button.place(x=0, y=0, height=60, width=250)


Estoque_Button = Button(LeftFrame, text="Consulta de Estoque", width=40, font=("Courier", 15, "italic", "bold"), bg="#808000", activebackground="#66FF99", borderwidth=3)
Estoque_Button.place(x=0, y=50, height=60, width=250)

Venda_Button = Button(LeftFrame, text="Vender", width=40, font=("Courier", 15, "italic", "bold"), bg="#808000", activebackground="#66FF99", borderwidth=3)
Venda_Button.place(x=0, y=100, height=60, width=250)


janela_principal.mainloop()
