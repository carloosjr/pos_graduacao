# Criando funções para serem importadas em outro arquivo
# Criando funções individuais com diversos argumentos

def somar(*args):
    resultado = 0
    for i in args:
        resultado += i
    return resultado

def subtracao(*args):
    resultado = 0
    for i in args:
        resultado -= i
    return resultado

def multiplicacao(*args):
    resultado = 0
    for i in args:
        resultado *= i
    return resultado

def divisao(*args):
    resultado = 0
    for i in args:
        resultado /= i
    return resultado
