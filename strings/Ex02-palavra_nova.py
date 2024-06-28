"""
Programa que recebe uma palavra e imprime uma palavra nova derivada desta, 
que é composta pelos dois primeiros caracteres da palavra de entrada com os dois últimos.


A Entrada consiste de:
Uma string que contém quatro ou mais caracteres.

A Saída deve apresentar:
Uma string representando a palavra nova.

"""

string = input()
nova_palavra = string[:2] + string [-2:]

print(nova_palavra)