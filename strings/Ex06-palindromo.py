palavra = input()
palavra_invertida = palavra[::-1]
tamanho = len(palavra)
diferencas = 0

for i in range(tamanho):
        if palavra[i] != palavra_invertida[i]:
            diferencas += 1

print(diferencas)
