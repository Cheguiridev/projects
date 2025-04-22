import tkinter as tk
from tkinter import font


root = tk.Tk()
root.title("Calculadora Python Moderna")
root.geometry("320x500")
root.resizable(False, False)
root.configure(bg="#2E2E2E") 


fonte_display = font.Font(family="Arial", size=24, weight="bold")
fonte_botoes = font.Font(family="Arial", size=14, weight="bold")


cor_display = "#3D3D3D"
cor_botoes_numeros = "#5A5A5A"
cor_botoes_operadores = "#FF9500"
cor_botoes_especiais = "#A5A5A5"
cor_texto = "#FFFFFF"


expressao = ""
entrada_texto = tk.StringVar()


def adicionar_caractere(caractere):
    global expressao
    expressao += str(caractere)
    entrada_texto.set(expressao)

def calcular():
    global expressao
    try:
        resultado = str(eval(expressao))
        entrada_texto.set(resultado)
        expressao = resultado
    except:
        entrada_texto.set("Erro")
        expressao = ""

def limpar():
    global expressao
    expressao = ""
    entrada_texto.set("")


display = tk.Entry(
    root,
    textvariable=entrada_texto,
    font=fonte_display,
    bg=cor_display,
    fg=cor_texto,
    borderwidth=0,
    justify="right",
    insertbackground=cor_texto
)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=20, ipady=10, sticky="nsew")


botoes = [
    ('C', 1, 0, cor_botoes_especiais), ('⌫', 1, 1, cor_botoes_especiais), ('%', 1, 2, cor_botoes_operadores), ('/', 1, 3, cor_botoes_operadores),
    ('7', 2, 0, cor_botoes_numeros), ('8', 2, 1, cor_botoes_numeros), ('9', 2, 2, cor_botoes_numeros), ('*', 2, 3, cor_botoes_operadores),
    ('4', 3, 0, cor_botoes_numeros), ('5', 3, 1, cor_botoes_numeros), ('6', 3, 2, cor_botoes_numeros), ('-', 3, 3, cor_botoes_operadores),
    ('1', 4, 0, cor_botoes_numeros), ('2', 4, 1, cor_botoes_numeros), ('3', 4, 2, cor_botoes_numeros), ('+', 4, 3, cor_botoes_operadores),
    ('0', 5, 0, cor_botoes_numeros, 2), ('.', 5, 2, cor_botoes_numeros), ('=', 5, 3, cor_botoes_operadores)
]


def criar_botao(texto, linha, coluna, cor, colspan=1):
    botao = tk.Button(
        root,
        text=texto,
        command=lambda: adicionar_caractere(texto) if texto not in ('C', '⌫', '=') else limpar() if texto == 'C' else calcular(),
        bg=cor,
        fg=cor_texto,
        font=fonte_botoes,
        borderwidth=0,
        activebackground="#777777" if cor == cor_botoes_numeros else "#FFB143",
        relief="flat"
    )
    botao.grid(row=linha, column=coluna, columnspan=colspan, sticky="nsew", padx=5, pady=5, ipady=15)
    return botao


for botao in botoes:
    if len(botao) == 4:
        criar_botao(botao[0], botao[1], botao[2], botao[3])
    else:
        criar_botao(botao[0], botao[1], botao[2], botao[3], colspan=botao[4])


def apagar_ultimo():
    global expressao
    expressao = expressao[:-1]
    entrada_texto.set(expressao)

tk.Button(
    root,
    text="⌫",
    command=apagar_ultimo,
    bg=cor_botoes_especiais,
    fg=cor_texto,
    font=fonte_botoes,
    borderwidth=0,
    activebackground="#777777"
).grid(row=1, column=1, sticky="nsew", padx=5, pady=5, ipady=15)


for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
