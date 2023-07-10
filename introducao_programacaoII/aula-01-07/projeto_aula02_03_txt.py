import projeto_funcoes
from datetime import datetime
import os

# Função para limpar a tela
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# lista_nomes = ['Messias', 'Neymar', 'Messi', 'Cristiano']
lista_nomes = projeto_funcoes.ler_arquivo()

while True:

    print('1 - Adicionar\n'
          '2 - Pesquisar\n'
          '3 - Listar\n'
          '4 - Remover\n'
          '5 - Alterar\n'
          '6 - Gerar lista\n'
          '7 - Ler arquivo\n'
          '8 - Gerar log\n'
          '0 - Sair')

    opcao = int(input('Digite a opção desejada: '))
    limpar_tela()
    
    match opcao:
        case 1:
            lista_nomes = projeto_funcoes.adicionar(lista=lista_nomes)
            projeto_funcoes.gerar_log_adicionar()

        case 2:
            projeto_funcoes.pesquisar(lista=lista_nomes)
            print(f'{datetime.now()} - Pesquisa realizada com sucesso')

        case 3:
            projeto_funcoes.listar(lista=lista_nomes)
            print(f'{datetime.now()} - Listagem realizada com sucesso')

        case 4:
            lista_nomes = projeto_funcoes.remover(lista=lista_nomes)
            print(f'{datetime.now()} - Remoção de usuário realizada com sucesso')

        case 5:
            lista_nomes = projeto_funcoes.alterar(lista=lista_nomes)
            print(f'{datetime.now()} - Alteração de usuário realizada com sucesso')
            
        case 6:
            lista_nomes = projeto_funcoes.gerar_nomes_txt(lista=lista_nomes)
            print(f'{datetime.now()} - Usuários persistidos com sucesso')
            
        case 7:
            lista_nomes = projeto_funcoes.ler_arquivo()
            print(f'{datetime.now()} - Arquivo recuperado com sucesso')
            
        case 8:
            lista_nomes = projeto_funcoes.gerar_log()

        case 0:
            print(f'Programa finalizando...')
            break
