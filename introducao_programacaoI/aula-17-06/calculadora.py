# Criando calculadora importando as funções de outro arquivo

import funcoes

numero1 = input("Informe  o primeiro valor: \n")
numero2 = input("Informe  o segundo valor: \n")

numero1 = int(numero1)
numero2 = int(numero2)

while True:

    print("Informe a operação que deseja realizar: \n",
        '1 - Soma\n',
        '2 - Subtração\n',
        '3 - Multiplicação\n',
        '4 - Divisão\n',
        '5 - Sair'
        )

    operacao = input("Informe a operação desejada: \n")
    
    operacao = int(operacao)

    match operacao:
        case 1:
            resultado = funcoes.somar(numero1, numero2)
            print(f'A soma dos valores é {resultado}')
            
        case 2:
            resultado = funcoes.subtracao(numero1, numero2)
            print(f'A subtração dos valores é {resultado}')
            
        case 3:
            resultado = funcoes.multiplicacao(numero1, numero2)
            print(f'A multiplicação dos valores é {resultado}')
            
        case 4:
            resultado = funcoes.divisao(numero1, numero2)
            print(f'A divisão dos valores é {resultado}')
            
        case 5:
            break
                
        case _:
                print(f'Opção inválida!') 