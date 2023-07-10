# Desenvolva um programa em Python para:
# - Todas as linhas do livro em anexo
# - Contar quantas linhas cada livro tem

# Importando biblioteca para criar a função de encerrar a aplicação
import sys
import os

# Função para encerrar o app
def encerrar_programa():      
    print("Encerrando a aplicação...")
    sys.exit()

# Função para limpar a tela
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

print('===== Leitura de Arquivos =====')
print('Opções:\n')
print('0 - Conto dos Irmãos Grimm\n')
print('1 - O Príncipe Maquiavel\n')

opcao = int(input('Escolha a opção:\n'))

# Realizar a leitura do arquivo a partir da escolha, convertendo pelo int

if opcao == 0:
    with open('contos_dos_irmaos_grimm.txt','r',encoding='utf-8') as fo:
        conteudo = fo.read()
        print(conteudo)   
    
    print('Deseja contar as linhas?\n')
    print('0 - Sim\n')
    print('1 - Não\n')
    contar = int(input('Escolha a opção:\n'))

    if  contar == 0:    
        with open('contos_dos_irmaos_grimm.txt','r', encoding='utf-8') as fo2:
            linhas = fo2.readlines()
            contador = 0
            for l in linhas:
                contador += 1
            print(f'O livro contém {contador} linhas')
    
    elif contar == 1:
        encerrar_programa()

    else:
        print('Opção incorreta!')
        
elif opcao == 1:
    with open('o_principe_maquiavel.txt','r',encoding='utf-8') as fo:
       conteudo = fo.read()
       print(conteudo)
       
    print('Deseja contar as linhas?\n')
    print('0 - Sim\n')
    print('1 - Não\n')
    contar = int(input('Escolha a opção:\n'))
    limpar_tela()

    if  contar == 0:    
        with open('o_principe_maquiavel.txt','r', encoding='utf-8') as fo2:
            linhas = fo2.readlines()
            contador = 0
            for l in linhas:
                contador += 1
            print(f'O livro contém {contador} linhas')
    
    elif contar == 1:
        encerrar_programa()
        
    else:
        print('Opção incorreta!')

else:
    print('Opção incorreta!')