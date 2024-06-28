"""
Função recebe 3 números como parametro, represento 3 medidas diferentes. 

Calcula e imprime a área do retângulo utilizando A e B como Altura e Largura
Calcula e imprime a área do triângulo utilizando B e C como Base e Altura
Calcula e imprime a área do trapézio utilizando B, C e A como base maior, base menor e altura
Todas as saídas são no formato inteiro.

"""

def areas(A, B, C):
    areaR = A*B
    areaT = (B*C)/2
    areaTP = (((B+C)*A)/2)
    
    print(f'A área do retângulo utilizando a altura {A} e a lagura {B} é igual a {int(areaR)}')
    print(f'A área do triângulo utilizando a base {B} e a altura {C} é igual a {int(areaT)}')
    print(f'A área do triângulo utilizando a base menor {B}, a base maior {C} e a altura {A} é igual a {int(areaT)}')


areas(5,3,4)