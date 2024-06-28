"""

Escreva um programa que leia 3 números inteiros positivos e efetue o cálculo das médias Aritmética (A), Ponderada (P) e Harmônica (H) dependendo da letra dada pelo usuário, 
mostre qual o tipo de média e qual o valor da média. No caso do usuário digitar qualquer outro caractere, apresente a mensagem 'Operacao inexistente'.


A Entrada consiste de:
Linha contendo as três notas que são três números reais positivos.
Linha contendo um caractere (para determinar qual a média), sendo (P) Ponderada, (H) Harmônica e (A) Aritmética
Caso o caractere seja 'P', deve-se solicitar os três pesos de cada nota enviada, que são números positivos inteiros.

A Saída deve apresentar:
Na primeira linha, o tipo de média que ele fez ("Harmonica", "Ponderada", "Aritmetica" ou "Operacao inexistente")
Na segunda linha, caso tenha sido digito um caractere válido, o resultado da média com precisão de 2 casas decimais.
    
"""


notas = input().split()

nota1 = int(notas[0])
nota2 = int(notas[1])
nota3 = int(notas[2])

tipo_media = input()


def ponderada():
    media_ponderada = ((nota1 * peso1) + (nota2 * peso2)  + (nota3 * peso3)) / (peso1+peso2+peso3)
    print("Ponderada")
    print(f'{media_ponderada:.2f}')

def harmonica():
    soma = (1/nota1) + (1/nota2) + (1/nota3)
    media_harmonica = 3/soma
    print("Harmonica")
    print(f'{media_harmonica:.2f}')

def aritmetica():
    media_aritmetica = (nota1 + nota2 + nota3) / 3
    print("Aritmetica")
    print(f'{media_aritmetica:.2f}')


if tipo_media == "P":
    pesos = input().split()
    peso1 = int(pesos[0])
    peso2 = int(pesos[1])
    peso3 = int(pesos[2])
    ponderada()
elif tipo_media == "H":
    harmonica()
elif tipo_media == "A":
    aritmetica()
else:
    print('Operacao inexistente')
