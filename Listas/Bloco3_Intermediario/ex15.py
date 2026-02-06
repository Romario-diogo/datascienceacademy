"""
Dada uma lista de nomes, normalize: tirar espaços das pontas e deixar tudo minúsculo.
NÃO pode: criar outra lista (tem que alterar a original).
"""

nomes = ["  JOAO  "," maria","Carlos ","  aNa ","PEDRO","  luCas  ","ANA"," roBerto ","  sofia","MARIA  "]

nomes_copy = nomes.copy()

for i, n in enumerate(nomes_copy):
    if n != n.strip():
        tratamento = n.lower().strip()
        nomes[i]= tratamento
    else:
        tratamento = n.lower().strip()
        nomes[i] = tratamento
print(nomes)