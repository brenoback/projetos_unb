"""  
Programa recebe como entrada um número com pontos flutuantes (float)
A sáida do programa é o número com diferentes casas decimais: quatro, duas e o número inteiro (aproximado).

"""

print('Digite um número com pontos flutuantes. Exemplo: 25.923')
x = float(input())


print(f'O número com quatro casas decimais é: {x:.4f}')
print(f'O número com duas casas decimais é: {x:.2f}')
print(f'A aproximação para parte inteira desse número é: {x:.0f}')