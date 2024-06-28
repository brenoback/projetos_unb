"""
A primeira função retorna 1 caso o número seja PRIMO e 0 caso não seja
A segunda função recebe como parametro um número inteiro N e encontra quais são os divisores desse número
Checa se os divisores são primos e devolve a quantidade de divisores primos que o número possui
 
"""


def ehPrimo(n):
    total = 0
    for i in range(1, n+1):
        if n % i == 0:
            total += 1
    
    if total == 2:
        return 1
    else:
        return 0

def divisoresPrimos(x):
    count = 0
    
    for i in range(1, x):
        if x % i == 0:
            if ehPrimo(i) == 1:
                count += 1

    return count