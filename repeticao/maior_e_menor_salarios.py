"""
A Entrada consiste de:
De um número inteiro N na primeira linha, o número de colaboradores na empresa.
N linhas contendo uma string com o nome do colaborador, seguido do seu salário em ponto flutuante com duas casas decimais.
O valor do salário é maior do que R$ 0.00 e menor do que R$ 1000000000,00.
O nome e o salário estão separados por vírgulas e não por espaços em branco.

A Saída deve apresentar:
O valor da média salarial da empresa na primeira linha, com duas casas decimais;
Se não houver média imprimir "Não tem média".
Na segunda linha o nome do colaborador com maior salário  e o seu salário;
Na terceira linha o nome do colaborador com menor salário  e o seu salário;

Exemplo de entrada:
2
Maria,1.00
José,2.00

"""



nome_maior_salario = 'Não tem'
nome_menor_salario = 'Não tem'
maior_salario = 0
menor_salario = 1000000000
total_salarios = 0

quantidade = int(input())

for i in range(quantidade):
    nome, salario = input().split(',')
    salario = float(salario)
    total_salarios += salario
    
    if salario < menor_salario:
        menor_salario = salario
        nome_menor_salario = nome
    if salario > maior_salario:
        maior_salario = salario
        nome_maior_salario = nome

    
    
if quantidade == 0:
    print('Não tem média')
    print('Não tem')
    print('Não tem')
else:
    media = total_salarios/quantidade
    print(f'{media:.2f}')
    print(f'{nome_maior_salario} {maior_salario:.2f}')
    print(f'{nome_menor_salario} {menor_salario:.2f}')
    