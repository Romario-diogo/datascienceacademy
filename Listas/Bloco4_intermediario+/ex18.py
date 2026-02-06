"""“Rotacione” a lista para a direita 1 vez.
Ex: [1,2,3,4] → [4,1,2,3]
NÃO pode: slicing."""

numeros = [1, 2, 3, 29, 7, 10, 11, 12, 20, 5, 6, 22, 31]

ultimo = numeros.pop()
numeros.insert(0, ultimo)
print(numeros)