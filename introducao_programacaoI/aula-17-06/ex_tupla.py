# Definição de uma Tupla

dimensoes = (200, 50, 22, 23, 24, 25, 26, 27, 28)

print(f'No índice 0 {dimensoes[0]}')
print(f'No índice 1 {dimensoes[1]}')


# Utilizando um For

for dimensao in dimensoes:
    print(dimensao)
    
# Percorrendo uma Tupla

for contador in dimensoes:
    print(f'Neste ciclo o valor do contador é {contador}')