"""
Função que recebe um valor no formato inteiro e calcula o troco na menor quantidade de moedas possível.

Exemplo de uso: troco(150)
Saída: 3 moeda(s) de 50 centavos

"""

def troco(x):
 
    total = x

    moedas = 50
    total_moedas = 0
    while True:
        if total >= moedas:
            total -= moedas
            total_moedas += 1
        else: 
            if moedas == 1:
                print(f'{total_moedas} moeda(s) de {moedas} centavo')
            else:
                print(f'{total_moedas} moeda(s) de {moedas} centavos')
            if moedas == 50:
                moedas = 25
            elif moedas == 25:
                moedas = 10
            elif moedas == 10:
                moedas = 5
            elif moedas == 5:
                moedas = 1
            total_moedas = 0
            if total == 0:
                break
        

troco(150)