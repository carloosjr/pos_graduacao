# Um programa que permita saber qual o peso ideal de
# uma pessoa.
# ● Para homens: (72,7 * h) - 58
# ● Para mulheres: (62,1 * h) - 44,7
# Dados de entrada: altura e sexo de uma pessoa.

altura = float(input("Informe sua altura: \n"))

print("Informe o sexo:")
print("M -> Para Masculino")
print("F -> Para Feminino")

sexo = input("Informe o sexo:\n").upper()

if sexo == 'M':
    peso_ideal = (72.7 * altura) - 58
    print(f'O Peso ideal seria {peso_ideal:0.2f}')

elif sexo == 'F':
    peso_ideal = (62.1 * altura) - 44.7
    print(f'O peso ideal seria {peso_ideal:0.2f}')

else:
    print("Valor informado incorreto!")