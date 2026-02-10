#numeros = [34, 7, 128, 56, 19, 3, 92, 41, 15, 65]

numeros = [10, 20, 10, 30]

# Usando o interador 

it = iter(numeros)
primeiro_it = next(it)

for ultimo in it:
    pass

print(f"{primeiro_it}, {ultimo}")

numeros.remove(primeiro_it)
numeros.remove(ultimo)
print(numeros)