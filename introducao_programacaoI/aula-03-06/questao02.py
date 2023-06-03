# Precisamos de um programa de computador que calcule a quantidade de
# latas de tinta e o custo total para pintar tanques cilíndricos de
# combustível.
# Sabemos que:
# ● A lata de tinta custa R$ 50,00
# ● Cada lata contém 5 litros
# ● Cada litro de tinta pinta 3 metros quadrados
import math

PI = math.pi
raio = float(input("Informe  o raio: \n"))
altura = float(input("Informe a altura: \n"))

area_base = PI * (raio ** 2)
area_lateral = 2 * PI * raio * altura
area_cilindro = area_base + area_lateral
quantidade_total_litros = area_cilindro /3
quantidade_latas_tintas = math.ceil(quantidade_total_litros /5)
custo_total = quantidade_latas_tintas * 50  

print(f'A quantidade de latas de tintas que serão necessárias é {quantidade_latas_tintas} latas')
print(f'O custo total será de R${custo_total:0.2f}')