# Construir um algoritmo que calcule a média aritmética entre
# quatro notas bimestrais fornecidas por um aluno (usuário).
# Dados de entrada: quatro notas (n1, n2, n3, n4)
# Dados de saída: média aritmética anual (ma)


# Importando biblioteca e declarando função para limpar a tela
import os
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

nota1 = float(input("Informe a primeira nota: \n"))
limpar_tela()
while nota1 <0:
        print("Informe um valor válido!")
        nota1 = float(input("Informe a primeira nota: \n"))
        
nota2 = float(input("Informe a segunda nota: \n"))
limpar_tela()
while nota2 <0:
        print("Informe um valor válido!")
        nota2 = float(input("Informe a segunda nota: \n"))


nota3 = float(input("Informe a terceira nota: \n"))
limpar_tela()
while nota3 <0:
        print("Informe um valor válido!")
        nota3 = float(input("Informe a terceira nota: \n"))
        
        
nota4 = float(input("Informe a quarta nota: \n"))
limpar_tela()
while nota4 <0:
        print("Informe um valor válido!")
        nota4 = float(input("Informe a quarta nota: \n"))

ma = (nota1+nota2+nota3+nota4)/4;

print(f'A média aritmética anual é {ma:0.2f}')

if ma >=7.0:
    print("Você está aprovado!")
    
elif ma >=4.0:
    print("Você está de recuperação")
    
else:
    print("Você foi reprovado!")
    