"""
Programa que recebe uma string e retorna a quantidade de dígitos numéricos contidas nela.

A Entrada consiste de:
Uma string de tamanho variável.

A Saída deve apresentar:
Um inteiro, representando a quantidade de dígitos numéricos contidos na string. 

"""


string = input()
count = 0

for i in string:
    if i.isnumeric():
        count += 1

print(count)