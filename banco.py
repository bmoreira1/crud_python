import sqlite3 as lite

conn = lite.connect('empresas.db')

with conn:
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE dados_empresa(id INTEGER PRIMARY KEY AUTOINCREMENT, cnpj int, razao_social text, qualificacao_responsavel text, capital_social text, porte_empresa text, ente_federativo text, descricao_natureza_juridica text, descricao_porte_empresa text)')