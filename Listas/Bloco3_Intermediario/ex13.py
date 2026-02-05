numeros = [4, 7, 2, 7, 9, 4, 3, 2, 10, 7, 5, 4]

nova_lista = []
for n in numeros:
    if n not in nova_lista:
        nova_lista.append(n)
print(nova_lista)