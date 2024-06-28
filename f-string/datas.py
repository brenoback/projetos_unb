"""
Programa recebe como entrada uma data no formato DD/MM/AA   
A saida do programa é a data com 3 diferentes formatações.  

"""

x = input().split("/")

## Formato com hifens
print(f"{x[0]}-{x[1]}-{x[2]}")

## Formato em Ingles e com hifens
print(f"{x[1]}-{x[0]}-{x[2]}")

## Formato AA/MM/DD
print(f"{x[2]}/{x[1]}/{x[0]}")