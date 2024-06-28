"""
Programa que recebe uma string e retorna os caracteres contidos nos índices ímpares dessa string, ignorando os espaços em branco. 
Mostra os caracteres um ao lado do outro numa mesma linha, sem espaços.


A Entrada consiste de:
Uma string de tamanho variável.

A Saída deve apresentar:
Uma string composta pelos caracteres contidos nos índices ímpares da string de entrada.

"""

string = input()

for i in range(len(string)):
    if i % 2 != 0:
        print(string[i].strip(), end='')