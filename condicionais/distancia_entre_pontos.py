"""
A Entrada consiste de:
4 linhas, todas com variáveis do tipo inteiro, sendo as duas primeiras (x1,y1) a localização de Carêncio e as duas últimas (x2,y2) a localização de sua mais nova paquera.


A Saída deve apresentar:
Umas das três frases ("É o amor da minha vida!", "Talvez dê certo", "Não vale a pena investir") de acordo com a distância.

D ≤ 100: ''É o amor da minha vida!"
100 < D ≤ 200: "Talvez dê certo"
D > 200: "Não vale a pena investir"

"""


x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

d = ((x2 - x1)**2 + (y2 - y1)**2)**(1/2)

if d <= 100:
    print("É o amor da minha vida!")
elif d > 100 and d <= 200:
    print("Talvez dê certo")
else:
    print("Não vale a pena investir")