"""
Programa que recebe uma string e verifica se ela contém uma vírgula. Caso tenha, imprima "passed", caso contrário imprima "failed".


A Entrada consiste de:
Uma string de tamanho variável.

A Saída deve apresentar:
Uma string como especificado no enunciado.
 
"""


string = input()

if "," in string:
    print('passed')
else:
    print("failed")