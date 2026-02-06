"""Encontre o segundo maior número da lista.
NÃO pode: sort(), sorted(), max()."""

numeros = [1, 2, 3, 29, 7, 10, 11, 12, 20, 5, 6, 22, 31]
maior = numeros[0]
segundomaior = numeros[0]

for n in numeros:
    if n > maior:
        maior = n

for n in numeros:
    if n < maior and n > segundomaior:
        segundomaior = n

print(maior)
print(segundomaior)