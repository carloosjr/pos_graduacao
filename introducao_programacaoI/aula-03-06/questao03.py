# Um programa que verifique se existe permissão, a
# partir da idade, para entrar em uma festa.

# Importando biblioteca e declarando função para limpar a tela
import os
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

idade = int(input("Informe sua idade:\n"))
limpar_tela()

while idade <18:
    print("Você não tem idade para entrar na festa!\n")
    idade = int(input("Informe sua idade:\n"))
    limpar_tela()
    
tipo_ingresso = input("Informe o tipo de ingresso - VIP ou PISTA\n")
tipo_ingresso = tipo_ingresso.upper()

if idade >= 18 and tipo_ingresso == 'VIP':
    print("Você pode entrar na festa!\n")
    print("Siga para o primeiro andar!\n")
    
elif idade >=18 and tipo_ingresso == 'PISTA':
    print("Você pode entrar na festa!\n")
    print("Siga para o setor pista!\n")    
else:
    print("Você não pode entrar na festa!\n")