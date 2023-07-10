import csv

with open('arquivo_csv.csv','r',encoding='utf-8', newline='')as arquivo:
    leitor = csv.reader(arquivo,delimiter=';')
    for contador in leitor:
        print(contador)