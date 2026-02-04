numeros = [-12, 5, -3, 18, -7, 0, 9, -25, 4, -1, 30, -6]

indice_num = []
for indece, valor in enumerate(numeros):
    if valor < 0:
        indice_num.append(indece)

for n in indice_num:
    numeros[n] = 0
print(numeros)