import re

def valida_endereco(endereco):
    regex = r'^[a-zA-Z0-9\s]+$'
    while bool(re.match(regex,endereco)) == False:
        print("Digite um valor válido")
        endereco = (input(" "))
    return endereco






