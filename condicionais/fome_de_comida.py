"""
    
A Entrada consiste de:
Uma variável M do tipo inteiro representando os minutos do relógio.

A Saída deve apresentar:

1 linha contendo a frase “Fome de comida! Queremos arroz e feijão” para casos com números pares 
ou a frase "Só um lanchinho cai bem!" para os casos ímpares

"""


m = int(input())

if m % 2 == 0:
    print('Fome de comida! Queremos arroz e feijão')
else:
    print('Só um lanchinho cai bem!')