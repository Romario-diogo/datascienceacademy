numeros = [34, 7, 128, 56, 19, 3, 92, 41, 15, 65]

primeiro, *meio, ultimo = numeros

print(primeiro)
print(ultimo)


# Usando o interador 

it = iter(numeros)
primeiro_it = next(it)

for ultimo in it:
    pass

print(f"{primeiro}, {ultimo}")

numeros.remove(primeiro)
numeros.remove(ultimo)
print(numeros)