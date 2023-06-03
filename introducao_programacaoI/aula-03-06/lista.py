# Criando uma lista
nomes = ['Jose','Carlos','Soares']

print(nomes)

# Imprimindo o tipo de dados
print(f'O tipo do dado é: {type(nomes)}')

# Imprimindo a posição pelo índice
print(f'Imprimindo a posição 0-> {nomes[0]}')

# Alterando o valor do índice
nomes[1] = 'Júnior'
print(nomes)

# Inserindo um valor na lista
nomes.insert(1, 'Carlos')
print(nomes)

# Removendo um valor da lista
del nomes[0]
print(nomes)

# Identificando índice do valor
indice_carlos = nomes.index('Carlos')
print(f'O indice da melancia é: {indice_carlos}')