numeros = [34, 7, 128, 56, 19, 3, 92, 41, 15, 65]

maior = numeros[0]

for i in numeros:
    if i > maior:
        maior = i
    
print(f"Maior numero da lista com for {maior}")
print(f"Maior nnumero da lista com max {max(numeros)}")