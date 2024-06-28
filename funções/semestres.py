"""
Função recebe 3 parâmetros:
Uma matrícula da UnB no formato 110001020
O ano atual
O semestre atual

A função calcula com base nessas informações em qual período o aluno está
Contando que os dois primeiros números da matrícula indicam o ano de ingresso
E os dois números seguintes indicam em qual semestre do ano o aluno entrou. 00 para o primeiro e 01 para o segundo.

Exemplo de utilização: print(qual_periodo(230063980, 2024, 0))

"""


def qual_periodo(m, a, s):
    semestre_atual = s
    matricula = m
    ano_atual = str(a)[-2:]
    ano_atual = int(ano_atual)
    
    #Ano de ingresso
    primeiros2 = str(m)[:2]
    primeiros2 = int(primeiros2)

    #Semestre de ingresso se for 00 entrou no 1 se for 01 entrou no 2
    segundos2 = str(m)[3:4]
    segundos2 = int(segundos2)

    diferencasemestres = semestre_atual - segundos2
    quantos_s = (ano_atual - primeiros2) * 2 + diferencasemestres

    quantos_s += 1


    return quantos_s
    
   



print(qual_periodo(230063980, 2024, 0))