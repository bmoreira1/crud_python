import sqlite3 as lite

conn = lite.connect("empresas.db")

def inserir_info(i):
    with conn:
        cursor = conn.cursor()
        query= "INSERT INTO dados_empresa (cnpj, razao_social, qualificacao_responsavel, capital_social, porte_empresa, ente_federativo, descricao_natureza_juridica, descricao_porte_empresa) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"

        cursor.execute(query,i)


def mostar_info():
    lista = []
    with conn:
        cursor = conn.cursor()
        query = "SELECT * FROM dados_empresa"
        cursor.execute(query)

        info = cursor.fetchall()
        for i in info:
            lista.append(i)
    return lista


def atualizar_info(i):
    with conn:
        cursor = conn.cursor()
        query = "UPDATE dados_empresa SET cnpj=?, razao_social=?, qualificacao_responsavel=?, capital_social=?, porte_empresa=?, ente_federativo=?, descricao_natureza_juridica=?, descricao_porte_empresa=? WHERE id=?"
        cursor.execute(query, i)


def deletar_info(i):
    with conn:
        cursor = conn.cursor()
        query = "DELETE FROM dados_empresa WHERE id=?"
        cursor.execute(query, i)