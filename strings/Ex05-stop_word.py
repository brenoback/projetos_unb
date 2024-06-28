"""
Programa que recebe como entrada um tweet de Mei e a palavra a ser censurada, 
caso a palavra a ser censurada esteja no tweet, imprime com a censura, caso contrário imprime "tudo certo :)". 


A Entrada consiste de:
Uma string de tamanho variado representando um tweet de Mei e uma string sem espaços representando a palavra a ser censurada do tweet.

A Saída deve apresentar:
Uma string de tamanho variado como especificado no enunciado.

"""


frase = input()
palavra_censurada = input()

if palavra_censurada in frase:
    frase = frase.replace(palavra_censurada, '*')
    print(frase)
else:
    print('tudo certo :)')