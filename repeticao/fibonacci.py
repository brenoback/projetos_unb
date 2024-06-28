"""
Função que recebe como parametro um número inteiro N, representando quantos termos da sequência de fibonacci o usuário quer ver
Função retorna a sequência de fibonacci dos N termos que o usuário escolheu

Exemplo de entrada: fibonacci(4)
Saida: 0 1 1 2

"""


def fibonacci(n):
    t1 = 0
    t2 = 1
    if n == 1:
        print(0)
        return
    elif n == 2:
        print(0, 1)
        return
    
    print(0, 1, end = ' ')
    for i in range(2, n):
        t3 = t1 + t2
        print(f'{t3}', end=' ')
        t1 = t2
        t2 = t3
