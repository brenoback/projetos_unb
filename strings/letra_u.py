"""
Função que verfica se determinada palavra não possuí a letra "u".
Caso a palavra não possuir a letra U, a função retorna True
Caso a palavra possua a letra U, a função retorna False

A função recebe um parâmetro, uma palavra no formato de string
Exemplo de utilização: print(nao_possui_a_letra_u('Universidade'))

"""


def nao_possui_a_letra_u(palavra):
    todos_u = ['u', 'ú', 'ù', 'û', 'ü']
    for letra in palavra.lower():
        if letra in todos_u:
            return False
    return True

