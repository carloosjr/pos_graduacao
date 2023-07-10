print('===== Iniciando Programa =====')

print('Opções:\n')
print('0 - Sem Permissão\n')
print('1 - Com Permissão\n')

opcao = input('Escolha a opção:\n')

with open('permissoes.txt','r',encoding='utf-8') as fo:
    for linha in fo:
        if linha[0] == str(opcao):
            print(linha.rstrip())