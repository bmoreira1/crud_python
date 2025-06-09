import sqlite3 as lite

conn = lite.connect('CRUD/dados.db')

with conn:
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE formulario(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, email TEXT, telefone TEXT, dia_em DATE, estado TEXT, assunto TEXT)')

