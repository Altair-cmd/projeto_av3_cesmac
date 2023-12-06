

def verificar_number1(numero):
    numero.isnumeric()
    while(numero.isnumeric()) == False:
        print("Digite um valor válido ")
        numero = (input(" "))
    numero = float(numero)
    return numero