# # Funcionalidades
# 1- Adicionar Pessoas
# 2- Pesquisar pessoa

# Importando biblioteca e declarando função para limpar a tela
import os
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

lista = []
while True:
    print("1 - Adicionar\n")
    print("2 - Pesquisar\n")
    print("3 - Listar\n")
    print("4 - Remover\n")

    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        nome_pessoa = input("Informe o nome da pessoa: ")
        lista.append(nome_pessoa)
        limpar_tela()
        
    elif opcao == 2:
        nome_pesquisa = input("Digite o nome a ser pesquisado: ")
        limpar_tela()
        if nome_pesquisa in lista:            
            print(f'O nome {nome_pesquisa} está na lista')
        else:
            print("O nome informado não está na lista")
    
    elif opcao == 3:
        for nome in lista:
            print(f'--> {nome}')
            
    elif opcao == 4:
        lista.remove(input("Informe o nome a ser removido: "))