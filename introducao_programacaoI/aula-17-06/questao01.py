# Imagine que precisamos imprimir números para uma
# rifa da igreja da Vovó. Uma listagem de números
# entre 1 e 1000.

# Solucione o problema da Vovó com Python.

numero_rifa = 0

while numero_rifa < 1000:
    # Declaração normal
    # numero_rifa = numero_rifa +1
    numero_rifa += 1
    print(f'O número da rifa é: {numero_rifa}')

# controle = 0
# while True:
#     print(f'{controle} - SPFC')
#     controle += 1
#     if controle > 1000:
#         break