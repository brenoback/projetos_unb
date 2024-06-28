"""
Programa que recebe 3 entradas
Primeira entrada: 3 sabores de sorvete separados por vírgula
Segunda entrada: 2 sabores de cobertura separados por vírgula
Terceira entrada: sabor da calda

Como saída uma mensagem formatada dizendo os sabores, as coberturas e a calda.

Exemplo de entrada: 
Chocolate,Morango,Limão
Brigadeiro,MM's
Doce de Leite

Saída: Sorvete de Chocolate, Morango e Limão com coberturas de Brigadeiro e MM's e calda de Doce de Leite!

"""

sabores = str(input()).split(",")
coberturas = str(input()).split(",")
calda = str(input())

print(f"Sorvete de {sabores[0]}, {sabores[1]} e {sabores[2]} com coberturas de {coberturas[0]} e {coberturas[1]} e calda de {calda}!")
print("Não esqueça a banana!")