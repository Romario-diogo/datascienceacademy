"""Remova valores duplicados mantendo a ordem original."""

numeros = [7, 3, 9, 3, 12, 7, 5, 9, 1, 12, 4, 7, 2]
numeros_copia = numeros.copy()

tamanho = len(numeros_copia)

for i in range(tamanho):
    numero = numeros_copia[i]
for indice, valor in enumerate(numeros_copia):
    if numero == valor:
        print(indice, valor)