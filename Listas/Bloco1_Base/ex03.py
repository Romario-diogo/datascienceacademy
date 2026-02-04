numeros = [34, 7, 128, 56, 19, 3, 92, 41, 15, 65]

menor = numeros[0]

for i in numeros:
    if i < menor:
        menor = i
    
print(f"Menor numero da lista com for {menor}")
print(f"Menor nnumero da lista com max {min(numeros)}")