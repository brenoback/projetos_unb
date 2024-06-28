"""

A primeira linha da entrada contém dois inteiros: quantidade de amigos e preço do ingresso separados por espaço.
Cada uma das próximas n linhas contém um inteiro representando o dinheiro que cada amigo possui.

A Saída deve apresentar:
A primeira linha da saída deve conter a parte inteira do dinheiro médio para cada amigo, conforme os exemplos.
A segunda linha deve conter a mensagem "o rock reinara mais uma vez" se houver dinheiro o suficiente para todos, ou a mensagem "rockeiros trabalhando ja" em caso contrário.

Exemplo de entrada:
6 300
350
300
300
230
400
300

Saída esperada:
media: 313
o rock reinara mais uma vez

"""


quantidade, preco = input().split()
quantidade = int(quantidade)
preco = int(preco)

total = 0

for i in range(quantidade):
    valor = int(input())
    total += valor

media = int(total/quantidade)

print(f'media: {media}')

if media >= preco:
    print('o rock reinara mais uma vez')
else:
    print('rockeiros trabalhando ja')