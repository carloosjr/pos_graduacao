# A partir do ano de nascimento de uma pessoa mostrar
# sua idade, se já tem idade para votar (16 anos ou
# mais) e se já pode ser candidato a uma carteira de
# habilitação.
# Dados de entrada: ano de nascimento
# Saída: idade, idade para votar, idade para dirigir

# Importando biblioteca de data
import datetime

ano_atual = datetime.datetime.now().year

ano_nascimento = int(input("Informe o seu ano de nascimento:\n"))
idade = ano_atual - ano_nascimento

if idade >=16:
    print("Você está apto para votar!")
    if idade >=18:
        print("Você já pode tirar sua CNH!")
    else:
        print("Você não está apto para tirar a CNH")
    
elif idade <16:
    print("Você não está apto para votar e nem para tirar sua CNH!")