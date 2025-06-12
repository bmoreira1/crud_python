import tkinter as tk
from tkinter import ttk

from view import *
from tkinter import messagebox

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



janela = tk.Tk()
janela.title("")
janela.geometry('1483x653')
janela.configure(background=co9)
janela.resizable(width=False, height=False)



frame_cima = tk.Frame(janela, width=310, height=50, bg=co2, relief='flat')
frame_cima.grid(row=0, column=0)

frame_baixo = tk.Frame(janela, width=310, height=603, bg=co1, relief='flat')
frame_baixo.grid(row=1, column=0, padx=0, pady=0, sticky=tk.NSEW)

frame_direita = tk.Frame(janela, width=588, height=403, bg=co1, relief='flat')
frame_direita.grid(row=0, column=1, rowspan=2, padx=1, sticky=tk.NSEW)


app_nome = tk.Label(frame_cima, text='Dados Empresas', anchor=tk.NW, font=('Ivy 13 bold'), bg=co2, fg=co1, relief='flat')
app_nome.place(x=10, y=20)

global tree

def inserir():
    cnpj = entry_cnpj.get()
    razao_social = entry_razao_social.get()
    qualificacao_responsavel = entry_qualificacao_responsavel.get()
    capital_social = entry_capital_social.get()
    porte_empresa = entry_porte_empresa.get()
    ente_federativo = entry_ente_federativo.get()
    descricao_natureza_juridica = entry_descricao_natureza_juridica.get()
    descricao_porte_empresa = entry_descricao_porte_empresa.get()

    lista = [cnpj, razao_social, qualificacao_responsavel, capital_social, porte_empresa, ente_federativo, descricao_natureza_juridica, descricao_porte_empresa]

    if cnpj == '':
        messagebox.showerror('Erro', 'nome não pode ser vazio')
    else:
        inserir_info(lista)
        messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')

        entry_cnpj.delete(0, 'end')
        entry_razao_social.delete(0, 'end')
        entry_qualificacao_responsavel.delete(0, 'end')
        entry_capital_social.delete(0, 'end')
        entry_porte_empresa.delete(0, 'end')
        entry_ente_federativo.delete(0, 'end')
        entry_descricao_natureza_juridica.delete(0, 'end')
        entry_descricao_porte_empresa.delete(0, 'end')

    for widget in frame_direita.winfo_children():
        widget.destroy()
    mostrar()


def atualizar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario['values']

        valor_id = tree_lista[0]

        entry_cnpj.delete(0, 'end')
        entry_razao_social.delete(0, 'end')
        entry_qualificacao_responsavel.delete(0, 'end')
        entry_capital_social.delete(0, 'end')
        entry_porte_empresa.delete(0, 'end')
        entry_ente_federativo.delete(0, 'end')
        entry_descricao_natureza_juridica.delete(0, 'end')
        entry_descricao_porte_empresa.delete(0, 'end')

        entry_cnpj.insert(0, tree_lista[1])
        entry_razao_social.insert(0, tree_lista[2])
        entry_qualificacao_responsavel.insert(0, tree_lista[3])

        entry_capital_social.insert(0, tree_lista[4])
        entry_porte_empresa.insert(0, tree_lista[5])
        entry_ente_federativo.insert(0, tree_lista[6])
        entry_descricao_natureza_juridica.insert(0, tree_lista[7])
        entry_descricao_porte_empresa.insert(0, tree_lista[8])

        def update():
            cnpj = entry_cnpj.get()
            razao_social = entry_razao_social.get()
            qualificacao_responsavel = entry_qualificacao_responsavel.get()
            print(f"CNPJ: {cnpj}")
            print(f"Razão Social: {razao_social}")
            print(f"Qualificação Responsável: {qualificacao_responsavel}")
            capital_social = entry_capital_social.get()
            print(f"capital: {capital_social}")
            porte_empresa = entry_porte_empresa.get()
            ente_federativo = entry_ente_federativo.get()
            descricao_natureza_juridica = entry_descricao_natureza_juridica.get()
            descricao_porte_empresa = entry_descricao_porte_empresa.get()

            lista = [cnpj, razao_social, qualificacao_responsavel, capital_social, porte_empresa, ente_federativo, descricao_natureza_juridica, descricao_porte_empresa, valor_id]

            if cnpj == '':
                messagebox.showerror('Erro', 'Os campos não podem estar vazios')
            else:
                atualizar_info(lista)
                messagebox.showinfo('Sucesso', 'Os dados foram atualizados com sucesso')

                entry_cnpj.delete(0, 'end')
                entry_razao_social.delete(0, 'end')
                entry_qualificacao_responsavel.delete(0, 'end')
                entry_capital_social.delete(0, 'end')
                entry_porte_empresa.delete(0, 'end')
                entry_ente_federativo.delete(0, 'end')
                entry_descricao_natureza_juridica.delete(0, 'end')
                entry_descricao_porte_empresa.delete(0, 'end')

            for widget in frame_direita.winfo_children():
                widget.destroy()

            mostrar()
        botao_Confirmar = tk.Button(frame_baixo,command=update, text='Confirmar', width=10, font=("ivi 9 bold"), bg=co2, fg=co1, relief='raised', overrelief='ridge')
        botao_Confirmar.place(x=110, y=570)

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


label_cnpj = tk.Label(frame_baixo, text='CNPJ:', anchor=tk.NW, font=('Ivy 13 bold'), bg=co1, fg=co4, relief='flat')
label_cnpj.place(x=10, y=10)

entry_cnpj = tk.Entry(frame_baixo, width=45, justify='left',  relief='solid')
entry_cnpj.place(x=15, y=40)


label_razao_social = tk.Label(frame_baixo, text='Razão Social:', anchor=tk.NW, font=('Ivy 13 bold'), bg=co1, fg=co4, relief='flat')
label_razao_social.place(x=10, y=70)

entry_razao_social = tk.Entry(frame_baixo, width=45, justify='left',  relief='solid')
entry_razao_social.place(x=15, y=100)


label_qualificacao_responsavel = tk.Label(frame_baixo, text='Qualificação Responsável:', anchor=tk.NW, font=('Ivy 13 bold'), bg=co1, fg=co4, relief='flat')
label_qualificacao_responsavel.place(x=10, y=130)

entry_qualificacao_responsavel = tk.Entry(frame_baixo, width=45, justify='left',  relief='solid')
entry_qualificacao_responsavel.place(x=15, y=160)


label_capital_social = tk.Label(frame_baixo, text='Capital Social:', anchor=tk.NW, font=('Ivy 13 bold'), bg=co1, fg=co4, relief='flat')
label_capital_social.place(x=10, y=190)

entry_capital_social = tk.Entry(frame_baixo, width=45, justify='left',  relief='solid')
entry_capital_social.place(x=15, y=220)

label_porte_empresa = tk.Label(frame_baixo, text='Porte da Empresa:', anchor=tk.NW, font=('Ivy 13 bold'), bg=co1, fg=co4, relief='flat')
label_porte_empresa.place(x=10, y=250)

entry_porte_empresa = tk.Entry(frame_baixo, width=45, justify='left',  relief='solid')
entry_porte_empresa.place(x=15, y=280)


label_ente_federativo = tk.Label(frame_baixo, text='Ente Federativo:', anchor=tk.NW, font=('Ivy 13 bold'), bg=co1, fg=co4, relief='flat')
label_ente_federativo.place(x=10, y=310)

entry_ente_federativo = tk.Entry(frame_baixo, width=45, justify='left',  relief='solid')
entry_ente_federativo.place(x=15, y=340)


label_descricao_natureza_juridica = tk.Label(frame_baixo, text='Descrição da Naturaza Juridica:', anchor=tk.NW, font=('Ivy 13 bold'), bg=co1, fg=co4, relief='flat')
label_descricao_natureza_juridica.place(x=10, y=370)

entry_descricao_natureza_juridica = tk.Entry(frame_baixo, width=45, justify='left',  relief='solid')
entry_descricao_natureza_juridica.place(x=15, y=400)


label_descricao_porte_empresa = tk.Label(frame_baixo, text='Descrição do Porte da Empresa:', anchor=tk.NW, font=('Ivy 13 bold'), bg=co1, fg=co4, relief='flat')
label_descricao_porte_empresa.place(x=10, y=430)

entry_descricao_porte_empresa = tk.Entry(frame_baixo, width=45, justify='left',  relief='solid')
entry_descricao_porte_empresa.place(x=15, y=460)



botao_inserir = tk.Button(frame_baixo, command=inserir, text='Inserir', width=10, font=("ivi 9 bold"), bg=co6, fg=co1, relief='raised', overrelief='ridge')
botao_inserir.place(x=15, y=510)


botao_atualizar = tk.Button(frame_baixo, command=atualizar, text='Atualizar', width=10, font=("ivi 9 bold"), bg=co2, fg=co1, relief='raised', overrelief='ridge')
botao_atualizar.place(x=110, y=510)


botao_deletar = tk.Button(frame_baixo, command=deletar, text='Deletar', width=10, font=("ivi 9 bold"), bg=co7, fg=co1, relief='raised', overrelief='ridge')
botao_deletar.place(x=205, y=510)


def mostrar():
    global tree

    lista = mostar_info()

    tabela_head = ['ID','CNPJ', 'RAZÃO SOCIAL','QUALIFICAÇÃO RESPONSÁVEL', 'CAPITAL SOCIAL', 'PORTE DA EMPRESA', 'ENTE FEDERATIVO', 'DESCRIÇÃO NATUREZA JURÍDICA','DESCRIÇÃO PORTE DA EMPRESA']


    tree = ttk.Treeview(frame_direita, selectmode="extended", columns=tabela_head, show="headings")

    vsb = ttk.Scrollbar(frame_direita, orient="vertical", command=tree.yview)

    hsb = ttk.Scrollbar( frame_direita, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    frame_direita.grid_rowconfigure(0, weight=12)


    hd=["center","center","center","center","center","center","center","center","center"]
    h=[40,130,130,130,130,130,130, 180, 180]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=tk.CENTER)
        tree.column(col, width=h[n],anchor=hd[n])

        n+=1

    for item in lista:
        tree.insert('', 'end', values=item)


mostrar()

janela.mainloop()