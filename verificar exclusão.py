import os
import sys
import sqlite3 as lite

# cria a conexão com o banco de dados gerenciadordeassistencia.db
con = lite.connect('gerenciadordeassistencia.db')


# Insere Produto
def inserir_info(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO cad_produto (Produto, Cor, Valor_Compra, Valor_Venda, Estoque) VALUES (?, ?, ?, ?, ?);"
        cur.execute(query, i)


# Consulta Produto
def mostrar_info():
    lista = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM cad_produto;"
        cur.execute(query)
        informacao = cur.fetchall()

        for i in informacao:
            lista.append(i)
    return lista



# Atualizar Produto
def atualizar_info(i):
    with con:
        cur = con.cursor()
        query = "UPDATE cad_produto SET Codigo_Produto = ?, Produto = ?, Cor = ?, Valor_Compra = ?, Valor_Venda = ?, Estoque = ? WHERE Codigo_Produto = ?;"
        cur.execute(query, i)


# Deletar Produto
def deletar_info(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Cad_Produto WHERE Codigo_produto = ?"
        cur.execute(query, i)








