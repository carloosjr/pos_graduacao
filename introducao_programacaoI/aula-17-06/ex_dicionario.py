# Exemplo de um dicionário

# Definindo um dicionário

professor = {
    'nome': 'Jose',
    'idade': 26
}

aluno = {
    'nome': 'Carlos',
    'idade': 26
}

print(professor['nome'])
print(aluno['nome'])

print(aluno['idade'])
print(professor['idade'])

professores = {
    'Jose': {'idade':26, 'disciplinas': ['Python', 'Java', 'BD']},
    'Carlos': {'idade':26, 'disciplinas':['HTML', 'JavaScprit']}
}

print(professores['Jose'])
print(professores['Carlos'])
print(professores)

print(f'O professor Carlos'
      f' tem {professores["Carlos"]["idade"]}'
      f' anos, e ministra as disciplinas'
      f' de {professores["Carlos"]["disciplinas"]}')

# Adicionando novos dados
professores['Carlos']['email'] = 'josecarlosoares7@gmail.com'
professores['Carlos']['cpf'] = '097.181.994-70'

print(professores['Carlos'])