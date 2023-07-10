import datetime
from loguru import logger

def adicionar(lista):
    nome_pessoa = input('Digite o nome da pessoa: ')
    lista.append(nome_pessoa)

    return lista

def pesquisar(lista):
    nome_pesquisa = input('Digite o nome a pesquisa: ')

    if nome_pesquisa in lista:
        print(f'O nome {nome_pesquisa} está na lista.')

def listar(lista):

    for nome in lista:
        print(f'-> {nome}')

def remover(lista):

    nome_remover = input('Digite quem será removido: ')

    if nome_remover in lista:
        lista.remove(nome_remover)
    else:
        print('Nome não encontrados!')

    return lista

def alterar(lista):
    nome_alterar = input('Digite o nome a ser alterado: ')

    if nome_alterar in lista:
        print(f'O nome {nome_alterar} foi encontrado.')
        alteracao = input('Qual será o novo nome? ')
        lista[lista.index(nome_alterar)] = alteracao

    else:
        print('O nome não foi encontrado!')

    return lista

def gerar_nomes_txt(lista):
    conteudo = '\n'.join(lista)
    with open('nomes.txt','w',encoding='utf-8') as fo:
        fo.writelines(conteudo)
        
        
def ler_arquivo():
    with open('nomes.txt','r', encoding='utf-8') as fo:
        conteudo = fo.read()
        return (conteudo)
    
def gerar_log_adicionar():
    print(f'{datetime.now()} - Usuário adicionado com sucesso')
