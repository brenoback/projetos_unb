"""
Programa para formatação de strings.
A entrada é uma string qualquer
As saídas são:

Na primeira linha, a própria string
Na segunda linha, a string no formato: stringstring
Na terceira linha, a string no formato: string string:
Na quarta linha, a string no formato: 2string
Na quinta linha, a string no formato: [string]

"""

x = input()

print(x)
print(f"{x}{x}")
print(f"{x} {x}")
print(f"2{x}")
print(f"[{x}]")