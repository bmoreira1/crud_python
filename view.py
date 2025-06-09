import sqlite3 as lite

conn = lite.connect("dados.db")

def inserir_info(i):
    with conn:
        cursor = conn.cursor()
        query= "INSERT INTO formulario (nome, email, telefone, dia_em, estado, assunto) VALUES (?, ?, ?, ?, ?, ?)"
        cursor.execute(query,i)


def mostar_info():
    lista = []
    with conn:
        cursor = conn.cursor()
        query = "SELECT * FROM formulario"
        cursor.execute(query)

        info = cursor.fetchall()
        for i in info:
            lista.append(i)
    return lista


def atualizar_info(i):
    with conn:
        cursor = conn.cursor()
        query = "UPDATE formulario SET nome=?, email=?, telefone=?, dia_em=?, estado=?, assunto=? WHERE id=?"
        cursor.execute(query, i)


def deletar_info(i):
    with conn:
        cursor = conn.cursor()
        query = "DELETE FROM formulario WHERE id=?"
        cursor.execute(query, i)