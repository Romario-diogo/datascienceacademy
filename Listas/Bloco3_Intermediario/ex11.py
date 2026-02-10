numeros = [3, 7, 12, 25, 4, 18, 9, 30, 1, 6]

num_par = [n for n in numeros if n % 2 == 0]
num_impar = [n for n in numeros if n % 2 != 0]
print(num_impar)
print(num_par)