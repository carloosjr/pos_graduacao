# Abrindo e lendo o arquivo em .txt
# Buscando o arquivo em outro diretório

diretorio = 'aula-01-07\\'
arquivo = 'arquivo.txt'
filepath = diretorio + arquivo

with open(filepath,'r', encoding='utf-8') as file_object:
    conteudo = file_object.read()
    print(conteudo)
    
with open('tasks.txt','r', encoding='utf-8') as fo:
    for linha in fo:
        if '1' in linha:
            print(f'Tipo: {type(linha)} | {linha.rstrip()}')