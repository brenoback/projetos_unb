"""
Programa recebe um tempo no formato hh:mm:ss
Programa devolve quantos segundos tem nesse tempo
 
"""

x = input('Digite um tempo no formato horas:minutos:segundos\n').split(":")
horas = int(x[0])
minutos = int(x[1])
segundos = int(x[2])
y = (horas*3600) + (minutos*60) + segundos
print(f"La se foram {y} segundos que nao voltam mais...")