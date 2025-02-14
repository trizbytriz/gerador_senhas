import tkinter as tk
from tkinter import messagebox
from logica.gerador import gerar_senha

def gerar_senha_inter():
    try:
        comprimento = int(entry_comprimento.get())
        usar_letras = var_letras.get()
        usar_numeros = var_numeros.get()
        usar_simbolos = var_simbolos.get()

        senha = gerar_senha(comprimento, usar_letras, usar_numeros, usar_simbolos)
        entry_senha.delete(0, tk.END)
        entry_senha.insert(0, senha)
    except ValueError as e:
        messagebox.showerror('Error',str(e))

def copiar_senha():
    senha = entry_senha.get()
    if senha:
        root.clipboard_clear()
        root.clipboard_append(senha)
        messagebox.showinfo('Copiado', 'A senha foi copiada para a área de transferência.')
    else:
        messagebox.showwarning('Aviso', 'Nenhuma senha para copiar!')

#criar janela principal
root = tk.Tk()
root.title('Gerador de Senha')
root.geometry('400x400')
root.configure(bg='#FFC0CB') #cor de fundo rosa claro

# Rotulo de titulo
label_titulo = tk.Label(root, text ='Gerador de Senhas', font = ('Arial',16, 'bold'), bg = '#FFC0CB', fg = '#800080')
label_titulo.pack(pady=10)

#Entrada para comprimento
frame_comprimento = tk.Frame(root, bg = '#FFC0CB')
frame_comprimento.pack(pady=5)
label_comprimento = tk.Label(frame_comprimento, text = 'Comprimento da senha:', bg = '#FFC0CB', font = ('Arial', 12))
label_comprimento.pack(side = tk.LEFT)
entry_comprimento = tk.Entry(frame_comprimento, width=5, font = ('Arial', 12))
entry_comprimento.pack(side = tk.LEFT, padx = 5)

#checkboxes para opcoes
var_letras = tk.BooleanVar(value=True)
var_numeros = tk.BooleanVar(value=True)
var_simbolos = tk.BooleanVar(value = False)

check_letras = tk.Checkbutton(root, text = 'Incluir Letras', variable = var_letras, bg = '#FFC0CB', font = ('Arial',12))
check_letras.pack(anchor = 'w', padx=20)
check_numeros = tk.Checkbutton(root, text = 'Incluir Números', variable = var_numeros, bg = '#FFC0CB', font = ('Arial', 12))
check_numeros.pack(anchor = 'w', padx=20)
check_simbolos = tk.Checkbutton(root, text = 'Incluir Símbolos', variable = var_simbolos, bg = '#FFC0CB', font = ('Arial', 12))
check_simbolos.pack(anchor = 'w', padx=20)

#botao gerar senha
btn_gerar = tk.Button(root, text = 'Gerar Senha', command = gerar_senha_inter, bg = '#FF69B4', fg = 'pink', font = ('Arial', 12, 'bold'))
btn_gerar.pack(pady=10)

#campo para exibir a senha gerada
entry_senha = tk.Entry(root, font = ('Arial', 14), justify = 'center', state = 'normal', width = 30)
entry_senha.pack(pady=10)

#botao para copiar a senha
btn_copiar = tk.Button(root, text = 'Copiar Senha', command = copiar_senha, bg = '#FF1493', fg = 'pink', font = ('Arial', 12, 'bold'))
btn_copiar.pack(pady=10)

root.mainloop()