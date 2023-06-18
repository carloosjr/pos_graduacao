# Criando funções 
def calculadora (numero1, numero2):
    resultado_soma = numero1 + numero2
    resultado_subtracao = numero1 - numero2
    resultado_multiplicacao = numero1 * numero2
    resultado_divisao = numero1 / numero2
    
    return print(f'O resultado da soma é {resultado_soma}\n',
                 f'O resultado da subtração é {resultado_subtracao}\n',
                 f'O resultado da multiplicação é {resultado_multiplicacao}\n',
                 f'O resultado da divisão é {resultado_divisao:0.2f}')
    

numero1 = int(input("Informe o primeiro número: \n"))
numero2 = int(input("Informe o segundo número: \n"))

calculadora(numero1, numero2)