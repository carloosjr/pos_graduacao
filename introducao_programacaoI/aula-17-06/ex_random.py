from random import randint

# -> Exemplo com While

# lista_num = []
# controle = 0

# while controle <100:
#     numero_aleatorio = randint(0, 1000)
#     print(f'O número escolhido foi: {numero_aleatorio}')
#     lista_num.append(numero_aleatorio)
#     controle += 1
    
# print(lista_num)

# -> Exemplo com For

lista_num = []
for i in range(100):
    num_aleatorio = randint(0, 1000)
    print(f'O número escolhido foi: {num_aleatorio}')
    lista_num.append(num_aleatorio)

print(lista_num)

# Contadores
numero_impar = 0
numero_par = 0

for contador in lista_num:
    if num_aleatorio % 2 == 0:
        numero_par += 1
        
    else:
        numero_impar += 1
        
print(f'Esta lista tem {numero_par} números pares e '
      f'{numero_impar} ímpares')

