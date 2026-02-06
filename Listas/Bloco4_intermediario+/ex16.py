"""
Verifique se a lista está em ordem crescente.
NÃO pode: sorted() nem sort().

receber primeiro valor 
percorra a lista de numeros 
for i in numeros:


pegar o segundo valor 
pelo indice 

"""
numeros = [1, 2, 3, 7, 10, 11, 12, 20, 5, 6, 30, 31]
tamanho = len(numeros)
crescente = True
for cont in range(1,tamanho):
    n_atual = numeros[cont-1]
    n_proximo = numeros[cont]
    if n_atual > n_proximo:
        print("A Lista não é crescente")
        crescente = False
        break
if crescente:
    print("A Lista é Crescente")

