import random
import string

def gerar_senha(comprimento, usar_letras, usar_numeros, usar_simbolos):
    caracteres = ""

    if usar_letras:
        caracteres += string.ascii_letters #letras maiúsculas e minusculas
    if usar_numeros:
        caracteres += string.digits #Números de 0 a 9
    if usar_simbolos:
        caracteres += string.punctuation #simbolos
    if not caracteres:
        return "Selecione pelo menos uma opção de caracteres!"

    senha = "".join(random.choice(caracteres)for _ in range(comprimento))
    return senha