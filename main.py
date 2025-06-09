import tkinter as tk
from tkcalendar import DateEntry
from tkinter import ttk

from view import *
from tkinter import messagebox

################# cores ###############
co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#ef5350"   # vermelha
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # sky blue


################# criando janela ###############

janela = tk.Tk()
janela.title("")
janela.geometry('1043x453')
janela.configure(background=co9)
janela.resizable(width=False, height=False)


################# dividindo janela ###############

frame_cima = tk.Frame(janela, width=310, height=50, bg=co2, relief='flat')
frame_cima.grid(row=0, column=0)

frame_baixo = tk.Frame(janela, width=310, height=403, bg=co1, relief='flat')
frame_baixo.grid(row=1, column=0, padx=0, pady=0, sticky=tk.NSEW)

frame_direita = tk.Frame(janela, width=588, height=403, bg=co1, relief='flat')
frame_direita.grid(row=0, column=1, rowspan=2, padx=1, sticky=tk.NSEW)


################# label cima ###############

app_nome = tk.Label(frame_cima, text='Formulário de consultoria', anchor=tk.NW, font=('Ivy 13 bold'), bg=co2, fg=co1, relief='flat')
app_nome.place(x=10, y=20)

global tree

def inserir():
    nome = entry_nome.get()
    email = entry_email.get()
    telefone = entry_telefone.get()
    calendario = entry_calendario.get()
    estado = entry_estado.get()
    assunto = entry_assunto.get()

    lista = [nome, email, telefone, calendario, estado, assunto]

    if nome == '':
        messagebox.showerror('Erro', 'nome não pode ser vazio')
    else:
        inserir_info(lista)
        messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')

        entry_nome.delete(0, 'end')
        entry_email.delete(0, 'end')
        entry_telefone.delete(0, 'end')
        entry_calendario.delete(0, 'end')
        entry_estado.delete(0, 'end')
        entry_assunto.delete(0, 'end')

    for widget in frame_direita.winfo_children():
        widget.destroy()
    mostrar()


def atualizar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario['values']

        valor_id = tree_lista[0]

        entry_nome.delete(0, 'end')
        entry_email.delete(0, 'end')
        entry_telefone.delete(0, 'end')
        entry_calendario.delete(0, 'end')
        entry_estado.delete(0, 'end')
        entry_assunto.delete(0, 'end')

        entry_nome.insert(0, tree_lista[1])
        entry_email.insert(0, tree_lista[2])
        entry_telefone.insert(0, tree_lista[3])
        entry_calendario.insert(0, tree_lista[4])
        entry_estado.insert(0, tree_lista[5])
        entry_assunto.insert(0, tree_lista[6])

        def update():
            nome = entry_nome.get()
            email = entry_email.get()
            telefone = entry_telefone.get()
            calendario = entry_calendario.get()
            estado = entry_estado.get()
            assunto = entry_assunto.get()

            lista = [nome, email, telefone, calendario, estado, assunto, valor_id]

            if nome == '':
                messagebox.showerror('Erro', 'nome não pode ser vazio')
            else:
                atualizar_info(lista)
                messagebox.showinfo('Sucesso', 'Os dados foram atualizados com sucesso')

                entry_nome.delete(0, 'end')
                entry_email.delete(0, 'end')
                entry_telefone.delete(0, 'end')
                entry_calendario.delete(0, 'end')
                entry_estado.delete(0, 'end')
                entry_assunto.delete(0, 'end')

            for widget in frame_direita.winfo_children():
                widget.destroy()

            mostrar()
        botao_Confirmar = tk.Button(frame_baixo,command=update, text='Confirmar', width=10, font=("ivi 9 bold"), bg=co2, fg=co1, relief='raised', overrelief='ridge')
        botao_Confirmar.place(x=110, y=370)

    except IndexError:
        messagebox.showerror('Error', 'seleciona um dos dados na tabela')

def deletar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario['values']

        valor_id = [tree_lista[0]]

        deletar_info(valor_id)
        messagebox.showinfo('Sucesso', 'Os dados foram deletados com sucesso')

        for widget in frame_direita.winfo_children():
            widget.destroy()

        mostrar()

    except IndexError:
        messagebox.showerror('Error', 'seleciona um dos dados na tabela')

################# configurando frame baixo ###############
################# NOME ###############
label_nome = tk.Label(frame_baixo, text='Nome:', anchor=tk.NW, font=('Ivy 13 bold'), bg=co1, fg=co4, relief='flat')
label_nome.place(x=10, y=10)

entry_nome = tk.Entry(frame_baixo, width=45, justify='left',  relief='solid')
entry_nome.place(x=15, y=40)


################# EMAIL ###############
label_email = tk.Label(frame_baixo, text='Email:', anchor=tk.NW, font=('Ivy 13 bold'), bg=co1, fg=co4, relief='flat')
label_email.place(x=10, y=70)

entry_email = tk.Entry(frame_baixo, width=45, justify='left',  relief='solid')
entry_email.place(x=15, y=100)


################# TELEFONE ###############
label_telefone = tk.Label(frame_baixo, text='Telefone:', anchor=tk.NW, font=('Ivy 13 bold'), bg=co1, fg=co4, relief='flat')
label_telefone.place(x=10, y=130)

entry_telefone = tk.Entry(frame_baixo, width=45, justify='left',  relief='solid')
entry_telefone.place(x=15, y=160)


################# DATA CONSULTA ###############
label_calendario = tk.Label(frame_baixo, text='Data da consulta:', anchor=tk.NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
label_calendario.place(x=10, y=190)

entry_calendario = DateEntry(frame_baixo, selectmode='day', date_pattern='dd/mm/yyyy')
entry_calendario.place(x=15, y=220)



################# ESTADO DA CONSULTA ###############
label_estado = tk.Label(frame_baixo, text='Estado da consulta:', anchor=tk.NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
label_estado.place(x=160, y=190)

entry_estado = tk.Entry(frame_baixo, width=20, justify='left',  relief='solid')
entry_estado.place(x=160, y=220)


################# CONSULTA SOBRE ###############
label_assunto = tk.Label(frame_baixo, text='Informação extra:', anchor=tk.NW, font=('Ivy 13 bold'), bg=co1, fg=co4, relief='flat')
label_assunto.place(x=10, y=250)

entry_assunto = tk.Entry(frame_baixo, width=45, justify='left',  relief='solid')
entry_assunto.place(x=15, y=280)


################# BOTÃO INSERIR ###############
botao_inserir = tk.Button(frame_baixo, command=inserir, text='Inserir', width=10, font=("ivi 9 bold"), bg=co6, fg=co1, relief='raised', overrelief='ridge')
botao_inserir.place(x=15, y=330)


################# BOTÃO ATUALIZAR ###############
botao_atualizar = tk.Button(frame_baixo, command=atualizar, text='Atualizar', width=10, font=("ivi 9 bold"), bg=co2, fg=co1, relief='raised', overrelief='ridge')
botao_atualizar.place(x=110, y=330)


################# BOTÃO DELETAR ###############
botao_deletar = tk.Button(frame_baixo, command=deletar, text='Deletar', width=10, font=("ivi 9 bold"), bg=co7, fg=co1, relief='raised', overrelief='ridge')
botao_deletar.place(x=205, y=330)


def mostrar():
    global tree

    lista = mostar_info()

    # lista para cabecario
    tabela_head = ['ID','Nome',  'email','telefone', 'Data', 'Estado','Sobre']


    # criando a tabela
    tree = ttk.Treeview(frame_direita, selectmode="extended", columns=tabela_head, show="headings")

    # vertical scrollbar
    vsb = ttk.Scrollbar(frame_direita, orient="vertical", command=tree.yview)

    # horizontal scrollbar
    hsb = ttk.Scrollbar( frame_direita, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    frame_direita.grid_rowconfigure(0, weight=12)


    hd=["nw","nw","nw","nw","nw","center","center"]
    h=[30,170,140,100,120,50,100]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=tk.CENTER)
        # adjust the column's width to the header string
        tree.column(col, width=h[n],anchor=hd[n])

        n+=1

    for item in lista:
        tree.insert('', 'end', values=item)


mostrar()

janela.mainloop()