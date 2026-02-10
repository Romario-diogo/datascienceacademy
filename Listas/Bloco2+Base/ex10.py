numeros = [-12, 5, -3, 18, -7, 0, 9, -25, 4, -1, 30, -6]

indice_num = []
for indece, valor in enumerate(numeros):
    if valor < 0:
        numeros[indece] = 0

print(numeros)