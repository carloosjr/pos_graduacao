import csv

texto = [
            ['Carlos Jr',27],
            ['Soares', 22]
        ]
with open('escrita_csv.csv', 'w', encoding='utf-8', newline='') as arquivo:
    escritor = csv.writer(arquivo, delimiter=';')
    # escritor.writerow(texto)
    escritor.writerows(texto)
    