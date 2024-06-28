"""
Programa para formatação utilizando espaços a esquerda ou direita e preenchimento de zeros.

Recebe 2 inteiros como entrada, exemplo: 2 e 5
Na saída, uma formatação diferente por linha:

I1 = 2, I2 = 5
I1 = 2         , I2 = 5
I1 = 2, I2 =     5
I1 = 2         , I2 = 0005
I1 = 000002, I2 = 0005

"""

x = int(input())
y = int(input())

print(f"I1 = {x}, I2 = {y}")
print(f"I1 = {x: <10}, I2 = {y}")
print(f"I1 = {x}, I2 = {y: >5}")
print(f"I1 = {x: <10}, I2 = {y:04}")
print(f"I1 = {x:06}, I2 = {y:04}")