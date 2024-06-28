"""A Entrada consiste de:

A entrada contém 4 valores: dois inteiros (100≤PA,PB≤1000000) indicando respectivamente a população de A e B,
e dois valores (0.0≤T1,T2≤100.0), indicando respectivamente, em percentual, o crescimento populacional de A e B.

A Saída deve apresentar:
"Mais de um milenio." se a quantidade de anos for superior a 1000, 
"Vai alcancar em X ano(s).", onde X representa a quantidade de anos para a população de A alcançar o tamanho da população de B,
ou "A nunca alcancara B.", se a população nunca for alcançar a população de B.

"""


populacao_a, populacao_b, taxa_a, taxa_b = input().split()

populacao_a, populacao_b = int(populacao_a), int(populacao_b)
taxa_a, taxa_b = float(taxa_a), float(taxa_b)

anos = 0

if taxa_a > taxa_b:
    while populacao_a < populacao_b:
        populacao_a += int(populacao_a *(taxa_a/100))
        populacao_b += int(populacao_b *(taxa_b/100))
        anos += 1

if taxa_b > taxa_a:
    print('A nunca alcancara B.')
elif anos > 1000:
    print('Mais de um milenio.')
else:
    print(f'Vai alcancar em {anos} ano(s).')